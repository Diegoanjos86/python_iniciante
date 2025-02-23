lista_numeros = [1, 2, 3]

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])

# alterando o valor da lista

lista_numeros[0] = 5
print(lista_numeros[0])

#lista de strings

lista_nomes = ["Diego", "Daiane", "Tania"]
print(lista_nomes)

#metodo append

lista_vazia = []
lista_vazia.append("Olá")
lista_vazia.append("Mundo")
print(lista_vazia)

# Principais Métodos de Listas em Python e Seus Usos:

# 1. append(item): Adiciona um item ao final da lista.
#    Exemplo: lista.append(10) adiciona o número 10 ao final da lista.

# 2. extend(iterable): Adiciona todos os elementos de um iterável (como outra lista) ao final da lista.
#    Exemplo: lista.extend([1, 2, 3]) adiciona os elementos 1, 2 e 3 ao final da lista.

# 3. insert(index, item): Insere um item em uma posição específica da lista.
#    Exemplo: lista.insert(0, 'a') insere 'a' no início da lista.

# 4. remove(item): Remove o primeiro item da lista que corresponde ao valor especificado.
#    Exemplo: lista.remove('b') remove a primeira ocorrência de 'b' na lista.

# 5. pop([index]): Remove e retorna o item na posição especificada. Se nenhum índice for fornecido, remove e retorna o último item.
#    Exemplo: lista.pop(2) remove e retorna o item na posição 2.

# 6. index(item[, start[, end]]): Retorna o índice da primeira ocorrência do item na lista. Pode especificar um intervalo de busca.
#    Exemplo: lista.index('a') retorna o índice da primeira ocorrência de 'a'.

# 7. count(item): Retorna o número de vezes que o item aparece na lista.
#    Exemplo: lista.count(5) retorna o número de vezes que o número 5 aparece na lista.

# 8. sort(key=None, reverse=False): Ordena os itens da lista. O parâmetro 'key' pode ser usado para especificar uma função de ordenação.
#    Exemplo: lista.sort() ordena a lista em ordem crescente.

# 9. reverse(): Inverte a ordem dos elementos na lista.
#    Exemplo: lista.reverse() inverte a ordem dos elementos da lista.

# 10. copy(): Retorna uma cópia superficial da lista.
#     Exemplo: nova_lista = lista.copy() cria uma cópia da lista original.

# 11. clear(): Remove todos os itens da lista.
#     Exemplo: lista.clear() remove todos os elementos da lista, deixando-a vazia.

# 12. len(lista): Retorna o número de itens na lista (não é um método, mas uma função embutida).
#     Exemplo: len(lista) retorna o número de elementos na lista.

# 13. list(iterable): Converte um iterável em uma lista (não é um método, mas uma função embutida).
#     Exemplo: lista_nova = list('abc') cria uma lista ['a', 'b', 'c'].

# Esses são os principais métodos e funções para manipulação de listas em Python.