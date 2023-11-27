def esBinario(strbinario):

  for caracter in strbinario:
    if caracter != "0" and caracter != "1":
      return False

  return True

def convertirBinarioADecimal(strbinario):

  numeroDecimal = 0
  for i, caracter in enumerate(strbinario[::-1]):
    numeroDecimal += int(caracter) * (2 ** i)

  return numeroDecimal

def main():
  strbinario = input("Introduce un número binario: ")

  if esBinario(strbinario):
    print(f"El número binario {strbinario} en decimal es {convertirBinarioADecimal(strbinario)}")
  else:
    print("La cadena introducida no es un número binario")

if __name__ == "__main__":
  main()