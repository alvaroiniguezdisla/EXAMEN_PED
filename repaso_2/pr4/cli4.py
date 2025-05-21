#!/usr/bin/env python3
import os
import socket
import sys
import prctl

def main():
    prctl.set_name("cli4")

    SOCKET_PATH = sys.argv[1] if len(sys.argv) > 1 else "/tmp/socket_grupo5"

    client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    client_socket.connect(SOCKET_PATH)

    try:
        fichero = input("📄 Introduce la ruta del fichero: ").strip()
        client_socket.sendall(fichero.encode())

        buffer = bytearray()
        while True:
            bloque = client_socket.recv(1024)
            if not bloque:
                break
            buffer.extend(bloque)

        texto = buffer.decode()

        if texto.startswith("ERROR"):
            print(f"⚠️  Error recibido del servidor:\n{texto}")
        else:
            print(f"\n📜 Contenido del fichero:\n{texto}")

    except Exception as e:
        print(f"Error en la comunicación: {e}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
