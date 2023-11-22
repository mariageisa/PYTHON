'''Faça um codigo que peça uma nota, entre 0 e 10. Mostre uma mensagem caso a nota seja inválida
# e continue pedindo até que o usuario informe uma nota válida'''

while True:
    nota = float(input('Informe sua nota: '))
    if nota == 0 or nota >10:
        print('nota invalida')
    elif nota>=1 and nota<=10:
      break
    

