class Leiloes:
    def __init__(self, id, obra, lance_inicial, encerramento):
        self.id = id
        self.obra = obra
        self.lance_inicial = lance_inicial
        self.encerramento = encerramento
    
    def getId(self):
        return self.id
    
    def getObra(self):
        return self.obra
    
    def getLance_inicial(self):
        return self.lance_inicial
    
    def getEncerramento(self):
        return self.encerramento