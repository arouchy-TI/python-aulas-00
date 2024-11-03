# maiusculo, minusculo e titulo

#curso = "  python"

#print(curso.upper())
#print(curso.lower())
#print(curso.title())

#eliminando espaços

#curso1 = "  python  "

#print(curso1.strip() + ".")
#print(curso1.lstrip()  + ".")
#print(curso1.rstrip()  + ".")


# junçao e centralizaçao de string

#curso2 = "python"
#menu = "Java"

#print(menu.center(20, "-"))
#print(curso2.center(10, "*"))
#print(".".join(curso2))
#print(".".join(menu))

# interpolaçao de strings

#nome = "guilherme "
#idade = 20
#profissao = "programmer"
#linguagem = "python"

#dados = {"nome": "Guilherme" ,"idade" : 28 }

#print("nome: %s idade: %d" % (nome,idade))


#print("nome: {} idade: {}".format(nome,idade))
#print("nome: {0} idade: {1}".format(nome,idade))

#print("nome: {name} idade: {age}".format(name=nome,age=idade))
#print("nome: {name} idade: {age} {name} {age}".format(name=nome,age=idade))
#print("nome: {nome} idade: {idade}".format(**dados))

# fatiamento de string

#name = "guilherme pererira dos santos"

#print(name[0])
#print(name[9:])
#print(name[:10])
#print(name[10:16])
#print(name[0:16:2])
#print(name[ : ])
#print(name[::-1])

#String multiplas linhas

name = "Guilher santos pereira silva"
nickname = "arouchy_live"
language = "python"
college= "Dio.pro"

print(f"""hello my name is {name}
    and I leanr python
        THIS message has diferent recuos
""")

print(f""" hello world my nickname is {nickname}
    and i learn {language}
        and i study in {college}
""")

print("""

    ==========MENU=========

      1- SACAR
      2- DEPOSITAR
      3- SALDO
      4- SAIR
    =======================
        OBRIGADO POR USAR NOSSO SISTEMA!!

""")