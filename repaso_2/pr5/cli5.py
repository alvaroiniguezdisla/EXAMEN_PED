import os
import sys
import socket
import prctl

def main():
    prctl.set_name("cli5")

    HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 5005

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(5)

    try:
        client_socket.sendto(b"TIME?", (HOST, PORT))

        data, _ = client_socket.recvfrom(1024)
        texto = data.decode()

        print(f"📅 Fecha y hora del servidor: {texto}")

    except Exception as e:
        print(f"Error en el cliente: {e}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()