from gimnasio import Gimnasio
from proveedor import Proveedor
from mancuernas import Mancuernas
from aparatos_para_pierna import AparatosParaPierna
from caminadora import Caminadora
from escaladora import Escaladora

# Crear gimnasio
gimnasio = Gimnasio("Fitness Center", "Av. Siempre Viva 123")

# Crear proveedor
proveedor = Proveedor("MICH", "771-558-98-96", "Pesas", "ProGym", "Modelo 2024")
proveedor.mostrar_productos()

# Crear equipos y agregarlos al gimnasio
mancuerna = Mancuernas(1, "Mancuernas ajustables", "Disponible", 10)
gimnasio.agregar_equipo(mancuerna)

smith = AparatosParaPierna(2, "Máquina Smith", "Disponible", 20, 150)
gimnasio.agregar_equipo(smith)

caminadora = Caminadora(3, "Caminadora Eléctrica", "Disponible", 20, 15)
gimnasio.agregar_equipo(caminadora)

escaladora = Escaladora(4, "Escaladora Avanzada", "Disponible", 3)
gimnasio.agregar_equipo(escaladora)

# Mostrar información del gimnasio
gimnasio.mostrar_informacion()

# Probar funcionalidades
mancuerna.ajustar_peso(15)
smith.ajustar_carga(100)
caminadora.ajustar_velocidad(12)
escaladora.ajustar_dificultad(5)
