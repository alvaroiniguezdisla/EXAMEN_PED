from datetime import datetime

class Mensajes:
    @staticmethod
    def procesar_mensaje(mensaje):
        if mensaje.upper() == "FECHA":
            return datetime.now().strftime("%Y-%m-%d")
        elif mensaje.upper() == "HORA":
            return datetime.now().strftime("%H:%M")

        else:
            return "ERROR"
