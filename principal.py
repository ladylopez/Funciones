import numpy as np
import matplotlib.pyplot as plt
#from gatoV import perro
from funexp import fun2

a, b = np.array([1, 2, 3]), np.array([6, 7, 8]) #definimos listas
h = np.array([26,12,8])

c, d = 1, 6
f, g = 2, 7

#res0 = perro(a,b) #aplicando funciones a listas arreglo de rsultados
#res1 = perro(c,d)
#res2 = perro(f,g)

res3 = fun2(a,b,h)

#print(res0)
#print(res1)
#print(res2)

#print(res0[0])
print(res3)



