from TESTES import posicao

vendas = [100, 200, 300, 400, 500, 600]

#print(vendas[-1])
#print(vendas[-2])
#print(vendas[1])

quantidade = len(vendas)
print(quantidade)
total_vendas = sum(vendas)
print(total_vendas)

valor_max = max(vendas)
valor_min = min(vendas)

print(valor_max, valor_min)

posicao = vendas.index(600)
print(posicao)
print(vendas[:5])

#verificar se produto foi cadastrado

produtos = ["iphone","ipad","ipod"]
preco = [4000,5000,6000]
preco2 = [200, 300, 400, 500]
print("iphone" in produtos)

# editar o item

preco[0] = 4500
novo_preco = preco[0] * 1.1
print(f"preco com aumento de 10% vai ser ",novo_preco)

# adicionar novo item na lista

produtos.append("macbook")
preco.append("10000")
print(produtos)
print(preco)

# remover um item da lista

produtos.remove("macbook")
preco.pop(3)
print(produtos)
print(preco)

# inserir um valor na lista

produtos.insert(1,"ipod")
print(produtos)

# contar valores

print(produtos.count("ipod"))

# ordem crescente e ordem decrescente

preco.sort()
preco2.sort(reverse = True)
print(preco)
print(preco2)