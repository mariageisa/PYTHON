nome = "geisa"
altura = 1.50
peso = 47
imc = peso / (altura * altura)

print(nome, " tem ", altura, "de altura ",)
print("pesa ", peso, "quilos e seu IMC é:")
print(imc)

# A RESPOSTA DESSA QUESTÃO DEVE SER:
# FULANO TEM ALT DE ALTURA, PESA QUILOS E SEU IMC É:
# Valor 

#INTERPOLAÇÃO

print(f'{nome} tem {altura: .2f} de altura, pesa {peso} quilos e seu imc é:  {imc: .2f}')