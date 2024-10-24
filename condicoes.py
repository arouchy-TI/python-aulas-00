#faturamento = 1000
#custo = 800
#lucro = faturamento - custo

#if lucro >= 0:
#    print(f"o lucro foi de {lucro}")
#else:
#    print("Prejuizo")


#produtos = ["iphone","ipad","ipod"]
#novo_produto = input("digite um novo produto ")
#novo_produto = novo_produto.lower()

#if novo_produto in produtos:
#    print(f"{novo_produto},Produto ja cadastrado ")
#else:
#    print(f"{novo_produto},Produto cadastrado com sucesso")
#   produtos.append(novo_produto)

#print(produtos)


# vendas acima de 15000 -> bonus 500
# vendas acima de 10000 -> bonus de 250
# vendas acima de 5000 -> bonus de 50
vendas = 15000

if vendas > 15000:
    bonus = 500
elif vendas > 10000:
    bonus = 250
elif vendas > 5000:
    bonus = 50
else:
    bonus = 0
#print(f"bonus foi de {bonus}")


if vendas > 5000:
    if vendas > 10000:
        bonus = 250
    else:
        bonus = 50
        if vendas > 15000:
            bonus = 500
        else:
            bonus = 250
else:
    bonus = 0
#print("bonus foi de", bonus)


# vendas acima de 15000 -> bonus 500
# vendas acima de 10000 -> bonus de 250
# vendas acima de 5000 -> bonus de 50
# bonus somente vendas empresa acima 50000

vendas = 17000
vendas_empresa = 60000
meta_empresa = 50000

if not vendas_empresa > meta_empresa:
    bonus = 0
else:
    if vendas > 15000 and vendas_empresa > meta_empresa:
        bonus = 500
    elif vendas > 10000:
        bonus = 250
    elif vendas > 5000:
        bonus = 50
    else:
        bonus = 0

#print("bonus foi de",bonus)

#desafio
#consultar produtos

preco = [1500,1000,800,2000]
produtos = ["celular","camera","fone de ouvido", "monitor"]

produto_usuario = input("digite o produto que esta procurando? ")
produto_usuario.lower()

if produto_usuario in produtos:
    produtos.index("celular")
    print(f"o produto {produto_usuario} custa ",preco[1])

elif produto_usuario in produtos:
    produtos.index("camera")
    print(f"o produto {produto_usuario},custa ",preco[0])




else:
    print("nao temos esse produto produto")



