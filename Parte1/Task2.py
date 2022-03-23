menu = {"Sonho": 5, "Croissant": 4, "Coxinha": 3, "Pastel": 4.5, "Refrigerante": 6}

item1 = input("Escolha o primeiro item do pedido: ")
item2 = input("Escolha o segundo item do pedido: ")

total = menu[item1] + menu[item2]
print("Seu total foi: R$ %.2f" % total)