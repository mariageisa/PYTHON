entrada = input('[E] para entra e [S] para passar : ')
senha = '12345678'
senha_digitada = input('Digite a senha : ')

if (entrada == 'E' or entrada == 'e'):
    if(senha == senha_digitada):
        print("Sucesso, voce entrou")
    else:
        print("senha incorreta")
elif (entrada == 'S' or entrada == 's'):
    if (senha == senha_digitada):
        print("sucesso, voce passou")
    else:
        print("voce não passou, senha incorreta" )
else:
    print("voce nao selecionou uma opçao valida")