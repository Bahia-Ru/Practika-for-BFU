#2
from sympy import *
x, y, z= symbols('x,y,z')

F = (ln(z**2)+cos(y)+sin(x))/(z*x**2*y**2)

dFdx=diff(F,x,1)
dFdy=diff(F,y,1)
dFdz=diff(F,z,1)
d2Fdx2=diff(F,x,2)
d2Fdy2=diff(F,y,2)
d2Fdz2=diff(F,z,2)
d2Fdxdy=diff(F,x,y)
d2Fdzdy=diff(F,z,y)

print('dFdx',dFdx,
      '\n','dFdy=',dFdy,
      '\n','dFdz=',dFdz,
      '\n','d2Fdx2=',d2Fdx2,
      '\n','d2Fdy2=',d2Fdy2,
      '\n','d2Fdz2=',d2Fdz2,
      '\n','d2Fdxdy=',d2Fdxdy,
      '\n','d2Fdxdy=',d2Fdxdy,
      '\n','d2Fdzdy=',d2Fdzdy)