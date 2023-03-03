# Definição da string a ser invertida
string_original = "Exemplo de string a ser invertida"

# Criação de uma lista com os caracteres da string original
lista_caracteres = list(string_original)

# Inversão dos caracteres da lista
for i in range(len(lista_caracteres) // 2):
    j = len(lista_caracteres) - 1 - i
    lista_caracteres[i], lista_caracteres[j] = lista_caracteres[j], lista_caracteres[i]

# Criação de uma nova string a partir da lista invertida
string_invertida = "".join(lista_caracteres)

# Exibição da string invertida
print(string_invertida)