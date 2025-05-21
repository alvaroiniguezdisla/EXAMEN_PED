#!/usr/bin/env python3
import os
import socket
import sys
import prctl

def main():
    prctl.set_name("serv4")

    SOCKET_PATH = sys.argv[1] if len(sys.argv) > 1 else "/tmp/socket_grupo5"

    if os.path.exists(SOCKET_PATH):
        os.unlink(SOCKET_PATH)

    server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server_socket.bind(SOCKET_PATH)
    server_socket.listen()

    print(f"🟢 Servidor escuchando en {SOCKET_PATH}")

    try:
        while True:
            cliente_socket, _ = server_socket.accept()
            with cliente_socket:
                peticion = cliente_socket.recv(1024).decode().strip()

                if os.path.isfile(peticion):
                    with open(peticion, 'r') as f:
                        contenido = f.read()
                    cliente_socket.sendall(contenido.encode())
                else:
                    error = "ERROR: Fichero no encontrado."
                    cliente_socket.sendall(error.encode())

    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido (Ctrl+C)")

    finally:
        server_socket.close()
        os.unlink(SOCKET_PATH)
        print("🔒 Socket cerrado y eliminado")

if __name__ == "__main__":
    main()


