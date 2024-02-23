def fazerBigMac(nome):
  print(f"Nome: {nome}")
  print("Sanduíche: Big Mac")

def fazerBatata(tamanho):
  print(f"Batata: {tamanho}")

def prepararRefri(tipo, tamanho):
  print(f"Refrigerante: {tipo} {tamanho}")

def combo(nome, tamanhoBatata, tipoRefri, tamanhoRefri):
  print("----- Bem-vindo -----")
  fazerBigMac(nome)
  fazerBatata(tamanhoBatata)
  prepararRefri(tipoRefri, tamanhoRefri)
  print("---------------------")

combo("Arthur", "Média", "Coca-cola", "700ml")