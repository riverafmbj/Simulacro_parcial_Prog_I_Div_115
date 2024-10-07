from validaciones import *

def menu()->str:
  """
  Imprime el menú en pantalla

  Returns:
      input: para seleccionar la opción que querramos
  """
  print(f"{'EMPIRE INVENTORY':^50}")
  print(f"{'Menú de opciones':^50}")
  print("1 - Cargar producto/s")
  print("2 - Buscar producto")
  print("3 - Ordenar inventario")
  print("4 - Mostrar producto mas caro y mas barato")
  print("5 - Mostrar productos con precio mayor a 15000")
  print("6 - Salir")

  return input("Ingrese opción: ")

def agregar_producto()->list:
  """
  Crea una lista con el nombre, precio y cantidad del producto

  Returns:
      (list): La lista con los datos del producto
  """
  nuevo_producto = []
  
  producto = input("Ingrese nombre del producto: ").capitalize()
  nuevo_producto.append(producto)
  
  precio = input("Ingrese el precio del producto: ")
  nuevo_producto.append(validar_flotante(precio))

  cantidad = input("Ingrese la cantidad: ")
  nuevo_producto.append(validar_entero(cantidad))

  return nuevo_producto

def buscar_producto(inventario, producto_a_buscar) -> None:
  """
  Busca e imprime por pantalla los datos de un producto si es que se encuentra en el invetario

  Args:
      inventario(list): la lista en la cual se busca el producto
      producto_a_buscar(str): el producto que queremos buscar
  Returns:
      None
  """ 
  disponible = False
  for producto in inventario:
    for _ in producto:
      nombre = producto[0]

      if producto_a_buscar == nombre.lower():
        disponible = True
        precio = producto[1]
        cantidad = producto[2]
      
  if disponible == True:
    print("---------------------------------------------------------------------------------------------")
    print(f"Nombre de producto: {producto_a_buscar} - Precio: ${precio:.2f} - Cantidad: {cantidad}")
    print("---------------------------------------------------------------------------------------------")
  else:
    print("---------------------------------------------------------------------------------------------")
    print("El producto no se encuentra en el inventario")
    print("---------------------------------------------------------------------------------------------")

def ordenar_precio_ascendente(inventario) -> None:
  """
  Ordena la lista por precio ascendente

  Args:
      inventario(list): la lista que queremos ordenar
  Returns:
      None
  """
  longitud = len(inventario)

  for i in range(longitud):
    for j in range(longitud - 1 - i):
      if inventario[j][1] > inventario[j+1][1]:
        aux = inventario[j+1]
        inventario[j+1] = inventario[j]
        inventario[j] = aux

def buscar_producto_mas_caro(inventario: list) -> tuple:
  """
  Busca y devuelve el producto mas caro de la lista de productos

  Args:
      inventario(list): la lista en la cual se busca el producto mas caro
  
  Returns:
      nombre_mas_caro(str): devuelve el nombre del producto mas caro
      producto_mas_caro(float): devuelve el producto mas caro de la lista
  """     
  producto_mas_caro = 0
  flag_producto_mas_caro = False

  for producto in inventario:
    for _ in producto:
      producto_actual = producto[1]

      if flag_producto_mas_caro == False or producto_actual > producto_mas_caro:
        producto_mas_caro = producto_actual
        nombre = producto[0]
        flag_producto_mas_caro = True
  
  return nombre, producto_mas_caro

def buscar_producto_mas_barato(inventario: list) -> tuple:
  """
  Busca y devuelve el producto mas barato de la lista de productos

  Args:
      inventario(list): la lista en la cual se busca el producto mas barato
  
  Returns:
      nombre_mas_caro(str): devuelve el nombre del producto mas barato
      producto_mas_barato(float): devuelve el producto mas barato de la lista
  """     
  producto_mas_barato = 0
  flag_producto_mas_barato = False

  for producto in inventario:
    for _ in producto:
      producto_actual = producto[1]

      if flag_producto_mas_barato == False or producto_actual < producto_mas_barato:
        producto_mas_barato = producto_actual
        nombre = producto[0]
        flag_producto_mas_barato = True
  
  return nombre, producto_mas_barato

def buscar_mayor_quincemil(inventario, flag):
  """
  Busca e imprime por pantalla los productos que valgan mas de $15000 si es que existen

  Args:
      inventario(list): la lista en la cual se busca el producto con precio mayor a $15000
      flag(bool): la bandera que indica si existen o no productos con precio mayor a $15000
  Returns:
      None:
  """       
  for producto in inventario:
    for _ in producto:
      nombre = producto[0]
      precio = producto[1]
      cantidad = producto[2]
    if precio > 15000:
      flag = True
      print(f"{nombre} - Precio: ${precio} - Cantidad: {cantidad}")

  if flag == False:
      print("No hay productos con precio mayor a $15000.00")  