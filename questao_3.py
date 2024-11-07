from collections import Counter
import string

def most_frequent_letters(text):
  letters = [char.lower() for char in text if char in string.ascii_letters]

  letter_counts = Counter(letters)

  most_common = letter_counts.most_common()
  most_common.sort(key=lambda x: (-x[1], x[0]))  

  result = []
  total_letters = sum(letter_counts.values())

  for letter, count in most_common[:2]:
      percentage = (count / total_letters) * 100
      result.append(f"{letter} {percentage:.2f}%")

  return "\n".join(result)

def main():

  while True:

    text = input("Digite a cadeia de caracteres: ")

    textWithoutSpaces = text.replace(" ", "")

    if len(text) == 0 or text != textWithoutSpaces or len(text) > 1000:
      print("O texto deve conter entre 1 e 1000 caracteres sem espaços em branco")
    else: 
      print(most_frequent_letters(text))

    keep = input("Deseja continuar? (s/n): ")

    if keep == 'n' or keep == 'N':
      break
    elif keep == 's' or keep == 'S': 
      continue
    else:
      print("Opção inválida")
      break

if __name__ == "__main__":
    main()