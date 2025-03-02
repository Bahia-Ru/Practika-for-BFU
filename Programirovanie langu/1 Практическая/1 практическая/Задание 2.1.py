from math import *
x = int(input('x='))
y = int(input('y='))
z = int(input('z='))


if y**7<0 or ((y**2) - (5*x*y*z) + (z**5)) == 0 or log((y**7),e)  +  (2**(x*3))  * (e**(3*x)) < 0 :
    print('Error')
    
else:
    F =  ((log((y**7), e)   +  (2**(x*3))*(e**(3*x)))**0.5 )  /  ((y**2) - (5*x*y*z) + (z**5))
    print (F)


