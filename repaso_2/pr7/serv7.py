#!/usr/bin/env python3
"""
serv7.py - Servidor de chat simple usando select()
Uso: python3 serv7.py
"""
import socket
import select
import signal
import sys

# Configuración del servidor
HOST = '0.0.0.0'     # Escuchar en todas las interfaces
PORT = 4000          # Puerto de escucha
BACKLOG = 5          # Cola de conexiones pendientes
BUFFER_SIZE = 1024   # Tamaño máximo de mensaje

# Estructuras de datos globales
clients = []         # Lista de sockets: incluye socket de escucha + clientes
nicknames = {}       # Diccionario socket -> nick del cliente


def broadcast_message(message: bytes, exclude_sock=None):
    """
    Envía `message` a todos los clientes conectados, excepto `exclude_sock`.
    """
    for sock in list(clients):
        # No reenvía al socket excluido ni al socket de escucha
        if sock is exclude_sock or sock is listen_sock:
            continue
        try:
            sock.sendall(message)
        except Exception:
            # Si falla el envío, desconectar al cliente problemático
            disconnect_client(sock)


def disconnect_client(sock: socket.socket):
    """
    Cierra la conexión del cliente, lo elimina de las estructuras y notifica al resto.
    """
    nick = nicknames.get(sock)
    if nick:
        # Notificar al resto que este cliente se desconectó
        msg = f"* {nick} se ha desconectado\n".encode()
        broadcast_message(msg, exclude_sock=sock)
        del nicknames[sock]

    if sock in clients:
        clients.remove(sock)
    try:
        sock.close()
    except Exception:
        pass


def handle_shutdown(signum, frame):
    """
    Manejador de SIGINT (Ctrl-C): notifica a todos y cierra el servidor.
    """
    msg = b"* SERVIDOR detenido, bye\n"
    for sock in list(clients):
        if sock is not listen_sock:
            try:
                sock.sendall(msg)
                sock.close()
            except Exception:
                pass
    listen_sock.close()
    sys.exit(0)


def main():
    """
    Función principal: inicializa el servidor y entra en el bucle de select.
    """
    global listen_sock

    # Instalar manejador de señal para parada limpia
    signal.signal(signal.SIGINT, handle_shutdown)

    # 1. Crear socket de escucha
    listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_sock.bind((HOST, PORT))
    listen_sock.listen(BACKLOG)
    print(f"[+] Servidor escuchando en {HOST}:{PORT}")

    # Añadir socket de escucha a la lista de clientes monitoreados
    clients.append(listen_sock)

    # 2. Bucle principal con select para manejar múltiples conexiones
    while True:
        # Espera hasta que haya datos o nuevas conexiones
        read_ready, _, _ = select.select(clients, [], [])

        for sock in read_ready:
            if sock is listen_sock:
                # Nueva conexión entrante
                conn, addr = listen_sock.accept()
                print(f"[+] Conexión desde {addr}")

                # Leer el nick enviado por el cliente
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    conn.close()
                    continue
                nick = data.decode().strip()

                # Comprobar que el nick no esté en uso
                if nick in nicknames.values():
                    conn.sendall(b"ERROR: nick en uso\n")
                    conn.close()
                    continue

                # Aceptar el cliente: confirmar y registrar
                conn.sendall(b"OK\n")
                clients.append(conn)
                nicknames[conn] = nick

                # Notificar a los demás clientes
                welcome_msg = f"* {nick} se ha conectado\n".encode()
                broadcast_message(welcome_msg, exclude_sock=conn)

            else:
                # Datos de un cliente ya conectado
                try:
                    data = sock.recv(BUFFER_SIZE)
                except Exception:
                    # Error de recv: desconectar
                    disconnect_client(sock)
                    continue

                if not data:
                    # Conexión cerrada por el cliente
                    disconnect_client(sock)
                    continue

                # Construir mensaje con el nick y reenviar
                nick = nicknames.get(sock, "?")
                text = data.decode()
                full_msg = f"{nick}: {text}".encode()
                broadcast_message(full_msg)


if __name__ == '__main__':
    main()
