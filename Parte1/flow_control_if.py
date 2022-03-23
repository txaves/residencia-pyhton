print("Digite 'M' para converter para maiúsculas")
print("Digite 'm' para converter para minúsculas")
print("Digite 'S' para quebrar as palavras da frase em um array")
option = input("Escolha uma opção: ")
text = input("Digite uma frase: ")


if option == "M":
    print(text.upper())
elif option == 'm':
    print(text.lower())
else:
    print(text.split())