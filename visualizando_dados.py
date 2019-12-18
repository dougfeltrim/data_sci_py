#Visualisação de doados em python

import matplotlib.pyplot as plt

x = [1,2, 5]
y = [2,3, 7]

#titulo
plt.title("Meu primeiro grafico com python")

#eixos
plt.xlabel("eixo X")
plt.xlabel("eixo Y")


plt.plot(x,y)
plt.show()


