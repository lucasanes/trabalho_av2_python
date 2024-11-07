def convert(msg):
  cleanMessage = ''.join(filter(str.isalnum, msg))

  if len(cleanMessage) == 0:
    return "A mensagem não contém caracteres alfanuméricos"
  
  alphaFragments = []
  numberFragments = []

  cleanAlphaFragments = []

  i = 0

  while i < len(cleanMessage):
    if cleanMessage[i].isdigit():
      num = ''
      while i < len(cleanMessage) and cleanMessage[i].isdigit():
        num += cleanMessage[i]
        i += 1
      numberFragments.append(int(num))
    else:
      text = ''
      while i < len(cleanMessage) and cleanMessage[i].isalpha():
        text += cleanMessage[i]
        i += 1
      alphaFragments.append(text)

  for fragment in numberFragments:
    if fragment >= 100 and fragment <= 200:
      index = numberFragments.index(fragment)
      cleanAlphaFragments.append(alphaFragments[index])

  return ''.join(cleanAlphaFragments)

def main():
  while True:
    message = input("Digite a mensagem do Kni: ") 
    messageWithoutSpaces = message.replace(" ", "")

    if len(message) > 250:
      print("A mensagem deve conter até 250 caracteres sem espaços em branco")
    else: 
      print(convert(messageWithoutSpaces))
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