# while - enquanto

# loop infinito
# while True:
contador = 0
while contador < 300: 
    print(contador)
    contador += 1 #contador = contador + 1

    if contador == 12:
        print("cheguei no 12")

    if contador == 290:
        break

print("saiu do while")
