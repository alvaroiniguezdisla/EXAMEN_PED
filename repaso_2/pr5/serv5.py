#!/usr/bin/env python3
import socket
import sys
from datetime import datetime
import prctl

def main():
    prctl.set_name("serv5")

    PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5005

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))

    print(f"🟢 Servidor escuchando en UDP puerto {PORT}")

    try:
        while True:
            data, client_addr = server_socket.recvfrom(1024)
            mensaje = data.decode().strip()
            print(f"🔌 Petición recibida de {client_addr}: {mensaje}")

            if mensaje == "TIME?":
                fecha_hora = str(datetime.now())
                server_socket.sendto(fecha_hora.encode(), client_addr)
                print(f"✅ Enviado: {fecha_hora}")
            else:
                error_msg = "❌ ERROR: Petición no válida"
                server_socket.sendto(error_msg.encode(), client_addr)
                print(f"❌ Petición inválida. Enviado error a {client_addr}")

    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido manualmente con Ctrl+C")

    except Exception as e:
        print(f"⚠️ Error en el servidor: {e}")

    finally:
        server_socket.close()
        print("🔒 Socket cerrado")

if __name__ == "__main__":
    main()
