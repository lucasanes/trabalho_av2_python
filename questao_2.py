def kaprekar(n):
  strN = str(n)
  half = len(strN) // 2

  if len(strN) % 2 == 0:

    left = int(strN[:half])
    right = int(strN[half:])

    result = left + right

    if result ** 2 == n:
      return 1
    else:
      return 0
  else:

    left = int(strN[:half])
    right = int(strN[half:])

    leftPlusOne = int(strN[:half+1])
    rightPlusOne = int(strN[half+1:])

    result = left + right
    resultPlusOne = leftPlusOne + rightPlusOne

    if result ** 2 == n or resultPlusOne ** 2 == n:
      return 1
    else:
      return 0

def main():
        
  while True:
    num = int(input('\nDigite um número: '))

    if num < 1 or num > 100000000:
      print('\nO número precisa ser maior que 1 e menor que 100.000.000')
      continue
    else:
      print(kaprekar(num))

    keep = input('\nDeseja continuar? (s/n): ')

    if keep == 'n' or keep == 'N':
      break
    elif keep == 's' or keep == 'S':
      continue
    else:
      print('\nOpção inválida.')
      break

if __name__ == '__main__':
  main()