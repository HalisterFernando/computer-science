# 🚀 Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.


def average_value(numbers):
    list_length = len(numbers)
    value = 0

    for number in numbers:
        value += number

    return print(value / list_length)


average_value([2, 3, 3, 5, 7, 10])
