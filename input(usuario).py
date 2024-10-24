nome = str(input("digite seu nome "))
email = str(input("digite seu email "))


#descobrir servidor email

endereco_email = email.find("@")
posicao_email = email[endereco_email:]
#print(posicao_email)

#descobrir primeiro nome usuario

first_name = nome.find(" ")
primeiro_nome = nome[:first_name]
#print(primeiro_nome)

#mensagem

mensagem = f"Usuario: {primeiro_nome} foi cadastrado com sucesso com o email: {email}"
print(mensagem)

#mensagem

primeira_letra = email[0]
mensagem2 = f"Enviamos um email de confirmacao para o email {primeira_letra}***{posicao_email}"
print(mensagem2)