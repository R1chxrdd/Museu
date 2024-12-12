from flask import Flask, render_template
from artistas import Artistas
from exibicoes import Exibicoes
from lance import Lance
from leiloes import Leiloes
from obra import Obra
from categorias import Categorias

app = Flask(__name__) 


obra1 = Obra(1, 'Monalisa', 'Pintura', 'monalisa.jpg', 'Armando J.', 1, '20/10/1999', 'A "Monalisa," também conhecida como "La Gioconda," é uma das pinturas mais icônicas do mundo. Este retrato de uma mulher com um sorriso enigmático foi pintado em 1999 e é atualmente exibido no Museu do Louvre, em Paris. A pintura é famosa pela expressão ambígua da Monalisa, seu olhar misterioso que parece seguir os espectadores em qualquer direção que se movam, e pelo uso inovador do sfumato, uma técnica que cria transições suaves entre as cores e tonalidades, dando uma sensação de profundidade e volume.','Exibição','Ricardo: Gostei muito da obra, considero o melhor pintor que ja existiu','Amanda: Eu fiquei completamente fascinada pela "Monalisa". A sutileza do sorriso e o olhar que parece seguir você são realmente hipnotizantes.','Data do comentário: 25/11/2024')

obra2 = Obra(2, 'O Grito', 'Pintura', 'ogrito.webp', 'Armando J.', 1, '05/04/1993','"O Grito" é frequentemente interpretado como uma manifestação visual das emoções internas do ser humano, capturando a essência do medo e da vulnerabilidade. A obra tem sido analisada sob várias perspectivas, desde questões existenciais até reflexões sobre a condição humana. Seu impacto duradouro continua a inspirar e intrigar espectadores em todo o mundo, tornando-se um símbolo universal da angústia moderna.','Exibição','Ronaldo: Gostei muito da obra, fiquei intrigado para ver pessoalmente','Luiza: Fiquei profundamente tocada pela obra. A angústia capturada na expressão do personagem é incrivelmente poderosa.','Data do comentário: 25/11/2024')

obra3 = Obra(3, 'Blue', 'Pintura', 'aazul.jpg', 'Armando J.', 1, '09/01/2010', '"Blue" é uma obra conhecida por seu impacto emocional e sua habilidade de evocar sentimentos profundos de introspecção e serenidade. A peça retrata uma vastidão de tons azuis, desde os mais suaves e tranquilos até os mais profundos e escuros, criando uma sensação de imersão em um oceano de emoções.','Exibição','Amilton: Não gosto de obras abstratas, mas essa eu gostei!','Matheus: Fiquei impressionado com "Blue". A vastidão de tons azuis e a figura contemplativa criam uma sensação de serenidade e introspecção. A obra realmente evoca emoções profundas e me deixou refletindo por um bom tempo.','Data do comentário: 25/11/2024')

obra4 = Obra(4, 'O Beijo', 'Escultura', 'obeijo.webp', 'Mario R.', 1,'19/07/2001','"O Beijo" é uma escultura que captura a essência do amor e da união em um momento eterno. A peça retrata duas figuras entrelaçadas em um abraço apaixonado, seus corpos esculpidos com uma fluidez que sugere um movimento contínuo e harmonioso. As formas suaves e os detalhes delicados das expressões faciais transmitem uma intimidade profunda, enquanto as mãos e os braços dos amantes se fundem, simbolizando a conexão inquebrantável entre eles','Leilão',"Amanda ofertou por 50 Mil a obra",'Lance inicial: 5 mil','Data do lance: 25/11/2024')

obra5 = Obra(5, 'As Meninas', 'Escultura', 'asmeninaass.jpg', 'Mario R.',1,'30/10/1999','"As Meninas" é uma escultura que celebra a inocência e a alegria da infância. A peça retrata um grupo de três meninas, capturadas em um momento de brincadeira e camaradagem. As figuras são esculpidas com detalhes cuidadosos, mostrando expressões de felicidade e interação espontânea. Seus vestidos fluem suavemente, dando a impressão de movimento e liberdade.','Leilão','Rafaela ofertou por 500 Mil a obra','Lance inicial: 100 mil','Data do lance: 25/11/2024')

obra6 = Obra(6, 'Abaporu', 'Escultura', 'abaparu.jpg', 'Mario R.',1,'22/07/2005','"Abaporu" é uma escultura que explora a identidade cultural e o espírito de transformação. A peça retrata uma figura humana de proporções exageradas, com uma grande cabeça e membros alongados, em uma pose introspectiva. Os traços da figura são marcantes e únicos, evocando tanto a força quanto a vulnerabilidade.','Leilão','Rafael ofertou por 1 Milhão a obra', 'Lance inicial: 500 mil',' Data do lance: 25/11/2024')



artista1 = Artistas(1, 'Armando J.', 'mich.webp', 'Monalisa, o grito, blue','Um pintor talentoso nascido no Brasil, Armando J. é conhecido por suas vibrantes paisagens urbanas e toques surrealistas. Com formação em Artes Visuais pela Universidade de São Paulo, ele se destacou no cenário artístico nacional. Suas obras frequentemente capturam a energia e a diversidade da vida cotidiana, sempre com um jogo intrigante de cores e formas.','Armando J., nascido no Brasil, é um pintor talentoso reconhecido por suas vibrantes paisagens urbanas e toques surrealistas. Desde jovem, Armando demonstrou um fascínio pela arte, frequentemente desenhando e pintando em seus cadernos escolares. Seu talento precoce foi notado por seus professores, que o incentivaram a seguir uma formação artística. Ele se formou em Artes Visuais pela Universidade de São Paulo, onde aprimorou suas habilidades e começou a explorar sua própria linguagem visual.'
)
artista2 = Artistas(2, 'Mario R.', 'leo.jpg', 'O Beijo, as meninas, Abaporu','Como escultor, Mario R. transforma materiais brutos em obras de arte que contam histórias profundas e emocionantes. Formado em Belas Artes pela Universidade Federal do Rio de Janeiro, ele é aclamado por sua habilidade de combinar elementos da arte popular com técnicas modernas. Suas esculturas exploram temas de identidade e cultura, muitas vezes refletindo a rica herança cultural do Brasil.','Mario R. é um escultor brasileiro aclamado por transformar materiais brutos em obras de arte que contam histórias profundas e emocionantes. Desde criança, Mario sempre se encantou com a possibilidade de criar algo novo a partir de materiais simples. Ele passava horas esculpindo em madeira e modelando argila, o que chamou a atenção de sua família e amigos. Motivado por essa paixão, decidiu estudar Belas Artes na Universidade Federal do Rio de Janeiro. Mario é um professor dedicado, compartilhando seus conhecimentos e inspirando a próxima geração de artistas.'
)


categoria_list = [
    Categorias(1, 'Pintura', obra1),
    Categorias(2, 'Pintura', obra2),
    Categorias(3, 'Pintura', obra3),
    Categorias(4, 'Escultura', obra4),
    Categorias(5, 'Escultura', obra5),
    Categorias(6, 'Escultura', obra6),
]

exibicao1 = Exibicoes(1,'Exibições' ,'Expressões da Humanidade', '21/11/2024', '25/11/2024','images/cores.webp' )
exibicao2 = Exibicoes(2, 'Exibições','A Arte da Escultura', '01/12/2024', '05/12/2024','images/escultura.webp' )
exibicoes = [exibicao1, exibicao2]


lance4 = Lance(4,'Ver Leiões' ,'10 mil', 'Pedro B.', obra4,'25/11/2024')
lance5 = Lance(5,'Ver Leiões' ,'1 milhão', 'Rafaela I.', obra5,'25/11/2024')
lance6 = Lance(6,'Ver Leiões','2 milhões', 'Queila T.', obra6,'25/11/2024')


leilao4 = Leiloes(4, obra4, '100 mil', 'Data de Encerramento: 25/11/2024')
leilao5 = Leiloes(5, obra5, '900 mil', '25/11/2024')
leilao6 = Leiloes(6, obra6, '1 milhão', '25/11/2024')



@app.route('/')
def home():
    return render_template('listagemobra.html', obras=[obra1, obra2, obra3, obra4, obra5, obra6], artistas=[artista1, artista2], exibicoes=[exibicao1], lance=[lance4])


@app.route('/obra/<int:obra_id>')
def detalhe_obra(obra_id):
    obra = next((o for o in [obra1, obra2, obra3, obra4, obra5, obra6] if o.getId() == obra_id), None)
    if obra is None:
        return "Obra não encontrada", 404
    return render_template(f'obra{obra_id}.html', obra=obra)


@app.route('/artistas/<int:artistas_id>')
def detalhe_artistas(artistas_id):
    artistas = next((o for o in [artista1, artista2] if o.getId() == artistas_id), None)
    if artistas is None:
        return "Artista não encontrado", 404
    obras_do_artista = [obra for obra in [obra1, obra2, obra3, obra4, obra5, obra6] if obra.getArtista() == artistas.getNome()]
    
    return render_template(f'artistas{artistas_id}.html', artista=artistas, obras=obras_do_artista)


def get_exibicao_by_id(exibicao_id):
    for exibicao in exibicoes:
        if exibicao.getId() == exibicao_id:
            return exibicao
    return None

@app.route('/exibicoes')
def lista_exibicoes():
    return render_template('exibicao.html', exibicoes=exibicoes)

@app.route('/detalhe_exibicao/<int:exibicao_id>')
def detalhe_exibicao(exibicao_id):
    exibicao = get_exibicao_by_id(exibicao_id)
    if exibicao:
        if exibicao_id == 1:
            return render_template('detalheexibicao.html', exibicao=exibicao, obra1=obra1, obra2=obra2, obra3=obra3)
        elif exibicao_id == 2:
            return render_template('detalheexibicao2.html', exibicao=exibicao, obra4=obra4, obra5=obra5, obra6=obra6)
    return "Exibição não encontrada", 404

@app.route('/leiloes')
def lista_lance():
    return render_template('leiloes.html', leiloes= Leiloes, obra4=obra4, obra5=obra5, obra6=obra6, leilao4=leilao4)

@app.route('/lance')
def lista_leiloes():
    return render_template('detalhelance.html', leiloes= Leiloes, obra1=obra1,obra2=obra2,obra3=obra3,obra4=obra4,obra5=obra5,obra6=obra6, leilao5=leilao5)


if __name__ == '__main__':
    app.run(debug=True)