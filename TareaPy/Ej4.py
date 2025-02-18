def calcularTiempoDistancia():
    marca = input("Introduce la marca del vehículo: ")
    consumo = float(input("Introduce el consumo de combustible a los 100 km: "))
    litros_repostados = float(input("Introduce los litros de combustible que tienes: "))
    velocidad = float(input("Introduce la velocidad a la que circulas (km/h): "))
    km_recorridos = (litros_repostados / consumo) * 100
    tiempo = (km_recorridos / velocidad) * 60
    print(f"\nEl vehículo marca {marca} que consume {consumo} litros a los 100km\n"
          f"Circulando a {velocidad} km/h con {litros_repostados} litros\n"
          f"Me permite circular durante {tiempo:.2f} minutos una distancia de {km_recorridos:.2f} km")

calcularTiempoDistancia()
