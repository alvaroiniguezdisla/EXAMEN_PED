class Partida:

    def empezar_partida(self):
        self.rondas = []
        self.contador = 0

    def comprobar_rondas(self, rondas):
        if len(rondas) == 10:
            self.rondas = rondas
            return 10
        elif len(rondas) == 11 and rondas[9][0] != 10 and rondas[9][0] + rondas[9][1] == 10:
            self.rondas = rondas
            return 10
        elif len(rondas) == 12 and rondas[9][0] == 10:
            self.rondas = rondas
            return 10
        else:
            raise ValueError("Número de rondas inválido para una partida.")

    def calcular_puntuacion_partida_simple(self):
        total_puntos = 0
        for ronda in self.rondas:
            total_puntos += ronda[0] + ronda[1]
        return total_puntos

    def calcular_puntuacion_partida_con_strike(self):
        total_puntos = 0
        for i in range(len(self.rondas)):
            ronda = self.rondas[i]
            if ronda[0] == 10 and ronda[1] == 0:
                if i + 1 < len(self.rondas):
                    ronda_siguiente = self.rondas[i + 1]
                    total_puntos += 10 + ronda_siguiente[0] + ronda_siguiente[1]
                else:
                    total_puntos += 10
            else:
                total_puntos += ronda[0] + ronda[1]
        return total_puntos

    def calcular_puntuacion_partida_con_spare(self):
        total_puntos = 0
        for i in range(len(self.rondas)):
            ronda = self.rondas[i]
            if ronda[0] + ronda[1] == 10 and ronda[0] != 10 and ronda[1] != 10:
                if i + 1 < len(self.rondas):
                    siguiente_ronda = self.rondas[i + 1]
                    total_puntos += ronda[0] + ronda[1] + siguiente_ronda[0]
                else:
                    total_puntos += ronda[0] + ronda[1]
            else:
                total_puntos += ronda[0] + ronda[1]
        return total_puntos

    def calcular_puntuacion_partida_cualquiera(self):
        total_puntos = 0
        for i in range(len(self.rondas)):
            ronda = self.rondas[i]
            # Filtramos por spares
            if ronda[0] + ronda[1] == 10 and ronda[0] != 10 and ronda[1] != 10:
                if i + 1 < len(self.rondas):
                    siguiente_ronda = self.rondas[i + 1]
                    total_puntos += ronda[0] + ronda[1] + siguiente_ronda[0]
                else:
                    total_puntos += ronda[0] + ronda[1]
            # Filtramos por strike
            elif ronda[0] == 10 and ronda[1] == 0:
                if i + 1 < len(self.rondas):
                    ronda_siguiente = self.rondas[i + 1]
                    total_puntos += 10 + ronda_siguiente[0] + ronda_siguiente[1]
                else:
                    total_puntos += 10
            # Ronda normal
            else:
                total_puntos += ronda[0] + ronda[1]
        return total_puntos

    def sumar_puntos_extra(self):
        # Spare en la ronda 10 (ronda[9]) → 1 tiro extra (ronda[10])
        if len(self.rondas) > 10 and self.rondas[9][0] != 10 and self.rondas[9][0] + self.rondas[9][1] == 10:
            self.contador += self.rondas[10][0]
        # Strike en la ronda 10 (ronda[9]) → 2 tiros extra (rondas[10] y [11])
        elif len(self.rondas) > 11 and self.rondas[9][0] == 10:
            self.contador += self.rondas[10][0] + self.rondas[11][0]

    def calcular_puntuacion_partida_cualquiera_tiros_extra(self):
        self.contador = 0  # Reiniciamos el contador

        # Solo procesamos las 10 primeras rondas
        for i in range(10):
            ronda = self.rondas[i]

            # Filtramos por spares
            if ronda[0] + ronda[1] == 10 and ronda[0] != 10 and ronda[1] != 10:
                if i + 1 < len(self.rondas):
                    siguiente_ronda = self.rondas[i + 1]
                    self.contador += ronda[0] + ronda[1] + siguiente_ronda[0]
                else:
                    self.contador += ronda[0] + ronda[1]

            # Filtramos por strike
            elif ronda[0] == 10 and ronda[1] == 0:
                if i + 1 < len(self.rondas):
                    ronda_siguiente = self.rondas[i + 1]
                    self.contador += 10 + ronda_siguiente[0] + ronda_siguiente[1]
                else:
                    self.contador += 10

            # Ronda normal
            else:
                self.contador += ronda[0] + ronda[1]

        # Agregamos puntos extra si hay
        self.sumar_puntos_extra()

        return self.contador
    
