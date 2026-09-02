###Funcionamento de um semáforo!

import time
class Semaforo:
    def __init__(self,cor_atual,tempo_restante):
      self.cor_atual ='vermelho'
      self.tempo_restante = 10

    def exibirTempo(self):
       print(f'A cor atual é {self.cor_atual.upper()} / Restam: {self.tempo_restante} segundos')

    def iniciarContagem(self):
        while self.tempo_restante > 0:
           self.exibirTempo()
           time.sleep(1)
           self.tempo_restante -= 1

        self.trocarCor()

    def trocarCor(self):
        if self.cor_atual == 'vermelho':
            self.cor_atual = 'verde'
            self.tempo_restante = 10
        elif self.cor_atual == 'verde':
            self.cor_atual = 'amarelo'
            self.tempo_restante = 3
        elif self.cor_atual == 'amarelo':
            self.cor_atual = 'vermelho'
            self.tempo_restante = 10

meu_semaforo = Semaforo('vermelho', 10)

while True:
    meu_semaforo.iniciarContagem()
