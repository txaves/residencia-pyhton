input1 = input("Insira a palavra #1")
input2 = input("Insira a palavra #2")
input3 = input("Insira a palavra #3")

input3 = input3.upper().replace('A', '').replace('E', '').replace('I', '').replace('O', '').replace('U', '')

print(input1.upper())
print(input2.lower())
print(input3)