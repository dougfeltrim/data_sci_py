#Visualisação de doados em python

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]



titulo = "Scatterplot: grafico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.xlabel(eixoy)


plt.scatter(x,y, label = "Meus pontos", color = "red")
plt.plot(x,y)
plt.legend()
plt.show()



