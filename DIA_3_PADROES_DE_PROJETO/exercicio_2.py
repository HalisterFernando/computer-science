# Defina uma classe Estatistica que calcule média, mediana e moda de uma lista
# de números.


class Estatistica:
    @staticmethod
    def media(list):
        sum_of_elements = 0
        for el in list:
            sum_of_elements += el

        return sum_of_elements / len(list)

    @staticmethod
    def mediana(list):
        is_even = True if len(list) % 2 == 0 else False

        if is_even:
            index = len(list) // 2
            return (list[index] + list[index + 1]) / 2
        else:
            index = (len(list) + 1) // 2
            return list[index] // 100

    @staticmethod
    def moda(list):
        number_dict = {}
        for el in list:
            if el not in number_dict:
                number_dict[el] = 1
            else:
                number_dict[el] += 1

        return max(number_dict, key=number_dict.get)


players_age = [28, 27, 19, 23, 21]
shoes_number = [34, 39, 36, 35, 37, 40, 36, 38, 36, 38, 41]
students_height = [154, 167, 150, 165, 175, 169, 160, 155, 178]
some_data = [32, 27, 15, 44, 15, 32]

players_statistics = Estatistica()
shoes_moda = Estatistica()
students_mediana = Estatistica()
data_mediana = Estatistica()

print(players_statistics.media(players_age))
print(shoes_moda.moda(shoes_number))
print(students_mediana.mediana(students_height))
print(data_mediana.mediana(some_data))
