class Item:
    def __init__ (self, nombre, precio , cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad


    def sub_total(self):
        return self.precio * self.cantidad

    def mostrar (self):
        print(f"{self.nombre}-${self.precio:.2f}* {self.cantidad}= ${self.sub_total():.2f}")    