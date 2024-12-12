class Categorias:
    def __init__(self, id, nome, obras):
        self.id = id
        self.nome = nome
        self.obras = obras
    
    def getId(self):
        return self.id
    
    def getNome(self):
        return self.nome
    
    def getObras(self):
        return self.obras