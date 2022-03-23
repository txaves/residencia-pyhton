POSSIBLE_OPTIONS = ['M', 'm', 'S']
option = 'M'

while option in POSSIBLE_OPTIONS:
    print("Escolha 'M' para converter para maiúsculas")
    print("Escolha 'm' para converter para minúsculas")
    print("Escolha 'S' para quebrar as palavras da frase em um array")
    print("Escolha outra letra para sair")
    option = input("Escolha uma opção: ")
    text = input("Digite uma frase: ")
    if option == "M":
        print(text.upper())
    elif option == 'm':
        print(text.lower())
    elif option == 'S':
        print(text.split())
    else:
        print("Saindo!")