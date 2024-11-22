class Proveedor:
    def __init__(self, nombre, contacto, producto, marca, modelo):
        self.nombre = nombre
        self.contacto = contacto
        self.producto = producto
        self.marca = marca
        self.modelo = modelo

    def mostrar_productos(self):
        print(f"🔧 Proveedor: {self.nombre}")
        print(f"📦 Producto: {self.producto}, Marca: {self.marca}, Modelo: {self.modelo}")
        print(f"📞 Contacto: {self.contacto}")
