class Sensor:
    def __init__(self,nombre):
        self.nombre = nombre
        self.medicion = []

    def agregar_medicion(self,valor):
        self.medicion.append(valor)

    def promedio(self):
        if not self.medicion:
            return 0 
        return sum(self.medicion) /len(self.medicion)

    def valor_maximo(self):
        if not self.medicion:
            return None
        return max (self.medicion)

    def valor_minimo(self):
        if not self.medicion: 
            return  min(self.medicion)    

    def resumen(self):
        print(f"SENSOR:{self.nombre}") 
        if not self.medicion:
            print("No hay mediciones registradas aun.") 
        else:
            print(f"Mediciones registradas:{self.medicion}")
            print(f"Promedio:{self.promedio():.2f}")   
            print(f"Maximo: {self.valor_maximo()}")      
            print(f"Minimo:{self.valor_minimo()}")