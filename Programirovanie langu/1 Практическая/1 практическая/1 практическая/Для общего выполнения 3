from sympy import *

with open('input.txt', 'r') as file:
    F_str = file.read()
    F = sympify(F_str)


x, y, z = symbols('x, y, z')

dF_dx = f'dF_dx {diff(F, x)}' 
dF_dy = f'dF_dy {diff(F, y)}'  
dF_dz = f'dF_dz {diff(F, z)}' 


d2F_dx2 = f'd2F_dx2 {diff(F, x, 2)}' 
d2F_dy2 = f'd2F_dy2 {diff(F, y, 2)}' 
d2F_dz2 = f'd2F_dz2 {diff(F, z, 2)}'  


d3F_dy3 = f'd3F_dy3 {diff(F, y, 3)}'  


d4F_dz4 = f'd4F_dz4 {diff(F, z, 4)}' 


d2F_dxdy = f'd2F_dxdy {diff(F, x, y)}' 
d2F_dzdx = f'd2F_dzdx {diff(F, z, x)}'
d2F_dxdz = f'd2F_dxdz {diff(F, x, z)}'

output = [dF_dx, dF_dy, dF_dz, d2F_dx2, d2F_dy2, d2F_dz2, d3F_dy3, d4F_dz4, d2F_dxdy, d2F_dzdx, d2F_dxdz]

with open('output.txt', 'w') as outputFile:
    for i in output:
        outputFile.write(f'{i}\n')
