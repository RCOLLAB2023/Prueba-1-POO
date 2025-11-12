from clases.libro import Libro

class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def agregar_libro(self,libro):
        self.catalogo.append(libro)  
        print(f"Se agrego el libro: {libro.titulo} de {libro.autor} al catalogo.")

    def mostrar_catalogo(self):
        print("CATALOGO BIBLIOTECA")
        if not self.catalogo:
            print("No existen Libros registrados.")      
        for libro in self.catalogo:
            libro.mostrar_info()

    def prestar_libro(self, titulo):
        for libro in self.catalogo:
            if libro.titulo.lower() == titulo.lower():
               libro.devolver()
               return
        print(f"El titulo '{titulo}' ingresado no se encuentra en catalogo")     
