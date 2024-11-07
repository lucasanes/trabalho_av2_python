def isPrime(n):
  if n < 2:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True

def goldbach(p):
  if p % 2 != 0 or p < 4:
    return -1
  for i in range(2, p // 2 + 1):
    if isPrime(i) and isPrime(p - i):
      return i, p - i
  return -1

def main():

  while True:

    number = int(input("\nDigite um número par: "))

    if number % 2 != 0 or number < 4 or number > 4294967294:
      print("\nO número digitado não é par ou é menor que 4 ou maior que 4.294.967.294")
    else:
      print(goldbach(number))

    keep = input("\nDeseja continuar? (s/n): ")

    if keep == "n" or keep == "N":
      break
    elif keep == "s" or keep == "S":
      continue
    else:
      print("Opção inválida")
      break

if __name__ == "__main__":
  main()