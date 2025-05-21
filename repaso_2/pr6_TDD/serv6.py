#!/usr/bin/env python3
import sys
import socket
import prctl

def main():
    prctl.set_name("serv6")

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5006

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen()

    print(f"🟢 Servidor TCP escuchando en puerto {port}")

    try:
        while True:
            client_socket, client_addr = server_socket.accept()
            with client_socket:
                print(f"🔌 Conexión recibida de {client_addr}")

                peticion = client_socket.recv(1024)
                path = peticion.decode().strip()

                try:
                    with open(path, 'r') as f:
                        contenido = f.read()
                    client_socket.sendall(contenido.encode())
                    print(f"✅ Enviado contenido del fichero: {path}")
                except Exception:
                    error = "ERROR: Fichero no encontrado o inaccesible."
                    client_socket.sendall(error.encode())
                    print(f"⚠️ {error}")

    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido manualmente (Ctrl+C)")

    except Exception :
        print("Error en la conexion con el cliente")

    finally:
        server_socket.close()
        print("🔒 Socket cerrado")

if __name__ == "__main__":
    main()
