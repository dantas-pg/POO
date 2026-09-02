###Um relógio biométrico

class Relogio:
    def __init__(self, funcionario, saldo_horas, esta_trabalhando):
        self.funcionario = funcionario
        self.saldo_horas = 0
        self.esta_trabalhando = False

    def registrar_ponto(self):
        if self.esta_trabalhando