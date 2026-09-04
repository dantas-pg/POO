###Um relógio biométrico

class Relogio:
    def __init__(self, funcionario):
        self.funcionario = funcionario
        self.saldo_horas = 0
        self.esta_trabalhando = False

    def registrar_ponto(self):
        if not self.esta_trabalhando:
            self.esta_trabalhando = True
            print(f'Ponto de ENTRADA registrado para {self.funcionario}')
        else: 
            self.esta_trabalhando = False
            self.saldo_horas += 8
            print(f'Ponto de SAÍDA registrado para {self.funcionario}')

    def adcionar_hora_extra(self,horas):
        self.saldo_horas += horas

    def exibir_relatorio(self):
        status = 'Trabalhando' if self.esta_trabalhando else 'Em descanso'
        print(f'Funcionário: {self.funcionario} | Status: {status} | Saldo de horas: {self.saldo_horas}')

funcionario = Relogio('Arthur')
funcionario.registrar_ponto()
funcionario.adcionar_hora_extra(2)
funcionario.registrar_ponto()
funcionario.exibir_relatorio()