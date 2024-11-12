def generateMagicSquare(n):
  square = [[0] * n for _ in range(n)]

  i, j = 0, n // 2
  for num in range(1, n * n + 1):
    square[i][j] = num
    new_i, new_j = (i - 1) % n, (j + 1) % n
    if square[new_i][new_j] != 0: 
      i += 1
    else:
      i, j = new_i, new_j

  return square

def impressMagicSquare(square):
  for line in square:
    print(" ".join(f"{num:2}" for num in line))

def main():
  while True:
    try:
      n2 = int(input('\nSeja muito bem vindo ao gerador de quadrado mágico:\n1 - Iniciar\n2 - Sair\n'))

      if n2 == 2:
        break
      elif n2 == 1:
        n = int(input("\nDigite um número ímpar para o tamanho do quadrado mágico (3 ≤ n ≤ 15): "))
        if n % 2 == 1 and 3 <= n <= 15:

          magicSquare = generateMagicSquare(n)
          magicConstant = n * (n**2 + 1) // 2
          print("\nQuadrado Mágico:")
          impressMagicSquare(magicSquare)
          print(f"\nConstante Mágica: {magicConstant}")

          repeat = str(input('\nDeseja voltar? [s/n]\n'))
          if repeat == 'S' or repeat == 's':
            continue
          elif repeat == 'N' or repeat == 'n':
            break
          else:
            print('\nResponda com S ou N.')
            repeat = str(input('\nDeseja voltar? [s/n]\n'))
        else:
          print("\nPor favor, digite um número ímpar entre 3 e 15.")
      else:
          break
    except ValueError:
      print("\nEntrada inválida. Por favor, digite um número ímpar entre 3 e 15.")

if __name__ == "__main__":
    main()