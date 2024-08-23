loginR = "admin"
senhaR = "123"
login = input('Digite seu login: ')
senha = input('Digite sua senha: ')
if (login == loginR) and (senha == senhaR):
    print ('Olá admin, seja bem-vindo!')
else:
    print('login ou senha incorretos, tente novamente.')