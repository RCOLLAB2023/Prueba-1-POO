class Contacto:
    def __init__(self,nombre,telefono,correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

class Agenda:
    def __init__(self):
        self.contacto = []

    def agregar_contacto(self,nombre,telefono,correo):
            if self.buscar_contacto(nombre):
                print(f"Contacto '{nombre}' Existente") 
            else:
                nuevo = Contacto(nombre,telefono,correo)
                self.contacto.append(nuevo)
                print(f"Contaco '{nombre}' agragdo corrrectamente") 

    def buscar_contacto(self,nombre):
            for c in self.contacto:
                if c.nombre.lower()== nombre.lower():
                    return c
                return None
            
    def eliminar_contacto(self,nombre):
            contacto = self.buscar_contacto(nombre)
            if contacto:
                self.contacto.remove(contacto)
                print(f"No se encontro el contacto'{nombre}'en el directorio")    
    def mostrar_contactos(self):
            if not self.contacto:
                print("No hay contactos en Agenda")
            else:
                print("Lista de contactos:")    
                for c in self.contacto:
                    print(f"{c.nombre}, {c.telefono},{c.correo}")