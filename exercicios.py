# 1 questão
# num1 = num2 = 0

# num1 = int(input("Infome um numero: "))
# num2 = int(input("Informe outro numero: "))

# if (num1>num2):
#     print (f"O maior numero é: {num1}")

# else:
#     print(f"O maior Numero é: {num2} ")

#---

# QUESTÃO 2
# num1 = 0
# final_num = None

# num1 = float(input("Informe um numero: "))

# if num1 > 0:
#     final_num =  num1 ** 0.5
#     print(f"O valor da raiz quadrada é: {final_num}")

# elif num1< 0:
#     print("Numero invalido") 
 
#---
       
# EXERCICIO 2 INCREMENTADO COM WHILE
# num1 = 0
# final_num = None
# resposta = None

# while  True:
#  num1 = float(input("Informe um número: "))
 
#  if num1 > 0:
#   final_num = num1 **0.5
#   print(f"O valor da raiz quadrada é:{final_num} ")
  
 
#  elif num1 <0:
#   print("Valor incorreto") 
#   resposta = input("deseja continuar? (S/N): ") 
#   if (resposta == "n") or (resposta =="N"):
#    #na linha 46 fazemos um ANINHAMENTO(NESTING)
#    break
  
#---

#EXERCICIO 3


# num1 = float(input("Informe um numero: "))

# if num1 > 0:
#     num_final = num1 **0.5
#     print(f"O valor da raiz é {num_final}")


# elif num1 <=0:
#     num_final = num1**2
#     print(f"O valor ao quadrado desse numero é {num_final}")

 
#Exercicio 4
#------

# num1 = 0 
# calc_raiz = calc_quadrado = 0
# resposta = None

# while True:

#     num1 = float(input("Por favor informe um número: "))

#     if num1 >= 0:
#         calc_raiz = num1 ** 0.5
#         calc_quadrado = num1 **2
#         print(f"O valor de {num1} ao quadrado é: {calc_quadrado} e este é o valor da raiz dele: {calc_raiz} ")

#     elif num1<0:

#         print("Você digitou num numero negativo")
#         resposta =  input(" deseja continuar? (S/N): ")
#         if (resposta == "n") or (resposta == "N"):
#             break
   
#Exercicio 5

# num1 = 0 
# valor_final = None

# num1 = int(input("Informe um numero: "))
# valor_final = num1%2

# if valor_final%2:
#     print(f"{num1} é Impar")

# else:
#     print(f"{num1} é Par ")

# Exercicio 6
#---

# n1 = n2 = 0
# valor_maior = None

# n1 = int(input("Informe um valor: "))
# n2 = int(input("Informe outro valor: "))

# if (n1 != n2):
#     valor_maior = max(n1,n2)
#     print(f"O maior valor é: {valor_maior}")
#     print(f"A diferença é: {abs(n1 - n2)}")
# else:
#     print("Os dois numeros são iguais ")


#Exercicio 7
#---

# n1=n2=0
# final_number = 0

# n1= float(input("Porfavor informe um número: "))
# n2 = float(input("Porfavor informe outro numero: "))

# if (n1 != n2):
#     final_number = (max(n1,n2))
#     print(f"Entre {n1} e {n2} o maior valor é: {final_number}")
# else:
#   print("Você digitou valores iguais.")

#Exercicio 8

# nota1=nota2=0
# media = None

# nota1 = float(input("Informe a primeira nota do aluno: "))
# nota2 = float(input("Informe a segunda nota do aluno: "))

# if (nota1 >= 0) and (nota1<=10) and (nota2 >=0 ) and (nota2 <=10):
#     media = (nota1 + nota2)/2
#     print(f"Sua primeira nota foi {nota1} e a segunda foi {nota2} sua média é: {media}")
# else:
#     print("Você informou um valor invalido.")

#Exercicio 9

# salario = prestacao = 0

# salario = float(input("Porfavor Informe seu salario: "))
# prestacao = float(input("Por favor informe o valor da prestacao: "))

# if (prestacao > (salario * 0.20 )):
#     print("Valor não concedido")
# else:
#     print("Valor concedido")

# pessoa = None
# altura_h = contador_h = 0
# altura_m = contador_m = 0

# pessoa = input("Você é homem ou mulher? ")

# if (pessoa == "H") or (pessoa == "h") or (pessoa == "HOMEM" ) or (pessoa == "homem") or (pessoa == "Homem"):
#  altura_h= float(input("Informe sua altura: "))
#  contador_h = (72.7 * altura_h) - 58
#  print(f"Seu peso ideal é: {contador_h}")

# elif (pessoa == "M") or (pessoa == "m") or (pessoa == "MULHER") or (pessoa == "mulher") or (pessoa == "Mulher"):
#  altura_m = float(input("Informe sua altura: "))
#  contador_m = (62.1 * altura_m) - 44.7
#  print(f"Seu peso ideal é: {contador_m}")

# else:
#  print("Você não especificou.")