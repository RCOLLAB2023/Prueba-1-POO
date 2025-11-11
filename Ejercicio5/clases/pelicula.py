class Pelicula:
    def __init__(self, titulo, genero, anio):
        self.titulo=titulo
        self.genero = genero
        self.anio = anio

    def mostrar_info(self):
        print(f"{self.titulo}({self.anio}),Genero:{self.genero}")


class Catalogo:
    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self,pelicula):
        self.peliculas.append(pelicula)

    def mostrar_catalogo(self):
        if not self.peliculas:
            print("Catalogo Sin Peliculas disponibles") 
        else:
            print("CATALOGO DE PELICULAS")  
            for peli in self.peliculas:
                peli.mostrar_info()

    def buscar_por_titulo(self,titulo):
        for peli in self.peliculas:
            if peli.titulo.lower() == titulo.lower():
                print("Pelicula Encontrada:")
                peli.mostrar_info()
                return
        print("No se encuentran pelicula scon ese titulo")

    def filtrar_por_genero(self,genero):
        filtradas = [p for p in self.peliculas if p.genero.lower() == genero.lower()]
        if filtradas:
            print("Peliculas del genero'{genero}':")
            for peli in filtradas:
                peli.mostrar_info()
        else:
            print (f"El Genero {genero} que busca no tiene peliculas disponibles")        

