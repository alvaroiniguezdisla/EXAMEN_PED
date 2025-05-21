#!/usr/bin/env python3
import os
import sys
import time
import prctl  # asegúrate de tener instalado python-prctl: pip install python-prctl

def main():
    prctl.set_name("serv3")  # cambia el nombre del proceso a "serv3"

    FIFO_CLIENTE = "/tmp/fifo_cliente_g5"
    FIFO_SERVIDOR = "/tmp/fifo_servidor_g5"

    # Eliminar FIFOs si ya existen para evitar errores
    for fifo in [FIFO_CLIENTE, FIFO_SERVIDOR]:
        if os.path.exists(fifo):
            os.remove(fifo)

    # Crear las FIFOs
    try:
        os.mkfifo(FIFO_CLIENTE)
        os.mkfifo(FIFO_SERVIDOR)
    except OSError as e:
        print(f"[Servidor] Error al crear las FIFOs: {e}")
        sys.exit(1)

    print("[Servidor] Esperando petición...")

    # Leer petición del cliente
    try:
        with open(FIFO_CLIENTE, "r") as fifo_lectura:
            peticion = fifo_lectura.readline().strip()
            print(f"[Servidor] Petición recibida: {peticion}")
    except Exception as e:
        print(f"[Servidor] Error al leer la petición: {e}")
        sys.exit(1)

    # Generar respuesta
    if peticion == "fecha":
        respuesta = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    else:
        respuesta = "ERROR: Comando no reconocido"

    # Enviar respuesta al cliente
    try:
        with open(FIFO_SERVIDOR, "w") as fifo_escritura:
            fifo_escritura.write(respuesta + "\n")
            print("[Servidor] Respuesta enviada")
    except Exception as e:
        print(f"[Servidor] Error al escribir la respuesta: {e}")
        sys.exit(1)

    # Limpiar
    os.remove(FIFO_CLIENTE)
    os.remove(FIFO_SERVIDOR)

if __name__ == "__main__":
    main()
