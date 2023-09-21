#Calculadora de Fatorial/Binomial
# N = 7
# P = 5
# def fatorial(num: int) -> int:
#     soma = 1
#     for x in range(1, num + 1):
#         soma = soma * x
#     return soma

# def comb(N, P):
#     res = fatorial(N) / (fatorial(P) * fatorial(N - P))
#     return res

# print(comb(N, P))



## retorna digitos
# num = 12345
# def retorna_digitos(num: int) -> int:
#     digitos = 0
#     aux = num
#     while aux > 0:
#         digitos += 1
#         aux //= 10
#     return digitos
# print(retorna_digitos(num))



## fibonnaci - até numero
# num = 10

# def fibonnaci(num: int) -> None:
#     aux = 1
#     aux_2 = 0
#     while aux <= num:
#         aux = aux_2 + aux
#         if aux >= num:
#             break
#         print(aux)
#         aux_2 = aux + aux_2
#         if aux_2 >= num:
#             break
#         print(aux_2)

# print(fibonnaci(num))


