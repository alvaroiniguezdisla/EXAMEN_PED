import socket

# Configuración del servidor
HOST = input("Introduce la dirección del servidor (por defecto localhost): ") or "127.0.0.1"
PUERTO = 16052  # Cambia según tu grupo (16000 + 10 * grupo + posición)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect((HOST, PUERTO))
        print(f"Conectado a {HOST}:{PUERTO}")
        for _ in range(3):
            mensaje = input("Introduce el mensaje a enviar (FECHA, HORA, otro): ")
            cliente.sendall(mensaje.encode('utf-8'))
            respuesta = cliente.recv(1024).decode('utf-8')
            print(f"Respuesta del servidor: {respuesta}")

if __name__ == "__main__":
    main()
