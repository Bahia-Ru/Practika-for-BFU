#Для общего выполнения 1
from sympy import *
x = Symbol('x')
y = (2+(x**2 - 2*x)**0.5)/(1+x)

derivative1_f = y.diff(x)
print('Производная 1го порядка: ', derivative1_f)
derivative2_f = y.diff(x,2)
print('Производная 2го порядка: ', derivative2_f)
derivative3_f = y.diff(x,5)
print('Производнaя 5го порядка: ', derivative3_f)