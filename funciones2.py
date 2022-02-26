import numpy as np
import matplotlib.pyplot as plt
from gatoV import perro 

a, b = np.array([1, 2, 3]), np.array([6, 7, 8]) #definimos listas
c, d = 1, 6
f, g = 2, 7

res0 = perro(a,b) #aplicando funciones a listas arreglo de rsultados
res1 = perro(c,d)
res2 = perro(f,g)

print(res0)
print(res1)
#print(res2)

print(res0[0])


