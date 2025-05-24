import unittest
from mensajes import Mensajes
from datetime import datetime

class TestMensajes(unittest.TestCase):
    def test_respuesta_fecha(self):
        resultado = Mensajes.procesar_mensaje("FECHA")
        esperado = datetime.now().strftime("%Y-%m-%d")
        self.assertEqual(resultado, esperado)
    
    def test_respuesta_hora(self):
        resultado = Mensajes.procesar_mensaje("HORA")
        esperado = datetime.now().strftime("%H:%M:%S")
        self.assertEqual(resultado[:5], esperado[:5])  # Comparamos solo HH:MM para tolerar diferencia de segundos

    def test_respuesta_error(self):
        resultado = Mensajes.procesar_mensaje("Hola")
        self.assertEqual(resultado, "ERROR")
    
    def test_respuesta_error_minusculas(self):
        resultado = Mensajes.procesar_mensaje("fecha")
        self.assertEqual(resultado, datetime.now().strftime("%Y-%m-%d"))

    

    def test_respuesta_error_mayusculas(self):
        resultado = Mensajes.procesar_mensaje("hora")
        self.assertEqual(resultado, datetime.now().strftime("%H:%M"))
   

    def test_respuesta_mensaje_vacio(self):
        resultado = Mensajes.procesar_mensaje("")
        self.assertEqual(resultado, "ERROR")
    
    def test_respuesta_mensaje_numerico(self):
        resultado = Mensajes.procesar_mensaje("123")
        self.assertEqual(resultado, "ERROR")

if __name__ == '__main__':
    unittest.main()
