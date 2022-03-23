import sys, os
sys.path.append(os.path.join('D:\\', 'git', 'python', 'Parte2', 'libs'))
print(sys.path)
from pack3.module3 import CONSTANT_3
from pack2.module2 import CONSTANT_2, CONSTANT_1
print(CONSTANT_1)
print(CONSTANT_2)
print(CONSTANT_3)