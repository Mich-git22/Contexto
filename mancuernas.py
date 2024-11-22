from equipos import Equipos

class Mancuernas(Equipos):
    def __init__(self, id_equipo, descripcion, estado, peso_kg):
        super().__init__(id_equipo, descripcion, estado)
        self.peso_kg = peso_kg
        self.peso_lb = peso_kg * 2.20462

    def ajustar_peso(self, nuevo_peso_kg):
        self.peso_kg = nuevo_peso_kg
        self.peso_lb = nuevo_peso_kg * 2.20462
        print(f"🔩 Mancuerna ajustada a {self.peso_kg} kg ({self.peso_lb:.2f} lb).")
