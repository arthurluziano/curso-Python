cornos = ["Tur", "Fab", "Dan", "Dragão", "Huguinho", "Gabs"]
#           0      1      2         3         4         5
#          -6     -5     -4        -3        -2        -1

# print(cornos[-1]) # Retorna o último valor (Ordem de trás pra frente).
# print(cornos[2]) # Retorna o valor do índice 2.
# print(cornos[1:]) # Retorna os valores do índice 1 até o fim da coleção.
# print(cornos[1:4]) # Retorna os valores do índice 1 até o índice 4 (excluindo o valor do 4° índice).

cornos[3] = "Levi"

cornos.extend(["João", "Pedro"]) # Concatena uma nova lista na lista especificada.
cornos.append("Bruno") # Adiciona um valor à lista.
print(cornos)