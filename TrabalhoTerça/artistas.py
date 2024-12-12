class Artistas:
    def __init__(self,id,nome,foto,obras,descricao,biografia):
        self.id = id
        self.nome = nome
        self.foto = foto
        self.obras = obras
        self.descricao = descricao
        self.biografia = biografia

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getFoto(self):
        return self.foto
        
    def getObras(self):
        return self.obras
    
    def getDescricao(self):
        return self.descricao
    
    def getBiografia(self):
        return self.biografia