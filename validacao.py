import banco
#Controller - a validação
def Validar_login(usuario_digitado, senha_digitado):  #Separa as informações, códigos de cima não irão interferir nesses
    usuário_BD= banco.Model_usuario()
    senha_BD= banco.Model_senha()
    if usuario_digitado==usuário_BD and senha_digitado==senha_BD:
            print("pode entrar")
    else:
            print("Usuário ou senha incorreto")