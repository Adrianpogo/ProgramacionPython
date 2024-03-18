def verListaRecursivaConTipoDatos(lista, nivel, tipo):
  """
  Función que imprime una lista de forma recursiva, 
  con sangrías para visualizar la estructura.

  Parámetros:
    lista: La lista que se desea imprimir.
    nivel: El nivel actual de la recursividad.
    tipo: El tipo de la lista (list, tuple, dict, set).
  """

  # Imprimir el tipo de la lista
  if tipo == list:
    print(f"{nivel}:->")
  elif tipo == tuple:
    print(f"{nivel}:_>")
  elif tipo == dict:
    print(f"{nivel}:>")
  elif tipo == set:
    print(f"{nivel}:=>")

  # Si la lista está vacía, no hay nada que hacer
  if not lista:
    return

  # Si el elemento actual es una lista, 
  # se llama a la función de forma recursiva para cada elemento
  if isinstance(lista[0], (list, tuple, dict, set)):
    for i, elemento in enumerate(lista):
      verListaRecursivaConTipoDatos(elemento, nivel + 1, type(elemento))
  else:
    # Si el elemento actual no es una lista, 
    # se imprime con la sangría correspondiente
    for i, elemento in enumerate(lista):
      print(f"{nivel + 1}:-> {elemento}")

# Ejemplo de uso
l = [1, 2, 3, (1, 2, 3), 4, 5, 6, [1, {"key1": 1, "key2": 2, "key3": {"Alumno1", "Alumno2", True}}, {1, 2, 3}]]
verListaRecursivaConTipoDatos(l, 0, type(l))