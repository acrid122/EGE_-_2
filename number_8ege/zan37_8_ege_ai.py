from itertools import *
c1 = 0
c2 = 0

for num, name in enumerate(product(sorted('НОРМАЛЬЕ'))), 1):
    name = "".join(name)   
    if  name.startswith('НОРМ'):
        c1 == num
        break

for num, name in enumerate(product(sorted('НОРМАЛЬЕ'))), 1):
    name = "".join(name)
    if name.startswith('НЕНОРМ'):
        c2 == num       
        break
        
print(num)
