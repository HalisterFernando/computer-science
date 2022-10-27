# Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1,
# imprima na tela um quadrado feito de asteriscos de lado de tamanho n.


def asterisc_form(number):
    asterisc_quantity = number * "*"
    for asterisc in asterisc_quantity:
        print(asterisc_quantity)


asterisc_form(5)
