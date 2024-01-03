# Receba a altura(h) de uma pessoa, crie um código que calcule seu peso ideal, utilizando as fórmulas abaixo:Para homens: (72.7*h) - 58 Para mulheres: (62.1*h) - 44.7

h = float (input("Qual sua altura?   "))
m = float((72.7)* float(h) - 58)
f = float(float(62.1)* float(h) - float(44.7))

print (f'De acordo com sua altura a media de peso ideal se voce for do sexo masculino: {m}. E feminino a media sera: {f}')