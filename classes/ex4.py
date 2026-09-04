#A classe deve ter: -numero, plano de internet_mb, saldo_reais
#Deve ter os seguintes métodos: recarregar(valor), fazer ligação(minutos), comprar pacote de internet, exibir extrato()

class CelularPrePago:
    def __init__(self, numero):
        self.numero = numero
        self.plano_mb = 0 
        self.saldo_reais = 0.0

    def recarregar(self, valor):
        self.saldo_reais = self.saldo_reais + valor
        print(f'{valor}reais foram creditados na sua conta')

    def fazer_ligacao(self, minutos):
        total = minutos * 0.5
        if self.saldo_reais >= total:
            self.saldo_reais -= total
            print(f'Sua ligação foi concluída, restam: {self.saldo_reais}')
        else: 
            print(f'Saldo insuficiente, restam: {self.saldo_reais}')

    def comprar_internet(self, plano_mb):
        valor = plano_mb*0.05
        if self.saldo_reais >= valor:
            self.plano_mb += plano_mb
            self.saldo_reais -= valor
            print(f'Sua recarga foi feita com sucesso, restam: {self.saldo_reais}')
        else:
            print('Saldo insuficiente, restam{self.saldo_reais}')
    def exibir_extrato(self):
        print(f'{self.numero}\n Restam: {self.plano_mb} mb \n Restam:{self.saldo_reais}')

Arthur = CelularPrePago(83987208467)
Arthur.recarregar(50)
Arthur.fazer_ligacao(10)
Arthur.comprar_internet(200)
Arthur.exibir_extrato()