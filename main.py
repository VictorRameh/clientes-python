#View - o que vai para o usuário
usuario_digitado=input("Informe o seu usuário: ")
senha_digitado=input("Informe sua senha: ")

# Model - O que vem do banco de dados (BD)
usuário_BD= 'joão'
senha_BD= '123'

#Controller - a validação
if usuario_digitado==usuário_BD and senha_digitado==senha_BD:
    print("pode entrar")
else:
    print("Usuário ou senha incorreto")