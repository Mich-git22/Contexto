from equipos import Equipos

class AparatosParaPierna(Equipos):
    def __init__(self, id_equipo, descripcion, estado, peso_de_la_barra, carga_maxima_kg):
        super().__init__(id_equipo, descripcion, estado)
        self.peso_de_la_barra = peso_de_la_barra
        self.carga_maxima_kg = carga_maxima_kg
        self.carga_maxima_lb = carga_maxima_kg * 2.20462

    def ajustar_carga(self, nueva_carga_kg):
        if nueva_carga_kg <= self.carga_maxima_kg:
            print(f"🦵 Carga ajustada a {nueva_carga_kg} kg.")
        else:
            print("⚠️ La carga excede el máximo permitido.")
