#!/usr/bin/env python3
import sys
import socket
import prctl

def main():
    prctl.set_name("cli6")

    host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 5006

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))

        path = input("📄 Introduce la ruta completa del fichero: ").strip()
        client_socket.sendall(path.encode())

        buffer = bytearray()

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            buffer.extend(data)

        respuesta = buffer.decode()

        print("\n📜 Respuesta del servidor:")
        print(respuesta)

    except Exception :
        print("Error en el cliente: ")

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
