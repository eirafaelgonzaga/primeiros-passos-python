nome = input("Qual seu nome?")
idade = int(input("Qual sua idade?"))
altura = float(input("Qual sua altura em metros?"))

maior_idade = idade >= 18

print(f"Olá, {nome}! Você tem {idade} anos e {altura}m de altura.")
print(f"Você é maior de idade? {maior_idade}")