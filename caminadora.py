from equipos import Equipos

class Caminadora(Equipos):
    def __init__(self, id_equipo, descripcion, estado, velocidad_maxima, inclinacion):
        super().__init__(id_equipo, descripcion, estado)
        self.velocidad_maxima = velocidad_maxima
        self.inclinacion = inclinacion

    def ajustar_velocidad(self, nueva_velocidad):
        if nueva_velocidad <= self.velocidad_maxima:
            print(f"🏃 Velocidad ajustada a {nueva_velocidad} km/h.")
        else:
            print("⚠️ La velocidad excede el máximo permitido.")

    def ajustar_inclinacion(self, nueva_inclinacion):
        print(f"⛰️ Inclinación ajustada a {nueva_inclinacion} grados.")
