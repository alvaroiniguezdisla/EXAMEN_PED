# test.py
import unittest
import servidor  

class TestServidor(unittest.TestCase):

    def test_leer_fichero_valido(self):
        with open("prueba.txt", "w") as f:
            f.write("Hola mundo")

        resultado = servidor.leer_fichero("prueba.txt")
        self.assertEqual(resultado, "Hola mundo")

    def test_leer_fichero_inexistente(self):
        resultado = servidor.leer_fichero("archivo_que_no_existe.txt")
        self.assertEqual(resultado, "ERROR: Fichero no encontrado o inaccesible.")

    def test_leer_fichero_vacio(self):
        with open("archivo_vacio.txt", "w") as f:
            pass  # no escribimos nada

        resultado = servidor.leer_fichero("archivo_vacio.txt")
        self.assertEqual(resultado, "")

    def test_leer_fichero_unicode(self):
        texto = "¡Hola! ¿Cómo estás? 😊 Привет мир"
        with open("unicode.txt", "w", encoding="utf-8") as f:
            f.write(texto)
        self.assertEqual(servidor.leer_fichero("unicode.txt"), texto)

    def test_validar_path_valido(self):
        self.assertTrue(servidor.validar_path("prueba.txt"))

    def test_validar_path_vacio(self):
        self.assertFalse(servidor.validar_path(""))

    def test_validar_path_peligroso(self):
        self.assertFalse(servidor.validar_path("../etc/passwd"))

    def test_decodificar_mensaje_correcto(self):
        self.assertEqual(servidor.decodificar_mensaje(b"hola"), "hola")

if __name__ == '__main__':
    unittest.main()
