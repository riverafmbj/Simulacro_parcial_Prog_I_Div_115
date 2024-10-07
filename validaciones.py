def validar_entero(entero:str) -> int:
  """
  Valida que el entero sea un digito

  Args:
      entero(str): el entero a validar
  
  Returns:
      entero(int): devuelve el entero validado
  """   
  while not entero.isdigit() or int(entero) <= 0:
      entero = input(f"Error. Ingrese el dato correctamente: ")
  return int(entero)

def validar_flotante(flotante:str) -> int:
  """
  Valida que el flotante sea un digito

  Args:
      flotante(str): el flotante a validar
  
  Returns:
      flotante(float): devuelve el flotante validado
  """   
  while not flotante.isdigit() or float(flotante) <= 0:
      flotante = input(f"Error. Ingrese el dato correctamente: ")
  return float(flotante)