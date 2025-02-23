# Criando uma tupla
minha_tupla = (1, 2, 3, "Python", 4.5)

# Acessando elementos de uma tupla
print("Primeiro elemento:", minha_tupla[0])  # Acessando o primeiro item (índice 0)
print("Último elemento:", minha_tupla[-1])  # Acessando o último item (índice -1)

# Tentando modificar um valor em uma tupla (isso vai gerar um erro, pois as tuplas são imutáveis)
# minha_tupla[0] = 10  # Vai gerar erro

# Desempacotando tupla
a, b, c, d, e = minha_tupla
print("\nDesempacotando a tupla:")
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
print("e =", e)

# Verificando o comprimento da tupla
print("\nComprimento da tupla:", len(minha_tupla))

# Usando tupla para armazenar dados heterogêneos
tupla_heterogenea = (100, "texto", [1, 2, 3])
print("\nTupla heterogênea:", tupla_heterogenea)

# Tuplas também podem ser aninhadas
tupla_aninhada = ((1, 2), (3, 4))
print("\nTupla aninhada:", tupla_aninhada)

# Contando a ocorrência de um item na tupla
print("\nNúmero de vezes que o valor 2 aparece na tupla:", minha_tupla.count(2))

# Encontrando o índice de um item na tupla
print("\nÍndice do valor 'Python' na tupla:", minha_tupla.index("Python"))
