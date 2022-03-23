text = input("Digite uma frase")

text_array = text.split()

for word in text_array:
    print(word[:2])