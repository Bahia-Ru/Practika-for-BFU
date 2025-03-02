from sympy import *
#1
x = Symbol('x')
f =  x**3
derivative1_f = f.diff(x)
print('Производная 1го порядка: ', derivative1_f)
derivative2_f = f.diff(x,2)
print('Производная 2го порядка: ', derivative2_f)
derivative3_f = f.diff(x,3)
print('Производнaя 3го порядка: ', derivative3_f)



#2
x, y = symbols('x,y')
z = x**3 + 3*x**2*y + y**2

#Частные производные первого порядка
dzdx = diff(z,x,1)
dzdy = diff(z,y,1)
print('dz/dx=',dzdx)
print('dz/dy=',dzdy)

#Частные производные второго порядка
d2zdx2 = diff(z,x,2)
dz2dy2 = diff(z,y,2)
print('d2z/dx2=',d2zdx2)
print('d2z/dy2=',dz2dy2)

#Смешанные производные второго порядка
d2zdxy = diff(z,x,y)
d2zdyx = diff(z,y,x)
print('d2z/dxy=',d2zdxy)
print('d2z/dyx=',d2zdyx)
