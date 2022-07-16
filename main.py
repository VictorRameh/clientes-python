#View - o que vai para o usuário
usuaio=input("Informe o seu usuário: ")
senha=input("Informe sua senha: ")

# Model - O que vem do banco de dados (BD)
usuário_BD= 'joão'
senha_BD= '123'

#Controller - a validação
if usuário=='joão' and senha=='123':
    print("pode entrar")
else:
    print("Usuário ou senha incorreto")