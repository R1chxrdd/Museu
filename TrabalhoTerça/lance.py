class Lance:
    def __init__(self, id, nome,valor, usuario, obra, encerramento):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.usuario = usuario
        self.obra = obra
        self.encerramento = encerramento

    def getId(self):
        return self.id
    
    def getNome(self):
        return self.nome
    
    def getValor(self):
        return self.valor
    
    def getUsuario(self):
        return self.usuario
    
    def getObra(self):
        return self.obra
    
    def getEncerramento(self):
        return self.encerramento