from clases.sensor import Sensor

def main():
    # Sensores
    sensor_temp = Sensor("Temperatura")
    sensor_hum = Sensor("Humedad")

    
    for valor in [28.5, 20.2, 22.6, 24.7]:
        sensor_temp.agregar_medicion(valor)

    for valor in [42, 59, 47, 51]:
        sensor_hum.agregar_medicion(valor)

    sensores = [sensor_temp, sensor_hum]

    while True:
        print( " MENÚ SENSOR ")
        print("1 Ver resumen de todos los sensores")
        print("2 Agregar nueva medición")
        print("3 Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for sensor in sensores:
                sensor.resumen()

        elif opcion == "2":
            print("Sensores disponibles:")
            for i, s in enumerate(sensores, start=1):
                print(f"{i}. {s.nombre}")
            try:
                eleccion = int(input("Seleccione el número del sensor: ")) - 1
                valor = float(input("Ingrese nueva medición: "))
                sensores[eleccion].agregar_medicion(valor)
                print(f"Medición {valor} agregada al sensor '{sensores[eleccion].nombre}'.")
            except (ValueError, IndexError):
                print("Opción o valor inválido. Intente nuevamente.")

        elif opcion == "3":
            print("Saliendo del sistema de sensores.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
