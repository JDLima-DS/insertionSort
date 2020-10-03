from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import matplotlib as mp 
import numpy as np
from random import randint as random

# A função abaixo retorna um vetor de tamanho 3 a 20
# com elementos aleatórios entre 0 e 1000
def randlist():
  v = []
  sizeOf = random(10, 31)
  for i in range(2, sizeOf):
    v.append(random(0, 1000))
    
  return v

# A função abaixo recebe uma lista e retorna a mesma lista
# com seus elementos ordenados em ordem crescente
def insertSort(v):
  for j in range(1, len(v)): 
        key = v[j] 
        i = j-1
  
        while(i >= 0 and v[i] > key): 
            v[i+1] = v[i] 
            i -= 1
  
            yield v 
        
        v[i+1] = key 
        yield v 

# A função abaixo é chamada repetidamente para
# animar o gráfico
def animate(A, rects, iteration): 
  
    # setting the size of each bar equal 
    # to the value of the elements 
    for rect, val in zip(rects, A): 
        rect.set_height(val) 
  
    iteration[0] += 1
    text.set_text("iterations : {}".format(iteration[0])) 


print("Digite 1 para escolher os numeros")
print("Digite 2 para numeros aleatorios")
mode = int(input())

if mode == 1:
  v=[]
  n = int(input("Numero de termos: "))
  for i in range (0, n, 1):
    x = int(input())
    v.append(x)
    
  print("Original: {}".format(v))
  print("Ordenada: {}".format(insertSort(v)))

elif mode == 2:
  v = randlist()
  print("Original: {}".format(v))
  print("Ordenada: {}".format(insertSort(v)))

generator = insertSort(v)

fig, ax = plt.subplots() 
rects = ax.bar(range(len(v)), v, align="edge")

text = ax.text(0.01, 0.95, "", transform=ax.transAxes) 
iteration = [0] 

anim = FuncAnimation(fig, func=animate, 
                     fargs=(rects, iteration), frames=generator, interval=50, 
                     repeat=False)
plt.show()