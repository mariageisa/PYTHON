numero = int(input("Digite um número inteiro: "))

if numero <= 1:
    print(numero, "não é um número primo.")
else:
    eh_primo = True
    i = 2
    while i <= int(numero**0.5):
        if numero % i == 0:
            eh_primo = False
            break
        i += 1

    if eh_primo:
        print(numero, "é um número primo.")
    else:
        print(numero, "não é um número primo.")