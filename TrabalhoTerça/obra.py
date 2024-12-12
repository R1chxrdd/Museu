class Obra:
    def __init__(self, id, nome, categoria, imagem, artista, artista_id, data_criacao, descricao, exibicao,comentario_lance,comentario_lance2,encerramento):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.imagem = imagem
        self.artista = artista
        self.artista_id = artista_id
        self.data_criacao = data_criacao
        self.descricao = descricao
        self.exibicao = exibicao
        self.comentario_lance = comentario_lance
        self.comentario_lance2 = comentario_lance2
        self.encerramento = encerramento
    
    def getId(self):
        return self.id
    
    def getNome(self):
        return self.nome
    
    def getCategoria(self):
        return self.categoria
    
    def getImagem(self):
        return self.imagem
    
    def getArtista(self):
        return self.artista
    
    def getArtistaId(self):
        return self.artista_id
    
    def getDataCriacao(self):
        return self.data_criacao
    
    def getDescricao(self):
        return self.descricao
    
    def getExibicao(self):
        return self.exibicao
        
    def getComentarioLance(self):
        return self.comentario_lance
    
    def getComentarioLance2(self):
        return self.comentario_lance2
    
    def getEncerramento(self):
        return self.encerramento