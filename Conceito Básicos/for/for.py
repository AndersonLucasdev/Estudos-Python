## soma dos números primos até numero com for 
# num = int(input("Digite um número: "))
# soma = 0
# for contador in range(num):
#     div = 0
#     for aux in range(1, contador + 1):
#         if contador % aux == 0:
#             div += 1
#     if div == 2:
#         soma += contador
#         print(contador)
# print(f"A soma é igual a {soma}")

## fibonacci - quantos termos
# num = int(input("Digite o número: "))
# y = 1
# x = 0
# cont = 0
# for _ in range(1, num):
#     y = y + x
#     print(y)
#     cont += 1
#     if cont >= num:
#         break
#     x += y
#     print(x)
#     cont += 1
#     if cont >= num:
#         break

## calcular fatorial dos numeros até num
# num = int(input("Digite o numero: "))

# for contador in range(1, num):
#     soma = 1
#     for aux in range(1, contador + 1):
#         soma *= aux
#     print(soma)

## intervalo de armstrong
# num_x = int(input("Digite um número: "))
# num_y = int(input("Digite um número: "))

# for contador in range(num_x, num_y, 1):
#     aux = contador
#     digitos = 0
#     for _ in range(aux):
#         aux //= 10
#         digitos += 1
#         if aux == 0:
#             break
#     aux = contador
#     soma = 0
#     for _ in range(aux):
#         digito = aux % 10
#         soma = soma + (digito ** digitos)
#         aux //= 10
#         if aux == 0:
#             break
        
#     if soma == contador:
#         print(contador)


## numeros menor que n divisiveis 3 ou 5
# num = int(input("Digite um numero: "))

# for contador in range(1, num):
#     if contador % 3 == 0 or contador % 5 == 0:
#         print(contador)
