''' Escreva um código que, recebe três palavras e uma frase, crie uma função que verifique se as
 palavras aparecem COMPLETAS na frase e indique qual intervalo de índices ele foi encontrada. Você deve 
 utilizar uma lista para realizar a atividade.

Obs.: você deve validar se a palavra tem três ou mais letras
Obs.: você deve validar se a frase tem pelo menos 20 palavras'''

def verificar_palavras(palavras, frase):
    # Validar se a frase tem pelo menos 20 palavras
    if len(frase.split()) < 2:
        return "A frase não contém pelo menos 20 palavras."
    
    resultados = []
    for palavra in palavras:
        # Validar se a palavra tem três ou mais letras
        if len(palavra) >= 3:
            # Verificar se a palavra aparece completa na frase
            inicio = frase.find(palavra)
            
            if inicio != -1:
                fim = inicio + len(palavra)
                resultados.append((palavra, inicio, fim))
            else:
                resultados.append((palavra, "não encontrada"))
        else:
            resultados.append((palavra, "tem menos de três letras"))
    
    return resultados

# Exemplo de uso da função
palavra1 = input('Digite uma palavra: ')
palavra2 = input('Digite uma palavra: ')
palavra3 = input('Digite uma palavra: ')
palavras = palavra1, palavra2, palavra3
frase = input('Digite uma frase: ')
print(verificar_palavras(palavras, frase))