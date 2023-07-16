while True:
    user = str(input('Informe um nome de usuario: '))
    passw = str(input('Informe uma senha:'))
    
    
    if user == passw:
        print('ERROR: A SENHA NÃO PODE SER IGUAL AO NOME DO USUARIO')
    
    else:
        print('Usuario cadastrado!')
        break