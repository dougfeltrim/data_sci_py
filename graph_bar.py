#Visualisação de doados em python

import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]

titulo = "Grafico de barras 2"
eixox = "Eixo X"
eixoy = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.xlabel(eixoy)


plt.bar(x1,y1, label = "grupo 1")
plt.bar(x2,y2, label = "grupo 2")
plt.legend()
plt.show()


