#Crescimento da população Brasileira 1980-2016
#DataSus
import matplotlib.pyplot as plt

dados = open("populacao-brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0: #ignorando a primeira linha
        linha = dados[i].split(";")
        x.append(int(linha[0])) #ano
        y.append(int(linha[1])) #populacao
        
plt.bar(x,y, color = "gray")
plt.plot(x,y, color = "blue", linestyle="--")
plt.title("Crescimento da Populacao Brasileira 1980-2016")
plt.xlabel("Ano")
plt.ylabel("Populacao em milhoes")
#plt.show()
plt.savefig("pop_br.png", dpi=300)
