def contador_de_vogais(Texto_Usuario):

    Vogais = "AEiOU"
    Vogais = Vogais.lower()

    contador = 0

    for Letra_do_Texto in Texto_Usuario:
        if Letra_do_Texto in Vogais:
            contador += 1
    
    return contador

Tecla_do_Usuario = input("digite uma palavra: ")

Resultado_do_Contador = contador_de_vogais(Tecla_do_Usuario)

print(f"A palavra {Tecla_do_Usuario} Possui {Resultado_do_Contador} vogais")


#_______________________________________________________________________________#

def conta_vogais(texto):
    
    # TODO: Defina um conjunto de vogais tanto minúsculas quanto maiúsculas:

    VOGAIS = "AeIoU"
    VOGAIS = VOGAIS.lower()
    
    # TODO: Inicialize um contador para contar as vogais:
    
    contador = 0

    # Iteramos pelos caracteres da string
    for char in texto:
        # TODO: Verifique se o caractere atual é uma vogal e incremente o valor do contador:
        if char in VOGAIS:
            contador += 1
    
    return contador

# Solicitamos ao usuário que insira uma string
texto = str(input())

# Chamamos a função conta_vogais e exibimos o resultado
resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")