import unittest
from bolos import Partida

class TestBolos(unittest.TestCase):


    def test_crear_partida_y_comprobar_rondas(self):
        partida=Partida()
        partida.empezar_partida()
        rondas = [(2, 4), (3, 5), (1, 6), (0, 9), (4, 4), (2, 7), (5, 2), (6, 1), (7, 2), (8, 1)]
        self.assertEqual(partida.comprobar_rondas(rondas),10)

    def test_calcular_puntuacion_partida_simple(self):
        partida=Partida()
        partida.empezar_partida()
        rondas = [(2, 4), (3, 5), (1, 6), (0, 9), (4, 4), (2, 7), (5, 2), (6, 1), (7, 2), (8, 1)]
        partida.comprobar_rondas(rondas)


        
        cont =0

        for ronda in rondas:
            cont =cont  +ronda[0]+ ronda[1]
        

        self.assertEqual(partida.calcular_puntuacion_partida_simple(),cont)


    def test_carcular_puntuacion_partida_con_strike(self):
        partida=Partida()
        partida.empezar_partida()
        rondas = [(10, 0), (1, 1), (1, 1), (10, 0), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (2, 1)]
        partida.comprobar_rondas(rondas)

        self.assertEqual(partida.calcular_puntuacion_partida_con_strike(),41)

    def test_calcular_puntuacion_partida_con_spare(self):
        partida=Partida()
        partida.empezar_partida()
        rondas = [(5, 5), (1, 1), (1, 1), (5, 5), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (2, 1)]
        partida.comprobar_rondas(rondas)

        self.assertEqual(partida.calcular_puntuacion_partida_con_spare(),39)

    def test_calcular_puntuacion_partida_cualquiera(self):
        partida=Partida()
        partida.empezar_partida()
        rondas = [(5, 5), (1, 1), (1, 1), (5, 5), (1, 1), (1, 1), (1, 1), (1, 1), (10, 0), (2, 1)]
        partida.comprobar_rondas(rondas)

        self.assertEqual(partida.calcular_puntuacion_partida_cualquiera(),50)
        

    def test_calcular_puntuacion_partida_cualquiera_un_tiro_extra(self):
        partida=Partida()
        partida.empezar_partida()
        rondas = [(5, 5), (1, 1), (1, 1), (5, 5), (1, 1), (1, 1), (1, 1), (1, 1), (10, 0), (6,4)]
        rondas.append((2, 0))
        partida.comprobar_rondas(rondas)
        
        self.assertEqual(partida.calcular_puntuacion_partida_cualquiera_tiros_extra(),68)

    def test_calcular_puntuacion_partida_cualquiera_dos_tiros_extra(self):
        partida=Partida()
        partida.empezar_partida()
        rondas = [(5, 5), (1, 1), (1, 1), (5, 5), (1, 1), (1, 1), (1, 1), (1, 1), (10, 0), (10,0)]
        #añadimos 2 tiros=2 rondas mas con solo la primera bola
        rondas.append((2, 0))
        rondas.append((2, 0))
        partida.comprobar_rondas(rondas)
        self.assertEqual(partida.calcular_puntuacion_partida_cualquiera_tiros_extra(),70)





if __name__ == '__main__' :
    unittest.main()



