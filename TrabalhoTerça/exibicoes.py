class Exibicoes:
    def __init__(self,id,nome,titulo,data_inicio,termino,foto):
        self.id = id
        self.nome = nome
        self.titulo = titulo
        self.data_inicio = data_inicio
        self.termino = termino
        self.foto = foto

    def getId(self):
        return self.id
    
    def getNome(self):
        return self.nome

    def getTitulo(self):
        return self.titulo
    
    def getData_inicio(self):
        return self.data_inicio
    
    def getTermino(self):
        return self.termino
    
    def getFoto(self):
        return self.foto