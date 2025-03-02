from sympy import * 

with open('input.txt', 'r') as file:
    F_str = file.read()
    f = sympify(F_str)

x, y, z= symbols('x,y,z')

dfdx = diff(f,x,1)
dfdy = diff(f,y,1)
dfdz = diff(f,z,1)
d2fdx2 =diff(f,x,2)
d3fdy3 = diff(f,y,3)
d4fdz4 =diff(f,z,4)
d2fdxy =diff(f,x,y)
d2fdzy =diff(f,z,y)
d2fdzx =diff(f,z,x)
d2fdxz = diff(f,x,z)

output = [dfdx, dfdy, dfdz, d2fdx2, d3fdy3, d4fdz4, d2fdxy, d2fdzy, d2fdzx, d2fdxz]


with open('output.txt', 'w') as outputFile:
    for i in output:
        outputFile.write(f'{i}\n')