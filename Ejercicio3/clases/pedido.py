from clases.item import Item

class Pedido:
    def __init__(self):
        self.items = []


    def agregar_item(self,nombre,precio,cantidad):
        item= Item(nombre,precio,cantidad)
        self.items.append(item)
        print(f"Item'{nombre}' agregado correctamente")

    def mostrar_items(self):
        if not self.items:
            print("Elpedido no tiene items.")      
            return
        print ("Detalle  Pedido")  
        for i, item in enumerate(self.items,start=1):
            print(f"{1}.)",end="")
            item.mostrar()

    def total (self):
        return sum(item.sub_total() for item in self.items)

    def mostrar_total(self):
        print(f"TOTAL A PAGAR: ${self.total():.2f}")

