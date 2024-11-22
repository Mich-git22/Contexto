class Gimnasio:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.equipos = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)
        print(f"Equipo '{equipo.descripcion}' agregado al gimnasio.")

    def mostrar_informacion(self):
        print(f"🏋️ Gimnasio: {self.nombre}\n📍 Dirección: {self.direccion}")
        print("\nEquipos disponibles:")
        for equipo in self.equipos:
            print(f"- {equipo.descripcion} ({equipo.estado})")
