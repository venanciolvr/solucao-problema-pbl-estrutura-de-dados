# Criando as matrizes para cada caminhão da frota
caminhao1 = []
caminhao2 = []
caminhao3 = []

for i in range(3):
  caminhao1.append([0]*2)
  caminhao2.append([0]*2)
  caminhao3.append([0]*3)

print(f"Matriz do caminhão 1: \n{caminhao1}")
print(f"Matriz do caminhão 2: \n{caminhao2}")
print(f"Matriz do caminhão 3: \n{caminhao3}")

# Adicionando os produtos à matriz dos veículos
# Carregamento do caminhão 1 
caminhao1[0][0] = "Produto 1"
caminhao1[0][1] = "Produto 1"
caminhao1[1][0] = "Produto 3"
caminhao1[1][1] = "Produto 3"
caminhao1[2][0] = "Produto 2"
caminhao1[2][1] = "Produto 2"

# Carregamento do caminhão 2
caminhao2[0][0] = "Produto 2"
caminhao2[1][0] = "Produto 3"
caminhao2[1][1] = "Produto 3"
caminhao2[2][1] = "Produto 1"

# Carregamento do caminhão 3
caminhao3[0][0] = "Produto 1"
caminhao3[0][1] = "Produto 1"
caminhao3[1][0] = "Produto 3"
caminhao3[1][1] = "Produto 3"
caminhao3[2][0] = "Produto 2"

#Imprimindo as matrizes dos veículos
print(f"Matriz do caminhão 1: \n{caminhao1}")
print(f"Matriz do caminhão 2: \n{caminhao2}")
print(f"Matriz do caminhão 3: \n{caminhao3}")