class Equipos:
    def __init__(self, id_equipo, descripcion, estado):
        self.id_equipo = id_equipo
        self.descripcion = descripcion
        self.estado = estado

    def usar(self):
        if self.estado.lower() == "disponible":
            print(f"✅ Usando el equipo '{self.descripcion}'.")
            self.estado = "En uso"
        else:
            print(f"⚠️ El equipo '{self.descripcion}' no está disponible.")

    def mantenimiento(self):
        print(f"🔧 El equipo '{self.descripcion}' está en mantenimiento.")
        self.estado = "En mantenimiento"
