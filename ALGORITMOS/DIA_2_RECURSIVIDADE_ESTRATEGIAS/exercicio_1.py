# Crie um algoritmo não recursivo para contar quantos
# números pares existem em uma sequência numérica (1 a n).


def count_even(n):
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            count += 1

    return count


if __name__ == "__main__":
    print(count_even(10))
