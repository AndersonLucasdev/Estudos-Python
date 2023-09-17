## Leia um número N e escreva esse número ao contrário usando while.
# num = int(input("Digite um número: "))
# while num > 0:
#     res = num % 10
#     print(res, end="")
#     num //= 10

## Fibonnaci - mostrar todos numeros até numero
# num = int(input("Digite um número"))
# aux = 1
# aux_2 = 0
# while aux <= num:
#     aux = aux_2 + aux
#     print(aux)
#     aux_2 = aux + aux_2
#     print(aux_2)

## Fibonnaci - mostrar quantos termos
# termos = int(input("Digite quantos termos deseja ver: "))
# aux = 1
# aux_2 = 0
# contador = 0
# while contador < termos:
#     aux = aux + aux_2
#     print(aux)
#     contador += 1
#     if contador >= termos:
#         break
#     aux_2 = aux + aux_2
#     print(aux_2)
#     contador += 1


## Crie um programa para converter de binário para decimal usando while.
# num = int(input("Digite um número: "))
# aux = num
# soma = 0
# contador = 0
# while aux > 0:
#     if (aux % 10) == 1:
#         soma = soma + 2 ** contador
#     contador += 1 
#     aux //= 10
# print(f"O numéro numero {num} é {soma} em binarios")


## Um inteiro positivo é chamado de número de Armstrong de ordem se. Crie um programa para verificar se um número n é um número de Armstrong.
# num = int(input("Digite um número: "))
# aux = num
# digitos = 0
# while aux > 0: ## conseguir o nmr de digitos
#     aux //= 10
#     digitos += 1
# aux = num
# soma = 0
# while aux > 0:
#     digito = aux % 10
#     soma = soma + digito ** digitos
#     aux //= 10
# if soma == num:
#     print("numero de armstrong")
# else:
#     print("N é numero de armstrong")


## fatorial de um número
# num = int(input("Digite o número que deseja o fatorial: "))
# soma = 1
# contador = 1
# while contador < num:
#     soma += soma * contador
#     contador += 1
# print(soma)

## fatorial de numeros até o numero digitado
# num = int(input("Digite o numero: "))
# contador = 1
# while contador < num:
#     aux = 1
#     soma = 1
#     while aux < contador:
#         soma += soma * aux
#         aux += 1
#     print(soma)
#     contador += 1

## Modifique a questão anterior para encontrar todos os números de Armstrong dado um intervalo.
# num_x = int(input("Digite um número para o intervalo: "))
# num_y = int(input("Digite um número para o intervalo: "))

# while num_y > num_x:
#     digitos = 0
#     aux = num_x
#     while aux > 0:
#         aux //= 10
#         digitos += 1
#     aux = num_x
#     soma = 0
#     while aux > 0:
#         digito = aux % 10
#         soma = soma + digito ** digitos
#         aux //= 10
#     if soma == num_x:
#         print(soma)
#     num_x += 1

## intervalo numeros primos até numero
# num = int(input("Digite um número: "))
# contador = 1
# while contador < num:
#     aux = 1
#     div = 0
#     while aux <= contador:
#         if contador % aux == 0:
#             div += 1
#         aux += 1
#     if div == 2:
#         print(contador)
#     contador += 1