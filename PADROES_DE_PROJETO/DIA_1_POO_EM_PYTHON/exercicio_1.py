# Crie a classe TV
# Atributos:

# volume - será inicializado com um valor de 50 e só pode estar entre 0 e 99;

# canal - será inicializado com um valor de 1 e só pode estar entre 1 e 99;

# tamanho - será inicializado com o valor do parâmetro;

# ligada - será inicializado com o valor de False, pois está inicialmente
# desligado.

# Todos os atributos devem ser privados.

# Métodos:

# aumentar_volume - aumenta o volume de 1 em 1 até o máximo de 99;

# diminuir_volume - diminui o volume de 1 em 1 até o mínimo de 0;

# modificar_canal - altera o canal de acordo com o parâmetro recebido e deve
# lançar uma exceção (ValueError) caso o valor esteja fora dos limites;

# ligar_desligar - alterna o estado da TV entre ligado e desligado (True/False)


class TV:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__volume = 50
        self.__canal = 1
        self.__ligada = False

    def tamanho(self):
        return f"O tamanho da TV é de {self.__tamanho} polegadas"

    def volume(self):
        return f"Volume atual: {self.__volume}"

    def canal(self):
        return f"Canal atual: {self.__canal}"

    def ligada(self):
        if self.__ligada:
            return "A TV está ligada"
        else:
            return "A está delsigada"

    def volume_up(self):
        if self.__volume < 100:
            self.__volume += 1
            return "Aumentar volume"

    def volume_down(self):
        if self.__volume > 1:
            self.__volume -= 1
            return "Diminuir volume"

    def change_channel(self, channel):
        if channel not in range(1, 99):
            raise ValueError
        else:
            self.__canal = channel
            return "Canal trocado"

    def turn_on_and_off(self):
        if self.__ligada:
            self.__ligada = False
            return "Desligando TV"
        else:
            self.__ligada = True
            return "Ligando TV"


toshiba = TV(32)

print(toshiba.canal())
print(toshiba.change_channel(5))
print(toshiba.canal())
print(toshiba.volume())
print(toshiba.volume_up())
print(toshiba.volume())
