import requests
from bs4 import BeautifulSoup as soup
import pandas as pd

def buscaSite(website):
    page_soup = "Erro"
    try:
        htmlContent = requests.get(website)
        t = htmlContent.text
        page_soup = soup (t, "html.parser")      
        return page_soup 
    except:
        return page_soup
        pass

websites = []
arrayIntermediario = []
newDf = pd.DataFrame()

nome_ficheiro = 'ludopedia.csv'

for x in range(1, 54):
    site = "https://www.ludopedia.com.br/ranking?pagina=" + str (x)
    page_soup = buscaSite (site)
    lista = page_soup.findAll ("div",{"class":"media-body"})
    for item in lista:
        if item.text.find ('R$') >= 0:
            continue
        else:
            arrayIntermediario.append (item.find('a')['href'])
            trechoNotas = item.findAll("div",{"class":"rank-info"})
            try:
                notas = trechoNotas[0].findAll('b')
            except:
                continue
            arrayIntermediario.append(notas[0].text) #notaRank
            arrayIntermediario.append(notas[1].text) #media
            arrayIntermediario.append(notas[2].text) #numAvaliacoes
            websites.append (arrayIntermediario)
            arrayIntermediario = []
        
for website in websites:
    print (website)
    notaRank = website[1]
    notaMedia = website [2]
    numAvaliacoes = website [3]
    page_soup = buscaSite (website[0])
    infos = page_soup.findAll ("div",{"class":"jogo-top-main"})
    print (infos)
    nome = infos[0].find('a').text
    print (nome)
    ano = infos[0].find('span',{'class':" text-xs"}).text
    detalhes = infos[0].ul.findAll ('li')
    for info in detalhes:
            
            if info.text.find('Idade') >= 0:
                idade = info.text.replace("Idade", "")
                
            elif info.text.find('min') >= 0:
                tempo = info.text
                
            elif info.text.find('jogadores') >= 0:
                jogadores = info.text
                
    detalhes2 = infos[0].findAll('span',{'class':"info-span text-sm"})
    for info in detalhes2:
            
            if info.text.find('Designer') == 0:
                designer = info.text
                head, sep, designer = designer.partition(':')
                
            elif info.text.find('Artista') == 0:
                artista = info.text
                head, sep, artista = artista.partition(':')     
                
            elif info.text.find('Editora') == 0:
                editora_brasileira = info.text    
                head, sep, editora_brasileira = editora_brasileira.partition(':')
                editoraBrasileira, sep, tail  = editora_brasileira.partition(',')
                             
    try:    
        editoraBrasileira = page_soup.findAll ("h4",{"class":"mar-top-no"})[0].text
    except:
        pass
    
    acaoProgramada = acaoSimultanea = alocacaoTrabalhadores = apostas = atuacao = blefe = campanhaDirigida = cantar = 0
    cercoArea = colecionarComponentes = colocacaoPecas = construcaoModelo = construcaoPecas = construcaoRotas = 0
    controleArea = cooperativo = deducao = desenhar = desenharLapis = eliminacaoJogadores = especulacaoFinanceira = 0
    forceSorte = gestaoMao = impulsoArea = diferentesHabilidades = jogoEquipe = leilao = linhaTempo = marcadoresHexagonos = 0
    memoria = mercadoAcoes = movimentoArea = movimentoGrades = pontoPonto = narracaoHistorias = negociacao = 0
    fasesVariavel = papelCaneta = pedraPapel = pegarEntregar = posicionamentoSecreto = reconhecimentoPadrao = 0
    rolagemDados = rolarMover = rpg = selecaoCartas = simulacao = pontosAcao = sistemaImpulsos = tabuleiroModular = 0
    tempoReal = tomaEssa = truques = votacao = 0
    
    adulto = animais = anime = arte = aventura = ciencias = civilizacao = culturaAfricana = culturaBrasileira = 0
    culturaOriental = culturaPop = economia = educacional = esportes = fantasia = faroeste = ficcaoCientifica = 0
    gastronomia = guerra = historia = horror = humor = literatura = artesMarciais = medieval = meioAmbiente = 0
    mitologia = piratas = policial = politica = preHistorico = quadrinhos = religiao = videoGame = transportes = vikings = 0
    
    quatrox = campanha = colecionavel = dungeonCrawler = estrategiaAbstrata = expansao = imprima = aplicativo = 0
    jogoAssimetrico = jogoCartas = jogoDados = jogoEntrada = jogoGuerra = jogoFestivo = legacy = livroJogo = 0
    minaturas = quebraCabeca = trivia = miniaturas = 0
    
    o = page_soup.findAll ("div",{"class":"mar-btm bg-gray-light pad-all"})
    mecanicas = o[0].findAll ("a",{"class":"text-primary"})
    for mecanica in mecanicas:
        #MECANICAS         
        if mecanica.text.find('Ação / Movimento Programado') == 0:
            acaoProgramada = 1
        elif mecanica.text.find('Ação Simultânea') == 0:
            acaoSimultanea = 1
        elif mecanica.text.find('Alocação de Trabalhadores') == 0:
            alocacaoTrabalhadores = 1
        elif mecanica.text.find('Apostas') == 0:
            apostas = 1
        elif mecanica.text.find('Atuação') == 0:
            atuacao = 1
        elif mecanica.text.find('Blefe') == 0:
            blefe = 1
        elif mecanica.text.find('Campanha/ Batalhas Dirigidas por Cartas') == 0:
            campanhaDirigida = 1
        elif mecanica.text.find('Cantar') == 0:
            cantar = 1
        elif mecanica.text.find('Cerco de Área') == 0:
            cercoArea = 1
        elif mecanica.text.find('Colecionar Componentes') == 0:
            colecionarComponentes = 1
        elif mecanica.text.find('Colocação de Peças') == 0:
            colocacaoPecas = 1
        elif mecanica.text.find('Construção a partir de Modelo') == 0:
            construcaoModelo = 1
        elif mecanica.text.find('Construção de Baralho/Peças') == 0:
            construcaoPecas = 1
        elif mecanica.text.find('Construção de Rotas') == 0:
            construcaoRotas = 1
        elif mecanica.text.find('Controle/Influência de Área') == 0:
            controleArea = 1
        elif mecanica.text.find('Cooperativo') == 0:
            cooperativo = 1
        elif mecanica.text.find('Dedução') == 0:
            deducao = 1
        elif mecanica.text.find('Desenhar') == 0:
            desenhar = 1
        elif mecanica.text.find('Desenhar Rota com Lápis') == 0:
            desenharLapis = 1
        elif mecanica.text.find('Eliminação de Jogadores') == 0:
            eliminacaoJogadores = 1
        elif mecanica.text.find('Especulação Financeira') == 0:
            especulacaoFinanceira = 1
        elif mecanica.text.find('Force sua sorte') == 0:
            forceSorte = 1
        elif mecanica.text.find('Gestão de Mão') == 0:
            gestaoMao = 1
        elif mecanica.text.find('Impulso de Área') == 0:
            impulsoArea = 1
        elif mecanica.text.find('Jogadores com Diferentes Habilidades') == 0:
            diferentesHabilidades = 1
        elif mecanica.text.find('Jogo em Equipe') == 0:
            jogoEquipe = 1
        elif mecanica.text.find('Leilão') == 0:
            leilao = 1
        elif mecanica.text.find('Linha de Tempo') == 0:
            linhaTempo = 1
        elif mecanica.text.find('Marcadores e Hexágonos') == 0:
            marcadoresHexagonos = 1
        elif mecanica.text.find('Memória') == 0:
            memoria = 1
        elif mecanica.text.find('Mercado de Ações') == 0:
            mercadoAcoes = 1
        elif mecanica.text.find('Movimento de Área') == 0:
            movimentoArea = 1
        elif mecanica.text.find('Movimento em Grades') == 0:
            movimentoGrades = 1
        elif mecanica.text.find('Movimento Ponto-a-Ponto') == 0:
            pontoPonto = 1
        elif mecanica.text.find('Narração de Histórias') == 0:
            narracaoHistorias = 1
        elif mecanica.text.find('Negociação') == 0:
            negociacao = 1
        elif mecanica.text.find('Ordem de Fases Variável') == 0:
            fasesVariavel = 1
        elif mecanica.text.find('Papel e Caneta') == 0:
            papelCaneta = 1
        elif mecanica.text.find('Pedra, Papel e Tesoura') == 0:
            pedraPapel = 1
        elif mecanica.text.find('Pegar e Entregar') == 0:
            pegarEntregar = 1
        elif mecanica.text.find('Posicionamento Secreto') == 0:
            posicionamentoSecreto = 1
        elif mecanica.text.find('Reconhecimento de Padrão') == 0:
            reconhecimentoPadrao = 1
        elif mecanica.text.find('Rolagem de Dados') == 0:
            rolagemDados = 1
        elif mecanica.text.find('Rolar e Mover') == 0:
            rolarMover = 1
        elif mecanica.text.find('RPG') == 0:
            rpg = 1
        elif mecanica.text.find('Seleção de Cartas') == 0:
            selecaoCartas = 1
        elif mecanica.text.find('Simulação') == 0:
            simulacao = 1
        elif mecanica.text.find('Sistema de Pontos de Ação') == 0:
            pontosAcao = 1 
        elif mecanica.text.find('Sistema por Impulsos') == 0:
            sistemaImpulsos = 1
        elif mecanica.text.find('Tabuleiro Modular') == 0:
            tabuleiroModular = 1
        elif mecanica.text.find('Tempo real') == 0:
            tempoReal = 1
        elif mecanica.text.find('Toma essa') == 0:
            tomaEssa = 1
        elif mecanica.text.find('Vazas/Truques') == 0:
            truques = 1
        elif mecanica.text.find('Votação') == 0:
            votacao = 1
        #TEMAS
        elif mecanica.text.find('Adulto') == 0:
            adulto = 1
        elif mecanica.text.find('Animais') == 0:
            animais = 1
        elif mecanica.text.find('Anime / Manga') == 0:
            anime = 1
        elif mecanica.text.find('Arte') == 0:
            arte = 1
        elif mecanica.text.find('Aventura') == 0:
            aventura = 1
        elif mecanica.text.find('Ciências') == 0:
            ciencias = 1
        elif mecanica.text.find('Civilização') == 0:
            civilizacao = 1
        elif mecanica.text.find('Cultura Africana') == 0:
            culturaAfricana = 1
        elif mecanica.text.find('Cultura Brasileira') == 0:
            culturaBrasileira = 1
        elif mecanica.text.find('Cultura Oriental') == 0:
            culturaOriental = 1
        elif mecanica.text.find('Cultura Pop ou Geek') == 0:
            culturaPop = 1
        elif mecanica.text.find('Economia / Produção') == 0:
            economia = 1
        elif mecanica.text.find('Educacional') == 0:
            educacional = 1
        elif mecanica.text.find('Esportes') == 0:
            esportes = 1
        elif mecanica.text.find('Fantasia') == 0:
            fantasia = 1
        elif mecanica.text.find('Faroeste') == 0:
            faroeste = 1 
        elif mecanica.text.find('Ficção Científica') == 0:
            ficcaoCientifica = 1
        elif mecanica.text.find('Gastronomia') == 0:
            gastronomia = 1
        elif mecanica.text.find('Guerra') == 0:
            guerra = 1
        elif mecanica.text.find('História') == 0:
            historia = 1
        elif mecanica.text.find('Horror') == 0:
            horror = 1 
        elif mecanica.text.find('Humor') == 0:
            humor = 1
        elif mecanica.text.find('Literatura') == 0:
            literatura = 1
        elif mecanica.text.find('Luta / Artes Marciais') == 0:
            artesMarciais = 1
        elif mecanica.text.find('Medieval') == 0:
            medieval = 1
        elif mecanica.text.find('Meio Ambiente') == 0:
            meioAmbiente = 1
        elif mecanica.text.find('Mitologia') == 0:
            mitologia = 1
        elif mecanica.text.find('Piratas') == 0:
            piratas = 1
        elif mecanica.text.find('Policial') == 0:
            policial = 1
        elif mecanica.text.find('Política') == 0:
            politica = 1
        elif mecanica.text.find('Pré-Histórico') == 0:
            preHistorico = 1
        elif mecanica.text.find('Quadrinhos') == 0:
            quadrinhos = 1
        elif mecanica.text.find('Religião') == 0:
            religiao = 1
        elif mecanica.text.find('Tema de Video Game') == 0:
            videoGame = 1
        elif mecanica.text.find('Transportes') == 0:
            transportes = 1
        elif mecanica.text.find('Vikings') == 0:
            vikings = 1
        #CATEGORIAS
        elif mecanica.text.find('4x') == 0:
            quatrox = 1
        elif mecanica.text.find('Campanha') == 0:
            campanha = 1
        elif mecanica.text.find('Colecionável') == 0:
            colecionavel = 1
        elif mecanica.text.find('Dungeon Crawler') == 0:
            dungeonCrawler = 1
        elif mecanica.text.find('Estratégia Abstrata') == 0:
            estrategiaAbstrata = 1
        elif mecanica.text.find('Expansão ou Suplemento') == 0:
            expansao = 1
        elif mecanica.text.find('Imprima e Jogue') == 0:
            imprima = 1
        elif mecanica.text.find('Integrado com Aplicativo') == 0:
            aplicativo = 1
        elif mecanica.text.find('Jogo Assimétrico') == 0:
            jogoAssimetrico = 1
        elif mecanica.text.find('Jogo de Cartas') == 0:
            jogoCartas = 1
        elif mecanica.text.find('Jogo de Dados') == 0:
            jogoDados = 1
        elif mecanica.text.find('Jogo de Entrada') == 0:
            jogoEntrada = 1
        elif mecanica.text.find('Jogo de Guerra') == 0:
            jogoGuerra = 1
        elif mecanica.text.find('Jogo Festivo') == 0:
            jogoFestivo = 1
        elif mecanica.text.find('Legacy') == 0:
            legacy = 1
        elif mecanica.text.find('Livro-jogo') == 0:
            livroJogo = 1
        elif mecanica.text.find('Miniaturas') == 0:
            miniaturas = 1
        elif mecanica.text.find('Quebra-Cabeça') == 0:
            quebraCabeca = 1
        elif mecanica.text.find('Trivia') == 0:
            trivia = 1
     
    linha = pd.DataFrame({'Link': [website], 'Nome': [nome], 'Ano de Lançamento': [ano], 'Nota Rank' : [notaRank], 
                          'Nota Média' : [notaMedia], '# Avaliações' : [numAvaliacoes], 'Faixa Etária': [idade],
                          'Tempo de Jogo':[tempo], '# de Jogadores': [jogadores], 'Designer' : [designer], 
                          'Artista': [artista], 'Editora Brasileira' : [editoraBrasileira],
                          'Ação / Movimento Programado' : [acaoProgramada], 'Ação Simultânea' : [acaoSimultanea],
                          'Alocação de Trabalhadores' : [alocacaoTrabalhadores], 'Apostas' : [apostas], 'Atuação' : [atuacao],
                          'Blefe' : [blefe], 'Campanha/ Batalhas Dirigidas por Cartas' : [campanhaDirigida], 'Cantar' : [cantar],
                          'Cerco de Área' :[cercoArea], 'Colecionar Componentes' :[colecionarComponentes], 
                          'Colocação de Peças' : [colocacaoPecas], 'Construção a partir de Modelo' : [construcaoModelo],
                          'Construção de Baralho/Peças' : [construcaoPecas], 'Construção de Rotas' : [construcaoRotas],
                          'Controle/Influência de Área' : [controleArea], 'Cooperativo' : [cooperativo], 'Dedução' : [deducao],
                          'Desenhar' : [desenhar], 'Desenhar Rota com Lápis' : [desenharLapis], 
                          'Eliminação de Jogadores' :[eliminacaoJogadores], 'Especulação Financeira' : [especulacaoFinanceira],
                          'Force sua sorte' : [forceSorte], 'Gestão de Mão' : [gestaoMao], 'Impulso de Área' : [impulsoArea],
                          'Jogadores com Diferentes Habilidades' : [diferentesHabilidades], 'Jogo em Equipe' : [jogoEquipe],
                          'Leilão' : [leilao], 'Linha de Tempo' : [linhaTempo], 'Marcadores e Hexágonos' : [marcadoresHexagonos],
                          'Memória' : [memoria], 'Mercado de Ações' : [mercadoAcoes], 'Movimento de Área' : [movimentoArea],
                          'Movimento em Grades' : [movimentoGrades], 'Movimento Ponto-a-Ponto' : [pontoPonto],
                          'Narração de Histórias' : [narracaoHistorias], 'Negociação' : [negociacao], 
                          'Ordem de Fases Variável' : [fasesVariavel], 'Papel e Caneta' : [papelCaneta],
                          'Pedra, Papel e Tesoura' : [pedraPapel], 'Pegar e Entregar' : [pegarEntregar], 
                          'Posicionamento Secreto' : [posicionamentoSecreto], 'Reconhecimento de Padrão' : [reconhecimentoPadrao],
                          'Rolagem de Dados' : [rolagemDados], 'Rolar e Mover' : [rolarMover], 'RPG' : [rpg], 
                          'Seleção de Cartas' : [selecaoCartas], 'Simulação' : [simulacao], 
                          'Sistema de Pontos de Ação' : [pontosAcao], 'Sistema por Impulsos' : [sistemaImpulsos], 
                          'Tabuleiro Modular' : [tabuleiroModular], 'Tempo real' : [tempoReal], 'Toma essa' : [tomaEssa],
                          'Vazas/Truques' : [truques], 'Votação' : [votacao], 'Adulto' : [adulto], 'Animais' :[animais], 
                          'Anime / Manga' : [anime], 'Arte' : [arte], 'Aventura' : aventura, 'Ciências':[ciencias], 
                          'Civilização' : [civilizacao], 'Cultura Africana' : [ culturaAfricana], 'Cultura Brasileira': [culturaBrasileira],
                          'Cultura Oriental' : [culturaOriental], 'Cultura Pop ou Geek' :[culturaPop], 
                          'Economia / Produção' : [economia], 'Educacional':[educacional], 'Esportes' : esportes, 
                          'Fantasia' : [fantasia], 'Faroeste' : [faroeste], 'Ficção Científica' : [ficcaoCientifica],
                          'Gastronomia' : [gastronomia], 'Guerra' : [guerra], 'História' : [historia], 'Horror' : [horror], 
                          'Humor' : humor, 'Literatura' : [literatura], 'Luta / Artes Marciais' : [artesMarciais], 
                          'Medieval' : [medieval], 'Meio Ambiente' : [meioAmbiente], 'Mitologia' : [mitologia],
                          'Piratas' : [piratas], 'Policial' : [policial], 'Política' : [politica], 'Pré-Histórico' : [preHistorico],
                          'Quadrinhos' : [quadrinhos], 'Religião' : [religiao], 'Tema de Video Game' : [videoGame], 
                          'Transportes' : [transportes], 'Vikings' : [vikings], '4x' : [quatrox], 'Campanha' : [campanha], 
                          'Colecionável' : [colecionavel], 'Dungeon Crawler' : [dungeonCrawler], 
                          'Estratégia Abstrata' : [estrategiaAbstrata], 'Expansão ou Suplemento':[expansao], 
                          'Imprima e Jogue' : [imprima], 'Integrado com Aplicativo' : [aplicativo], 
                          'Jogo Assimétrico' : [jogoAssimetrico], 'Jogo de Cartas' : [jogoCartas], 'Jogo de Dados':[jogoDados],
                          'Jogo de Entrada' : [jogoEntrada], 'Jogo de Guerra' : [jogoGuerra], 'Jogo Festivo' : [jogoFestivo],
                          'Legacy' : [legacy], 'Livro-jogo' : [livroJogo] , 'Miniaturas' : [miniaturas], 
                          'Quebra-Cabeça': [quebraCabeca], 'Trivia' : [trivia]})
    print (linha)
    print ("")
    
    newDf = newDf.append (linha)
              
newDf.to_csv('ludopediaDatabase.csv')
    
    
    
