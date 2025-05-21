#!/usr/bin/env python3
import os
import sys
import prctl  # asegúrate de tener instalado python-prctl: pip install python-prctl

def main():
    prctl.set_name("cli3")  # cambia el nombre del proceso a "cli3"

    FIFO_CLIENTE = "/tmp/fifo_cliente_g5"
    FIFO_SERVIDOR = "/tmp/fifo_servidor_g5"

    # Verificar que el servidor ya haya creado las FIFOs
    if not os.path.exists(FIFO_CLIENTE) or not os.path.exists(FIFO_SERVIDOR):
        print("[Cliente] Las FIFOs no existen. Ejecuta primero el servidor.")
        sys.exit(1)

    # Escribir petición al servidor
    try:
        with open(FIFO_CLIENTE, "w") as fifo_escritura:
            fifo_escritura.write("fecha\n")
            print("[Cliente] Petición enviada")
    except Exception as e:
        print(f"[Cliente] Error al escribir la petición: {e}")
        sys.exit(1)

    # Leer respuesta del servidor
    try:
        with open(FIFO_SERVIDOR, "r") as fifo_lectura:
            respuesta = fifo_lectura.readline().strip()
            print(f"[Cliente] Respuesta del servidor: {respuesta}")
    except Exception as e:
        print(f"[Cliente] Error al leer la respuesta: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
