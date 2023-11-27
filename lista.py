def estaEnRango(valor, minimo, maximo):
  """
  Devuelve True o False determinando que valor se encuentra entre el mínimo y el máximo.

  """
  return minimo <= valor <= maximo


def estaEnLista(valor, lista):
  """
  Devuelve True o False determinando si el valor está en la lista.

  """
  return valor in lista

def main():
  numero = int(input("Introduce un número del 1 al 20: "))

  # Comprobamos que el número introducido está en el rango indicado

  if not estaEnRango(numero, 1, 20):
    print("El número introducido no está en el rango indicado")
    return

  # Comprobamos si el número está en la lista

  if estaEnLista(numero, [6, 14, 11, 3, 2, 1, 15, 19]):
    print(f"El número {numero} está en la lista")
  else:
    print(f"El número {numero} no está en la lista")

if __name__ == "__main__":
  main()