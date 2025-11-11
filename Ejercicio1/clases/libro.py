class Libro:
    def __init__ (self,titulo,autor,copias):
        self.titulo = titulo                
        self.autor = autor
        self.copias = copias 
    def prestar(self):
        if self.copias > 0:
            self.copias -=1
            print(f"El Libro'{self.titulo}'ha sido prestado.Copias disponibles:{self.copias}")
        else:
            print(f"No existen copias disponibles del Libro '{self.titulo}'.")    

    def devolver(self):
        self.copias += 1
        print(f" El Libro '{self.titulo}' ha sido devuelto. Stock disponible: {self.copias}")

    def mostrar_info(self):
        print(f"Titulo:{self.titulo} , Autor: {self.autor},Stock Copias Disponibles:{self.copias}")             