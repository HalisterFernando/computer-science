#  Crie um algoritmo recursivo que
# encontre, em uma lista, o maior número inteiro.


def find_greatest_number_aux(list, len):
    if len == 1:
        return list[0]
    else:
        greatest_number = find_greatest_number_aux(list, len - 1)
        if greatest_number > list[len - 1]:
            return greatest_number
        else:
            return list[len - 1]


def greatest_number(list):
    size = len(list)
    return find_greatest_number_aux(list, size)


print(greatest_number([1, 21, 300, 4, 57]))
