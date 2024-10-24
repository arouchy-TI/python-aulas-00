faturamento = 1000
custo = 700
lucro = faturamento - custo
#print("faturamento: " + str(faturamento))
#print(f"faturamento: {faturamento}")




email = "email_falso@gmail.com"
email = "EMAIL_FALSO@GMAIL.COM"


print(email.lower())
print(email.find("@"))
print(email[11])

#encontrar email de alguem

posicao = email.find("@")
servidor = email[posicao:]
print(servidor)

nome_email = email[:posicao]
print(nome_email)

# tamanho de um texto

tamanho = len(email)
print(tamanho)

#replace

email_trocado = email.replace("GMAIL.COM", "hotmail.com")
print(email_trocado)

# capitalize tittle
nome = "joa lira"
print(nome.capitalize())
print(nome.title())

#casos especiais

margem = lucro / faturamento
print(f"faturamento: R${faturamento:.2f}, custo: {custo}, lucro: {lucro}")
print(f"margem: {margem:.2%}")

#exercicio

nome = "Joao Paulo Lira"
email = "bebefalso2@gmail.com"

#descobrir servidor email

endereco_email = email.find("@")
posicao_email = email[endereco_email:]
print(posicao_email)

#descobrir primeiro nome usuario

first_name = nome.find(" ")
primeiro_nome = nome[:first_name]
print(primeiro_nome)

#mensagem

mensagem = f"Usuario: {primeiro_nome} foi cadastrado com sucesso com o email: {email}"

#mensagem

primeira_letra = email[0]
print(primeira_letra)
mensagem2 = f"Enviamos um email de confirmacao para o email {primeira_letra}***{posicao_email}"
print(mensagem2)



