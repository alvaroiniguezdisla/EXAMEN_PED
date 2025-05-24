import socket
from mensajes import Mensajes

# Configuración del puerto N
PUERTO = 16052  # Cambiar según el grupo y posición (en tu caso)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind(('0.0.0.0', PUERTO))
        servidor.listen()
        print(f"Servidor escuchando en puerto {PUERTO}...")
        
        while True:
            conn, addr = servidor.accept()
            with conn:
                print(f"Conexión desde {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    mensaje = data.decode('utf-8').strip()
                    respuesta = Mensajes.procesar_mensaje(mensaje)
                    conn.sendall(respuesta.encode('utf-8'))

if __name__ == "__main__":
    main()
