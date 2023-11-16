# peça três temperaturas coloque em uma lista
# caso seja igual ou maior que 38 graus avisar que está com febre
# adicione duas novas temperaturas
# delete a temperatura do segundo indice
# delete a ULTIMA temperatura
# imprima os resultados

temperatura = float(input("Temperatura: "))
temperatura2 = float(input("Temperatura: "))
temperatura3 = float(input("Temperatura: "))
lista_temp = [temperatura, temperatura2, temperatura3]
if(temperatura >= 38): 
    print("temperatura-1 está com febre")
if(temperatura2 >= 38):
    print("temperatura-2 está com febre")
if(temperatura3 >= 38):
    print("temperatura-3 está com febre")

lista_temp.append(15)
lista_temp.append(16)
del lista_temp[1]
del lista_temp[-1]
print(lista_temp)
print("fim do programa")