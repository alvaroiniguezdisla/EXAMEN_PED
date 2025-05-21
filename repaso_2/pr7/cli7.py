#!/usr/bin/env python3
"""
cli7.py - Cliente de chat simple usando select()
Uso: python3 cli7.py <host> <puerto>
"""
import socket
import select
import sys

BUFFER_SIZE = 1024  # Tamaño máximo de mensaje


def main():
    """
    Función principal: conecta al servidor, autentica nick y entra en bucle de envío/recepción.
    """
    # Comprobar argumentos
    if len(sys.argv) != 3:
        print(f"Uso: {sys.argv[0]} <host> <puerto>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])

    # 1. Crear socket TCP y conectar
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
    except Exception as e:
        print(f"Error al conectar al servidor: {e}")
        sys.exit(1)

    # 2. Pedir y enviar nick al servidor
    nick = input("Introduce tu nick: ").strip()
    if not nick:
        print("El nick no puede estar vacío.")
        sock.close()
        sys.exit(1)
    sock.sendall((nick + "\n").encode())

    # 3. Leer respuesta del servidor
    response = sock.recv(BUFFER_SIZE).decode()
    if response.startswith("ERROR"):
        print(response.strip())
        sock.close()
        sys.exit(1)
    print(response.strip())  # "OK"

    print("--- Conectado. Escribe mensajes o /quit para salir. ---")

    # 4. Bucle de E/S con select sobre socket y stdin
    while True:
        # select en lista de fds: stdin (fd 0) y socket
        read_ready, _, _ = select.select([sys.stdin, sock], [], [])

        for fd in read_ready:
            if fd is sock:
                # Datos entrantes del servidor
                data = sock.recv(BUFFER_SIZE)
                if not data:
                    # Servidor cerrado
                    print("* Conexión al servidor perdida.")
                    sock.close()
                    sys.exit(0)
                # Mostrar mensaje
                print(data.decode(), end='')

            else:
                # Entrada del usuario por teclado
                line = sys.stdin.readline()
                if not line:
                    # EOF (Ctrl-D)
                    print("* Desconectando...")
                    sock.close()
                    sys.exit(0)
                line = line.rstrip("\n")
                if line == "/quit":
                    # Comando de salida
                    print("* Saliendo...")
                    sock.close()
                    sys.exit(0)
                # Enviar mensaje al servidor
                sock.sendall((line + "\n").encode())


if __name__ == '__main__':
    main()
