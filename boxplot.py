import matplotlib.pyplot as plt
import random

vetor = []

for i in range(10):
    num_aleatorio = random.randint(0,50000)
    vetor.append(num_aleatorio)
    
plt.boxplot(vetor)
plt.title('Boxplot')
plt.show()