## maior e menor elemento
# lista = [2, 3, 1]

# def pegar_menor_e_maior(lista):
#     maior = lista[0]
#     menor = lista[0]
#     for x in range(1, len(lista)):
#         if maior < lista[x]:
#             maior = lista[x]
#         if menor > lista[x]:
#             menor = lista[x]
#     return f"Menor: {menor}, Maior: {maior}"
# print(pegar_menor_e_maior(lista))


## Duplicados em uma Lista - retorne todos os elementos duplicados em uma lista.
# lista = [3, 1, 5, 5, 1]

# def retorna_duplicados(lista):
#     lista_duplicados = []
#     for x in range(len(lista)):
#         if lista.count(lista[x]) > 1 and lista[x] not in lista_duplicados:
#             lista_duplicados.append(lista[x])
#     return lista_duplicados
# print(retorna_duplicados(lista))


## inverte lista
# lista = [1, 2, 3]

# def inverte_lista(lista):
#     return lista[::-1]
# print(inverte_lista(lista))    


## Ordenação Personalizada: Desenvolva uma função de ordenação personalizada que ordene uma lista de strings primeiro pelo número de caracteres
# lista = ['abc', 'a', 'ab']

# def ordena_nmr_char(lista):
#     for x in range(len(lista)):
#         for y in range(len(lista)):
#             if len(lista[x]) < len(lista[y]):
#                 aux = lista[x]
#                 lista[x] = lista[y]
#                 lista[y] = aux
#     return lista
# print(ordena_nmr_char(lista))



