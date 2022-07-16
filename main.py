#View - o que vai para o usuário
def view():
    usuario_digitado=input("Informe o seu usuário: ")
    senha_digitado=input("Informe sua senha: ")
    Controller(usuario_digitado, senha_digitado)
# Model - O que vem do banco de dados (BD)
def Model_usuario():
    usuário_BD= 'joão'
    return  usuário_BD
def Model_senha():
    senha_BD= '123'
    return senha_BD
#Controller - a validação
def Controller(usuario_digitado, senha_digitado):  #Separa as informações, códigos de cima não irão interferir nesses
    usuário_BD= Model_usuario()
    senha_BD= Model_senha()
    if usuario_digitado==usuário_BD and senha_digitado==senha_BD:
            print("pode entrar")
    else:
            print("Usuário ou senha incorreto")

view()
