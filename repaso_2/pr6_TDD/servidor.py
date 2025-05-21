# servidor.py

def leer_fichero(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except Exception:
        return "ERROR: Fichero no encontrado o inaccesible."
    

def validar_path(path):
    return bool(path) and not path.startswith("..")


def decodificar_mensaje(data):
    try:
        return data.decode("utf-8")
    except:
        return "ERROR_DECODIFICACION"
