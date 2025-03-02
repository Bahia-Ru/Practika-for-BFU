from itertools import *
ch1 = 0
for x in product('32nyd2@&$681qh(', repeat=9):
    ch1+=1
    print(ch1,'',x)
