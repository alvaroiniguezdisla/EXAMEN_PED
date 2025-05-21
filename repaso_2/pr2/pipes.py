import os
import sys
import prctl

def main():
    # Pipe cliente -> servidor
    r1, w1 = os.pipe()
    # Pipe servidor -> cliente
    r2, w2 = os.pipe()

    pid = os.fork()

    if pid:
        # Proceso padre - Cliente
        prctl.set_name("cli2")

        os.close(r1)  # No lee del pipe cliente->servidor
        os.close(w2)  # No escribe al pipe servidor->cliente

        try:
            w1 = os.fdopen(w1, 'w')
            path = input("Introduce la ruta: ")
            w1.write(path + '\n')
            w1.flush()
            w1.close()
        except Exception as e:
            print(f"[Cliente] Error al enviar la ruta: {e}")
            sys.exit(1)

        try:
            r2 = os.fdopen(r2, 'r')
            contenido = r2.read()
            print(f"El contenido del archivo es el siguiente:\n{contenido}")
            r2.close()
        except Exception as e:
            print(f"[Cliente] Error al leer el contenido: {e}")
            sys.exit(1)

        os.wait()

    else:
        # Proceso hijo - Servidor
        prctl.set_name("serv2")

        os.close(w1)  # No escribe al pipe cliente->servidor
        os.close(r2)  # No lee del pipe servidor->cliente

        try:
            r1 = os.fdopen(r1, 'r')
            path = r1.readline().strip()
            r1.close()
            print(f"[Servidor] El cliente ha pedido lo siguiente: {path}")
        except Exception as e:
            print(f"[Servidor] Error leyendo la ruta: {e}")
            sys.exit(1)

        try:
            with open(path, 'r') as fd:
                contenido = fd.read()
        except Exception as e:
            contenido = f"[Servidor] Error al abrir el fichero: {e}"

        try:
            w2 = os.fdopen(w2, 'w')
            w2.write(contenido + '\n')
            w2.flush()
            w2.close()
        except Exception as e:
            print(f"[Servidor] Error enviando el contenido: {e}")
            sys.exit(1)

        sys.exit(0)

if __name__ == "__main__":
    main()
