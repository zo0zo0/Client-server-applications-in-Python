class PortError(Exception):
    def __str__(self):
        return 'В качестве порта может быть указано только число в диапазоне от 1024 до 65535.'


class IncorrectDataRecivedError(Exception):
    def __str__(self):
        return 'Принято некорректное сообщение от удалённого компьютера.'