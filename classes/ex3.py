class Aluno:
    def __init__(self, nome, n1, n2, n3, n4):
        self.nome = nome
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4   
        self.media = 0

    def calcular_media(self):
        self.media = (self.n1 * 2 + self.n2*3 + self.n3*4 + self.n4*1)/10

    def status(self):
        if self.media > 7:
            return('Aluno aprovado')
        elif self.media < 5:
            return('Aluno reprovado')
        else: 
            return('Aluno em exame')
        
    def exibir_boletim(self):

        print(f'Aluno: {self.nome} | Média: {self.media} | Status: {self.status()}')

arthur = Aluno('Arthur', 5, 6.9, 9, 1)
arthur.calcular_media()
arthur.exibir_boletim()