import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol #libreria para calcular la derivada
import sympy

#creacion de variables
xi= 0 #variables para inicializar
x = Symbol('x')
tolerancia = 0.00001
error = 1


f = input("Digite una funcion (con variable x): ")
df = sympy.diff(f) #Deriva a la funcion F

print("La derivada de la funcion es : ",df)

f= sympy.lambdify(x, f)
df= sympy.lambdify(x, df)

i = 0.1
while error > tolerancia:
  i+=1
  raiz = xi - (f(xi)/df(xi))
  error = np.abs((raiz-xi)/raiz)
  print('x ',i, '= ', xi) #muestra cuantas iteraciones se hicieron
  xi = raiz

print("La raiz es: ",raiz)
print("El valor de f(x) es: ", f(raiz))

#codigo para la grafica
xs = np.linspace(raiz-1, raiz+1, 50) #evaluar puntos de raiz-1 y raiz+1,en este caso 50
plt.plot(xs, f(xs), label = 'f(x)')
plt.title("Metodo Newton - Raphson")
plt.axhline(y=0, color = 'g')
plt.plot(raiz, f(raiz),'bo',label = f'f(x)=0, x={raiz:.6f}', color= 'k') #ver el punto en la grafica
plt.legend(loc = 'upper left')
plt.show()
#muestra la grafica