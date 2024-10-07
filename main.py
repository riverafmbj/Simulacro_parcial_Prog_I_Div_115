from funciones import *
from validaciones import *

inventario = [
  ["Laptop", 1500.00, 10],
  ["Silla", 200.00, 50],
  ["Libro", 15.00, 100],
  ["Monitor", 300.00, 30]
]

respuesta = "no"
while respuesta == "no":
  match menu():
    case "1":

      inventario.append(agregar_producto())
      continuar = input("¿Desea agregar otro producto?: ")
      while continuar == "si":
        inventario.append(agregar_producto())
        continuar = input("¿Desea agregar otro producto?: ")
      
    case "2":
        if inventario == []:
          print("No hay productos en el inventario.")
        else:
          producto_a_buscar = input("Ingrese el nombre del producto a buscar: ").lower()
          buscar_producto(inventario, producto_a_buscar)

    case "3":
      if inventario == []:
        print("No hay productos en el inventario.")
      else:
        ordenar_precio_ascendente(inventario)
        for producto in inventario:
          for _ in producto:
            nombre = producto[0]
            precio = producto[1]
            cantidad = producto[2]
          print(f"{nombre} - Precio: ${precio} - Cantidad: {cantidad}")

    case "4":
      if inventario == []:
        print("No hay productos en el inventario.")
      else:
        nombre_mas_caro, precio_mas_caro = buscar_producto_mas_caro(inventario)
        print(f"Nombre del producto mas caro: {nombre_mas_caro} - Precio: ${precio_mas_caro}")
        nombre_mas_barato, precio_mas_barato = buscar_producto_mas_barato(inventario)
        print(f"Nombre del producto mas barato: {nombre_mas_barato} - Precio: ${precio_mas_barato}")


    case "5":
      if inventario == []:
        print("No hay productos en el inventario.")
      else:
        flag_mayor_quincemil = False
        buscar_mayor_quincemil(inventario, flag_mayor_quincemil)

    case "6":
      respuesta = input("¿Está seguro que desea salir? (si/no): ")
      while respuesta != "no" and respuesta != "si":
        respuesta = input("Error. Ingrese 'si' o 'no' : ")

    case _:
      print("Error. Ingrese una opción correcta. (De 1 a 6)")