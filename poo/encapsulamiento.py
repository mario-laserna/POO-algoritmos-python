class CasillaDeVotación:
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self.__region = None

    # manera de crear un getter
    @property
    def region(self):
        return self.__region

    # manera de crear un setter
    @region.setter
    def region(self, value):
        if value in self._pais:
            self.__region = value
        else:
            raise ValueError(f'La region {value} no es valida en {self._pais}')


if __name__ == '__main__':
    casilla = CasillaDeVotación(123, ['Bogota', 'Manizales'])
    print(casilla.region)
    # print(casilla.__region) esto no es posible porque el metodo está privado

    casilla.region = 'Bogota'
    print(casilla.region)

    casilla.region = 'Pereira'
    print(casilla.region)
