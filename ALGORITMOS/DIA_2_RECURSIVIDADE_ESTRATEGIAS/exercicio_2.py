#  Transforme o algoritmo do exericio anterior em recursivo.

def recursive_count_even(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return 1 + recursive_count_even(n - 1)
    else:
        return recursive_count_even(n - 1)


if __name__ == "__main__":
    print(recursive_count_even(10))
