# Em um software monitor, o qual verifica a resiliência de outro software,
# precisamos saber o tempo máximo que um software
# permaneceu sem instabilidades.
# Para isto, a cada hora é feito uma requisição ao sistema
# para verificamos se está tudo bem.
# Supondo um array que contenha os estados coletados por nosso software,
# calcule quanto tempo máximo que o servidor permaneceu sem instabilidades.
from itertools import groupby


def software_check(arr):
    result = []
    for value, group in groupby(arr):
        if value == 1:
            result.append(len(list(group)))

    return max(result)


print(software_check([1, 1, 1, 1, 0, 0, 1, 1]))
