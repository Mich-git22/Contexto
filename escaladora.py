from equipos import Equipos

class Escaladora(Equipos):
    def __init__(self, id_equipo, descripcion, estado, nivel_dificultad):
        super().__init__(id_equipo, descripcion, estado)
        self.nivel_dificultad = nivel_dificultad

    def ajustar_dificultad(self, nuevo_nivel):
        self.nivel_dificultad = nuevo_nivel
        print(f"🚶 Dificultad ajustada a nivel {self.nivel_dificultad}.")
