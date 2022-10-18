# 🚀 Exercício 4: Crie uma função que receba uma lista de nomes
# e retorne o nome com a maior quantidade de caracteres.


def find_greatest_name(list):
    sorted_names = sorted(list, key=len)
    return print(sorted_names[-1])


list = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]


find_greatest_name(list)
