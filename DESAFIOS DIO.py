def verificador_ano_bissexto():
    ano = int(input("digite um ano "))
    
    if ano % 4 == 0:
      if ano % 100 != 0 or ano % 400 == 0:
        print("SIM")
      
      else:
        print("NÃO")
    
    else:
      print("NÃO")

# TODO: Verifique se o ano é bissexto utilizando uma estrutura de controle condicional, como if/else:


verificador_ano_bissexto()