text = 2

try:
    print(text)
except NameError as error:
    print("NameError - Esse nome não existe:",  error)
except Exception as error:
    print("Exception - Vixi:",  error)
else:
    text +=1
    print("Else:", text)
finally:
    text = []
    print("Finally:", text)

print("Fora do bloco!")