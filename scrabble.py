
#region TAD Casa

# O TAD imutável casa é usado para representar uma casa do tabuleiro de Scrabble.

# A representação escolhida para este TAD, pir ser imutável é um tuplo

# region Construtor
def cria_casa(lin, col):
    """
    recebe dois inteiros correspondentes à linha, lin, e coluna, col, e
    devolve a casa correspondente. O construtor verifica a validade dos seus argu-
    mentos, gerando um ValueError com a mensagem 'cria_casa: argumentos
    inválidos' caso os seus argumentos não sejam válidos.

    cria_casa: {int, int} -> {tuple}
    """
    if (
        not isinstance(lin, int)
        or not isinstance(col, int)
        or not 0 < lin <= 15
        or not 0 < col <= 15
    ):
        raise ValueError("cria_casa: argumentos inválidos")

    return (lin, col)

#endregion

# region Seletores
def obtem_col(casa):
    """
    Recebe uma casa e devolve a coluna asociada à casa

    obtem_coluna: {tuple} -> {int}
    """

    return casa[1]


def obtem_lin(casa):
    """
    Recebe uma casa e devolve a linha associada à casa

    obtem_lin: {tuple} -> {int}
    """

    return casa[0]

#endregion

# region Reconhecedor
def eh_casa(casa):
    """
    Verifica se o argumento é uma casa, devolvendo True se se o argumento for
    uma casa ou False caso contrário.

    eh_casa: {tuple} -> {bool}
    """

    # Ser um tuplo, representação escolhida
    if isinstance(casa, tuple):
        # Os tipos das coordenadas estarem corretos
        if isinstance(obtem_col(casa), int) and isinstance(obtem_lin(casa), int):
            # Estar dentro do tabuleiro
            if 1 <= obtem_col(casa) <= 15 and 1 <= obtem_lin(casa) <= 15:
                return True
    else:
        return False  # se nenhuma destas condições se verificar, então não é uma casa

#endregion

# region Teste
def casas_iguais(casa1, casa2):
    """
    Verifica se as casas fornecidas como argumento são iguais, verificando se ambas
    as coordenadas são idênticas entre as casas. Devolve True se as casas forem
    iguais e False caso contrário.

    casa_iguais: {casa, casa} -> {bool}
    """

    return (
        True
        if obtem_lin(casa1) == obtem_lin(casa2) and obtem_col(casa1) == obtem_col(casa2)
        else False
    )

#endregion

# region Transformadores
def casa_para_str(casa):
    """
    Devolve a cadeia de caracteres que representa a casa fornecida como argumento.

    casas_para_str: {casa} -> {str}
    """

    return str(casa).replace(" ", "")


def str_para_casa(cadeia):
    """
    Devolve a casa que é representada pela cadeia de carecters fornecida como argumento

    str_para_casa: {str} -> {tuple}
    """
    cadeia_coordenadas_casa = ""
    for caracter in cadeia:
        if not caracter in {"(", ")", " "}:
            cadeia_coordenadas_casa += "".join(caracter)
    coordenadas = cadeia_coordenadas_casa.split(",")

    casa = cria_casa(int(coordenadas[0]), int(coordenadas[1]))

    return casa

#endregion

# region Funções de alto Nível
def incrementa_casa(c, d, s):
    """
    Devolve a casa dum tabuleiro de Scrabble a seguir à casa fornecida como argumento
    na direção indicada e à distância s.

    incrementa_casa: {casa, str, int} -> {casa}
    """

    coluna_original = obtem_col(c)
    linha_original = obtem_lin(c)

    if d == "V":
        linha = linha_original + s
        coluna = coluna_original
    if d == "H":
        linha = linha_original
        coluna = coluna_original + s
    if 1 <= linha <= 15 and 1 <= coluna <= 15:
        return cria_casa(linha, coluna)
    else:
        return c

#endregion

#endregion


#region TAD Jogador

# O TAD jogador ´e usado para representar um jogador do jogo Scrabble, a sua pontua¸c˜ao
# e letras. Os jogadores podem ser humanos ou agentes.

#A representação escolhida para este TAD é um dicionário

# region Construtores
def cria_humano (nome):
    """
    Recebe uma cadeia de caracteres, não vazia, a representar
    o nome do jogador e devolve um jogador de Scrabble humano
    com 0 pontos e sem letras.
    
    cria_humano: {str} -> {dict}
    """
    
    if not isinstance(nome, str) or nome == '':
        raise ValueError('cria_humano: argumento inválido')
    
    return {'nome': nome, 'pontos': 0, 'letras': ''}

def cria_agente(nivel):
    """
    Recebe uma cadeia de caracteres a representar o nível do
    jogador ('FACIL', 'MEDIO' ou 'DIFICIL') e devolve um jogador
    de Scrabble agente com 0 pontos e sem letras.
    """
    
    if not isinstance(nivel, str) or nivel not in {'FACIL', 'MEDIO', 'DIFICIL'}:
        raise ValueError("cria_agente: argumento inválido")
    
    return {'nivel': nivel, 'pontos': 0, 'letras': ''}
#endregion

#region Seletores
def jogador_identidade (jogador):
    """
    Devolve o nome do jogador, caso este seja humano, ou o nível do jogador,
    caso este seja agente.
    
    jogador_identidade: {jogador} -> {str}
    """
    
    if 'nivel' in jogador: #Jogador agente
        return jogador['nivel']
    elif 'nome' in jogador: #Jogador humano
        return jogador['nome']
    
def jogador_pontos(jogador):
    """
    Devolve os pontos do jogador fornecido como argumento
    
    jogador_pontos: {jogador} -> {int}
    """
    
    return jogador['pontos']

def jogador_letras(jogador):
    """
    Devolve a cadeia de caracateres ordenada com todas as letras
    do jogador fornecido como argumento.
    
    jogador_letras: {jogador} -> {srtr}
    """
    
    return jogador['letras']
    
# endregion

# region Modificadores
def recebe_letra (jogador, letra):
    """
    Modifica destrutivamente o jogador fornecido como argumento,
    acrescentando a letra indicada às suas letras, e devolve o próprio jogador.
    
    recebe_letra: {jogador, str} -> {jogador}
    """
    
    letras_novas = jogador['letras'] + "".join(letra)
    
    jogador['letras'] = "".join(sorted(letras_novas, key = chave))
    
    return jogador

def usa_letra (jogador, letra):
    """
    Modifica destrutivamente o jogador fornecido como argumento,
    retirando a letra indicada às suas letras, e devolve o jogador.
    
    usa_letra: {jogador, str} -> {jogador}
    """
    
    jogador['letras'] = jogador['letras'].replace(letra, '', 1)
    
    return jogador

def soma_pontos (jogador, pontos):
    """
    Modifica destrutivamente o jogador fornecido como argumento,
    somando os pontos indicados à sua pontuação atual, e devolve o próprio jogador.
    
    soma_pontos: {jogador, int} -> {jogador}
    """
    
    jogador['pontos'] += pontos
    
    return jogador

# endregion

# region Reconhecedores
def eh_jogador (argumento):
    """
    Verifica se o argumento é um jogador e devolve True caso o argumento seja
    um TAD Jogador ou False caso contrário.
    
    eh_jogador: {universal} -> {bool}
    """
    
    if not isinstance(argumento, dict):
        return False
    
    if len(argumento.keys()) != 3:
        return False
    
    if 'nome' in argumento:
        conjunto_chaves_padrao = {'nome', 'pontos', 'letras'}
        if type(argumento['nome']) != str:
            return False
    elif 'nivel' in argumento:
        conjunto_chaves_padrao = {'nivel', 'pontos', 'letras'}
        if type(argumento['nivel']) != str:
            return False
    else:
        return False
    
    for chave in argumento:
       if chave not in conjunto_chaves_padrao:
           return False
       
    if type(argumento['pontos']) != int or argumento['pontos'] < 0:
        return False
    
    if type(argumento['letras']) != str:
        return False
    
    return True

def eh_humano (argumento):
    """
    Devolve True caso o seu arguemento seja um TAD Jogador humano e False caso
    contrário.
    
    eh_humano: {universal} -> {bool}
    """
    
    if eh_jogador(argumento):
        if 'nome' in argumento:
            return True
    
    return False

def eh_agente (argumento):
    """
    Devolve True caso o seu arguemento seja um TAD Jogador agente e False caso
    contrário.
    
    eh_humano: {universal} -> {bool}
    """
    
    if eh_jogador(argumento):
        if 'nivel' in argumento:
            return True
    
    return False
    
#endregion

# region Teste
def jogadores_iguais (jog1, jog2):
    """
    Devolve True apenas dejog1 e jog2 forem jogadores e forem iguais.
    
    jogadores_iguais: {universal, universal} -> {bool}
    """
    if eh_humano(jog1) and eh_humano(jog2):
        if jog1['nome'] == jog2['nome'] and jog1['pontos'] == jog2['pontos'] and jog1['letras'] == jog2['letras']:
            return True
    elif eh_agente(jog1) and eh_agente(jog2):
        if jog1['nivel'] == jog2['nivel'] and jog1['pontos'] == jog2['pontos'] and jog1['letras'] == jog2['letras']:
            return True
    
    return False

# endregion

# region Trasformador
def jogador_para_str(jogador):
    """
    Devolve a cadeia de caracteres que representa o jogador como
    mostrado nos exemplos.
    
    jogador_para_str: {jogador} -> {str}
    """
    cadeia_letras_jogador = adicionar_caracter(jogador_letras(jogador), ' ')
    
    if eh_humano(jogador):
        return f'{jogador_identidade(jogador)} ({jogador_pontos(jogador):>3}):{cadeia_letras_jogador}'
    elif eh_agente(jogador):
        return f'BOT({jogador_identidade(jogador)}) ({jogador_pontos(jogador):>3}):{cadeia_letras_jogador}'

# endregion

# region Funções de Alto Nível
def distribui_letras(jogador, saco, num):
    """
    Retira um máximo de num letras do final da lista saco (potencialmente vazia)
    e acrescenta-as ao jogador, devolvendo o jogador.
    A função modifica destrutivamente a lista de letras e o jogador passados como
    argumento.
    
    distribui_letras: {jogador, list, int} -> {jogador}
    """
    
    for i in range(0, num):
        if len(saco) == 0:                  # Apenas adicionar uma letra se o
            break                           # saco não estiver vazio.
        
        #Adicionar a última letra do saco às letras do jogador e removê-la do saco
        recebe_letra(jogador, saco.pop())
    
    return jogador
    
 
# endregion

# endregion


#region TAD Vocabulário

# O TAD vocabulario ´e usado para representar o conjunto de palavras que podem ser
# utilizadas durante o jogo. Adicionalmente, o TAD vocabulario regista a pontuação das
# palavras

# A estrutura de dados do TAD Vocabulário é organizada internamente por
# comprimento e primeira letra, para isso irão ser utilizados dicionários
# de dicionários.

# region Construtor
def cria_vocabulario(v):
    """
    Devolve o vocabulário que contém as palavras contidas no tuplo v. O
    construtor verifica a validade do seu argumento gerando um erro com
    a mensagem (cria_vocabulário: argumento inválido).
    
    cria_vocabulario: {tuple} -> {vocabulario}
    """
    
    if not isinstance(v, tuple) or len(v) < 1:
        raise ValueError('cria_vocabulario: argumento inválido')
    
    vocabulario = {}
    for palavra in v:
        #Verificar requisitos da palavra
        if type(palavra) != str or not 2 <= len(palavra) <= 15:
            raise ValueError('cria_vocabulario: argumento inválido')
        for letra in palavra:
            if letra not in {'A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'H', 'I',
                             'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                             'U', 'V', 'X', 'Z'}:
                raise ValueError('cria_vocabulario: argumento inválido')
        
            #Adicionar palavra
            if len(palavra) in vocabulario:
                if palavra[0] in vocabulario[len(palavra)]:
                    vocabulario[len(palavra)][palavra[0]] = vocabulario[len(palavra)][palavra[0]].union({palavra})
                else:
                    vocabulario[len(palavra)][palavra[0]] = {palavra}
            else:
                vocabulario[len(palavra)] = {}
                vocabulario[len(palavra)][palavra[0]] = {palavra}
    return vocabulario

# endregion

# region Seletores
def obtem_pontos(vocabulario, palavra):
    """
    Devolve os pontos da palavra do vocabolário, ou 0 caso não se encontre.
    
    obtem_pontos: {vocabulario, str} -> {int}
    """
    pontos = {'A': 1, 'B': 3, 'C': 2, 'Ç': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 4,
              'H': 4, 'I': 1, 'J': 5, 'L': 2, 'M': 1, 'N': 3, 'O': 1, 'P': 2,
              'Q': 6, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'X': 8, 'Z': 8}
    letra_inicial = palavra[0]
    comprimento = len(palavra)
    
    pontuacao_palavra = 0
    if palavra in vocabulario[comprimento][letra_inicial]: 
        for letra in palavra:
            pontuacao_palavra += pontos[letra]
    
    return pontuacao_palavra

def obtem_palavras (vocabulario, comprimento, letra):
    """
    Devolve um tuplo de pares que correspondem a todas as palavras com o 
    comprimento e a primeira letra fornecidos como argumentos.
    Cada par do tuplo contém a palavra e a respetiva pontuação. Os pares devem
    estar oredenados por ordem decrescente de pontuação das palavras, e em caso
    de empate, por ordem lexicográfica. Caso não existam no vocabuário
    palavras com o comprimento e a primeira letra indicados, a função deverá
    devolver um tuplo vazio.
    
    obtem_palavras: {vocabulario, int, str} -> {tuple}
    """
    if letra not in vocabulario[comprimento]:
        return ()
    
    tuplo_de_pares = ()
    for palavra in vocabulario[comprimento][letra]:
        tuplo_de_pares += ((palavra, int(obtem_pontos(vocabulario, palavra))),)

    return tuple(sorted(tuplo_de_pares, key=lambda x: (-x[1], chave(x[0]))))
    
        
# endregion

# region Teste
def testa_palavra_padrao(vocabulario, palavra, padrao, letras):
    """
    Devolve True caso exista a palavra no vocabulário e seja possível formar
    a palavra forncida substituindo os caracteres '.' do padrão por letras
    presentes na cadeia de caracteres letras, caso contrário, devolve False.
    
    testa_palavra_padrao: {vocabulario. str, str, str} -> {bool}
    """

    letra_inicial = palavra[0]
    comprimento = len(palavra)
    letras_jogador = letras
    
    # Verificar se a palavra está no vocabulário para o seu comprimento e letra
    # inicial sem levantar um key error.
    palavras_letra = vocabulario.get(comprimento, {}).get(letra_inicial, set())
    if palavra not in palavras_letra:
        return False
    
    if comprimento == len(padrao):
        for i in range(comprimento):
            if padrao[i] != '.' and padrao[i] != palavra[i]:
                return False
            elif padrao[i] == '.':
                if palavra[i] not in letras_jogador:
                    return False
                letras_jogador = letras_jogador.replace(palavra[i], '', 1)
        
        return True
    
    else: 
        return False

# endregion

# region Transformadores
def ficheiro_para_vocabulario(nome_ficheiro):
    """
    Devolve o vocabolário formado a partir das palavras contidas no ficheiro
    fornecido como argumento. Considere que o ficheiro contém uma palavra por
    linha, podendo ter linhas vazias (que serão ignoradas).
    As palavras do ficheiro são sequências de caracteres únicaas de comprimento
    arbitrário, contendo potencialmente qualquer caracter. Para a construção
    do vocabulário considere as palavras de comprimento de 2 a 15 letras do abecedário
    português, convertidas para letras maiscúlas.
    
    ficheiro_para_vocabulario: {str} -> {vocabolario}
    """
    
    with open(nome_ficheiro, 'r') as f:
        # Obter todas as linhas do ficheiro
        linhas = f.readlines()
        
    
        letras_validas = {'A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'H', 'I',
                        'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                        'V', 'X', 'Z'}
        
        tuplo_palavras = ()
        for linha in linhas:
            # obter a palavra maiusculada sem o '\n'
            palavra = linha.strip().upper()
            #Confirmar as letras e tamanho
            if 2 <= len(palavra) <= 15 and all(letra in letras_validas for letra in palavra):
                tuplo_palavras += (palavra,)
        
        return cria_vocabulario(tuplo_palavras)
    

def vocabulario_para_str (vocabulario):
    """
    Devolve uma cadeia de caracteres que concatena todas as palavras guardadas no
    vocabulário, separadas por um caracter de mudança de linha. As palavras devem
    estar ordenadas por ordem crescente do seu compriento e, para o mesmo
    comprimento, por ordem lexicográfica do seu primeiro caracter. Palavras que
    tenham o mesmo comprimento e o o mesmo primeiro caracter, devem estar ordenadas
    pala ordem definida no selotor obtem palavras.
    """

    palavras = []
    for comprimento in sorted(vocabulario.keys()): # ordem crescente de comprimento
        for letra_inicial in sorted(vocabulario[comprimento]): # ordem lexicográfica do primeiro caracter
            for palavra, _ in obtem_palavras(vocabulario, comprimento, letra_inicial):
                palavras.append(palavra) # obtem_palavras já devolve um tuplo de pares (palavra, pontos) ordenado corretamente.
                
    return '\n'.join(palavras)
            
# endregion

# region Funções Alto Nível

def procura_palavra_padrao(vocabulario, padrao, letras, min_pontos):
    """
    Devolve o tuplo formado pela palavra e a pontuação, que correspondem à
    palavra do vocabulário com a maior pontuação que é possível formar
    utilizando as letras da cadeia de caracteres letras para completar todos
    os espaços livres do padrão fornecido com argumento, cumprindo a restrição
    de que a pontuação da palavra não poderá ser inferior a min_pontos.
    Caso a função não encontre nenhuma palavra, deverá devolver o tuplo ('', 0).
        
    procura_palavra_padrao: {vocabulario, str, str, int} -> {tuple}
    """
    
    comprimento = len(padrao)
    pontuacao = 0
    palavra_escolhida = ''

    # Se não existe esse comprimento no vocabulário
    if comprimento not in vocabulario:
        return ('', 0)

    # Padrão começa com uma letra (fixa)
    if padrao[0] != '.':
        palavras = obtem_palavras(vocabulario, len(padrao), padrao[0])
        # obtem_palavras deve devolver um tuplo de pares (palavra, pontos)
        for tuplo in palavras:
            # proteger contra entradas inesperadas
            if not (isinstance(tuplo, tuple) and len(tuplo) >= 1):
                continue
            palavra = tuplo[0]
            # só testar palavra se ela for string
            if not isinstance(palavra, str):
                continue
            pontos_palavra = obtem_pontos(vocabulario, palavra)
            if pontos_palavra > pontuacao and testa_palavra_padrao(vocabulario, palavra, padrao, letras):
                pontuacao = pontos_palavra
                palavra_escolhida = palavra
            elif pontos_palavra == pontuacao and testa_palavra_padrao(vocabulario, palavra, padrao, letras):
                if palavra_escolhida == '' or palavra < palavra_escolhida:
                    palavra_escolhida = palavra

    # O padrão começa vazio — temos de tentar todas as letras do conjunto 'letras'
    else:
        palavras = ()
        for letra in letras:
            # obtem_palavras deve devolver um tuplo de pares (palavra, pontos) ou ()
            pares = obtem_palavras(vocabulario, len(padrao), letra)
            if not pares:
                continue
            # concatenar apenas se pares for do tipo iterável de pares
            palavras += tuple(pares)

        # iterar sobre tuplos (palavra, pontos) — protegendo contra entradas inválidas
        for item in palavras:
            if not (isinstance(item, tuple) and len(item) >= 1):
                continue
            palavra = item[0]
            if not isinstance(palavra, str):
                continue
            pontos_palavra = obtem_pontos(vocabulario, palavra)
            if pontos_palavra > pontuacao and testa_palavra_padrao(vocabulario, palavra, padrao, letras):
                pontuacao = pontos_palavra
                palavra_escolhida = palavra
            elif pontos_palavra == pontuacao and testa_palavra_padrao(vocabulario, palavra, padrao, letras):
                if palavra_escolhida == '' or palavra < palavra_escolhida:
                    palavra_escolhida = palavra

    return (palavra_escolhida, pontuacao) if pontuacao >= min_pontos else ('', 0)
        
# endregion

#endregion


#region TAD Tabuleiro

# A representação escolhida para este TAD é uma matriz - uma lista de listas.

# O TAD tabuleiro ´e usado para representar um tabuleiro do jogo Scrabble e as letras
# nele colocadas.

# region Construtores
def cria_tabuleiro ():
    """
    Vevolve um tabuleiro de Scrabble vazio.
    
    cria_tabuleiro: {} -> tabuleiro
    """
    
    tabuleiro = []
    for i in range(15):
        linha = []
        for j in range(15):
            linha.append(".")
        tabuleiro.append(linha)

    return tabuleiro

# endregion

# region Seletores
def obtem_letra(tabuleiro, casa):
    """
    Devolve a letra contida na casa indicada do tabuleiro fornecido como argumento.
    
    obtem_letras: {tabuleiro, casa} -> str
    """
    
    return tabuleiro[obtem_lin(casa) - 1][obtem_col(casa) - 1] #Passar de 1-based para 0-based

# endregion

# region Modificadores
def insere_letra(tabuleiro, casa, letra):
    """
    Modifica destrutivamente o tabuleiro fornecido como argumento, colocando a letra
    indicada na casa fornecida, e devolve o próprio tabuleiro.
    
    insere_letra: {tabuleiro, casa, str} -> {tabuleiro}
    """
    tabuleiro[obtem_lin(casa) - 1][obtem_col(casa) - 1] = letra #Passar de 1-based para 0-based

    return tabuleiro

# endregion

# region Reconhecedores
def eh_tabuleiro(argumento):
    """
    Devolve caso o argumento seja um TAD Tabuleiro e False caso contrário.
    
    eh_tabuleiro: {universal} -> {bool}
    """
    
    if type(argumento) == list: # Confirmar a estrutura
        if len(argumento) == 15: # Confirmar o número de linhas
            for linha in argumento:
                if type(linha) == list: #Confirmar a estrutura
                    if len(linha) == 15: #Confirmar número de colunas
                        return True
            
    return False


def eh_tabuleiro_vazio(argumento):
    """
    Devolve True caso o argumento seja um TAD Tabuleiro e estiver vazio, caso
    contrário devolve False.
    
    eh_tabuleiro. {universal} -> {bool}
    """
    if eh_tabuleiro(argumento):
        for linha in range(1, 16):
            for coluna in range (1, 16):
                if obtem_letra(argumento, cria_casa(linha, coluna)) != '.':
                    return False
        return True
    
    return False

# endregion

# region Teste
def tabuleiros_iguais(argumento1, argumento2):
    """
    Devolve True se ambos os argumentos forem TAD's Tabuleiro e forem iguais,
    caso contrário devolve False.
    
    tabuleiros_iguais: {universal, universal} -> {bool}
    """
    if eh_tabuleiro(argumento1) and eh_tabuleiro(argumento2): #Verificar se ambos são tabuleiros
        for linha in range(1, 16):
            for coluna in range (1, 16):
                if obtem_letra(argumento1, cria_casa(linha, coluna)) != obtem_letra(argumento2, cria_casa(linha, coluna)):
                    return False
        return True

# endregion

# region Transformador
def tabuleiro_para_str(tabuleiro):
    """
    Devolve a cadeia de caracteres que representa o tabuleiro.
    
    tabuleiro_para_str: {tabuleiro} -> {str}
    """
    
    linha_divisao = "   +-------------------------------+"

    tabuleiro_str = "                       1 1 1 1 1 1\n"  # linha 1
    tabuleiro_str += "     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5\n"  # linha 2
    tabuleiro_str += linha_divisao + '\n'  # linha 3

    # Adicionar as linhas de jogo
    for i in range(15):
        # Cria um str com os caracteres da linha
        linha = "".join(filter(filtro_caracteres, tabuleiro[i]))

        # Adicionar os espaços a cada linha
        linha = adicionar_caracter(linha, ' ')

        # Adicionar os limites a cada linha
        linha = " |" + linha + " |\n"

        # Adicionar a linha ao tabuleiro
        if i < 9:
            tabuleiro_str = tabuleiro_str + f" {i + 1}" + linha #Formatação devido ao digito a menos na linha
        else:
            tabuleiro_str = tabuleiro_str + f"{i + 1}" + linha  #Linha com dois dígitos, não precisa de espaço

    tabuleiro_str += linha_divisao #última linha

    return tabuleiro_str

# endregion

# region Funções de Alto Nível
def obtem_padrao(tabuleiro, casa_i, casa_f):
    """
    Devolve a sequência de letras contida no tabuleiro entre a casa inicial, casa_i,
    e a casa final, casa_f, (ambas inclusive) na mesma linha ou coluna.
    """
    
    linha_i = obtem_lin(casa_i)
    linha_f = obtem_lin(casa_f)
    
    coluna_i = obtem_col(casa_i)
    coluna_f = obtem_col(casa_f)
    
    padrao = ''
    
        
    if linha_i == linha_f:  # As casas estão na mesma linha
        for coluna in range(coluna_i, coluna_f + 1):
            casa_atual = cria_casa(linha_i, coluna)
            padrao += obtem_letra(tabuleiro, casa_atual)
    
    elif coluna_i == coluna_f: # As casas estão na mesma coluna
        for linha in range(linha_i, linha_f + 1):
            casa_atual = cria_casa(linha, coluna_i)
            padrao += obtem_letra(tabuleiro, casa_atual)
    else:
        raise ValueError("obtem_padrao: argumentos invalidos")
    
    return padrao


def insere_palavra(tabuleiro, casa, direcao, palavra):
    """
    Modifica destrutivamente o tabuleiro fornecido colocando a palavra selecionada
    na casa indicada na direção pretendida e devolve o próprio tabuleiro.
    
    insere_palavra: {tabuleiro, casa, str, str} -> {tabuleiro}
    """
    
    if direcao == 'V':
        for i in range(len(palavra)):
            insere_letra(tabuleiro, cria_casa(obtem_lin(casa) + i, obtem_col(casa)), palavra[i])
    elif direcao == 'H':
        for i in range(len(palavra)):
            insere_letra(tabuleiro, cria_casa(obtem_lin(casa), obtem_col(casa) + i), palavra[i])
    
    return tabuleiro


def obtem_subpadroes (tabuleiro, casa_i, casa_f, numero_maximo_espacos):
    """
    Devolve dois tuplos de igual tamanho. O primeiro tuplo contém todos os
    subpadrões viáveis ordenados gerados a partir do padrão original contido
    no tabuleiro fornecido como argumento, entre as casas casa_i e casa_f
    (ambas inclusive), com, no máximo, numero_maximo_espaços espaços livres.
    O segundo tuplo contém a casa onde começa cada um dos subpadrões
    correspondentes do primeiro tuplo. As casas casa_i e casa_f pertencem à
    mesma linha ou à mesma coluna.
    """
    
    padrao = obtem_padrao(tabuleiro, casa_i, casa_f)
    tuplo_subpadroes = ()
    tuplo_casas_i = ()
    
    for i in range(len(padrao)):
        for j in range(len(padrao), i, -1):  # ordem: mais longo primeiro
            subpadrao = padrao[i:j]
            
            # Contar espaços livres
            n_espacos = subpadrao.count('.')
            if n_espacos == 0 or n_espacos > numero_maximo_espacos:
                continue  # regra 2 e limite máximo

            # Confirmar que há pelo menos uma letra
            tem_letra = any(c != '.' for c in subpadrao)
            if not tem_letra:
                continue  # regra 1

            # Confirmar que não está colado a outras letras
            anterior_livre = (i == 0) or (padrao[i - 1] == '.')
            seguinte_livre = (j == len(padrao)) or (padrao[j] == '.')
            if not (anterior_livre and seguinte_livre):
                continue  # regra 3

            # Subpadrão viável — guardar
            tuplo_subpadroes += (subpadrao,)
            if obtem_lin(casa_i) == obtem_lin(casa_f):
                tuplo_casas_i += (cria_casa(obtem_lin(casa_i), obtem_col(casa_i) + i),)
            else:
                tuplo_casas_i += (cria_casa(obtem_lin(casa_i) + i, obtem_col(casa_i)),)
    
    return tuplo_subpadroes , tuplo_casas_i

def gera_todos_padroes(tabuleiro, numero_maximo_espacos):
    """
    Devolve três tuplos de igual tamanho. O primeiro contém todos os subpadrões
    viáveis do tabuleiro que contenham,no máximo, numero_maximo_espacos de
    espaços livres, formado pelos subpadrões ordenados obtidos de cada uma das
    linhas completas do tabuleiro (da primeira à última), seguidos dos subpadrões
    ordenados obtidos de cada coluna completa (da primeira até à última). O
    segundo e terceiro tuplos, correspondem à casa de início e à direção ('V' ou
    'H') do subpadrão correspondente do primeiro tuplo.
    
    gera_todos_padroes: {tabuleiro, int} -> {tuple, tuple, tuple}
    """
    
    tuplo_subpadroes = ()
    tuplo_casas_i = ()
    tuplo_direcoes = ()
    
    # Subpadrões das linhas
    for linha in range(1, 16):
        casa_i = cria_casa(linha, 1)
        casa_f = cria_casa(linha, 15)
        
        subpadroes, casas_i = obtem_subpadroes(tabuleiro, casa_i, casa_f, numero_maximo_espacos)
        
        tuplo_subpadroes += subpadroes
        tuplo_casas_i += casas_i
        tuplo_direcoes += tuple('H' for _ in subpadroes)
        
    # Subpadrões das colunas
    for coluna in range(1, 16):
        casa_i = cria_casa(1, coluna)
        casa_f = cria_casa(15, coluna)
        
        subpadroes, casas_i = obtem_subpadroes(tabuleiro, casa_i, casa_f, numero_maximo_espacos)
        
        tuplo_subpadroes += subpadroes
        tuplo_casas_i += casas_i
        tuplo_direcoes += tuple('V' for _ in subpadroes)
    
    return tuplo_subpadroes, tuplo_casas_i, tuplo_direcoes

# endregion

#endregion


#region Funções Adicionais
def baralha_saco(seed):
    """
    É uma função auxiliar que recebe um inteiro positivo seed representando o estado
    inicial do gerador de números pseudo-aleatório do primeiro projeto, e devolve uma
    lista baralhada com todas as letras contidas no saco de Scrabble.

    baralha_saco: {int} -> {list}
    """
    
    saco = {'A': 14, 'B': 3, 'C': 4, 'Ç': 2, 'D': 5, 'E': 11,
            'F': 2, 'G': 2, 'H': 2, 'I': 10, 'J': 2, 'L': 5,
            'M': 6, 'N': 4, 'O': 10, 'P': 4, 'Q': 1, 'R': 6,
            'S': 8, 'T': 5, 'U': 7, 'V': 2, 'X': 1, 'Z': 1 }

    conjunto = elementos_conjunto(saco)     #Criar uma lista com todas as letras do conjunto (dict)

    permuta_letras(conjunto, seed)        #Baralhar a lista

    return conjunto


def jogada_humano (tabuleiro, jogador, vocabulario, pilha):
    """
    É uma função auxiliar que recebe um tabuleiro, um jogador humano, um vocabulario,
    e uma lista de letras. A função processa o turno completo do jogador humano.
    
    joagada_humano: {tabuleiro, jogador, vocabulario, list} -> {bool}
    """
    letras = [
            "A",
            "B",
            "C",
            "Ç",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "X",
            "Z",
        ]
    
    # Obter jogada e processá-la:
    while True:
        
        continua = True #variável da Máquina de Estados
        
        jogada = input(f"Jogada {jogador_identidade(jogador)}: ")
        
        # Jogada vazia
        if jogada == '':
            continue
        
        # Passar a jogada:
        elif jogada == 'P':
            return False
        
        # Trocar letras
        elif jogada[0] == 'T':
            # Focar apenas nas letras a trocar
            jogada = jogada[2::]

            if len(jogada) % 2 == 0:
                continua = False
                
            if continua:
                # Verificar se as letras estão separadas por " "
                for index in range(len(jogada)):
                    if index % 2 == 0 and not jogada[index] in jogador_letras(jogador):
                        continua = False
                        break
                    elif index % 2 == 1 and not jogada[index] == " ":
                        continua = False
                        break

            # Trocar as letras
            if continua:
                letras_a_trocar = jogada.split(' ')
                
                #Verificar se há letras suficientes no saco
                if len(letras_a_trocar) > len(pilha):
                    # Não há letras suficientes no saco para a troca
                    # O jogador deve tentar outra jogada
                    continue  # Volta ao início do loop para nova tentativa
                
                for letra in letras_a_trocar:
                    jogador = usa_letra(jogador, letra)
                
                jogador = distribui_letras(jogador, pilha, len(letras_a_trocar))
                
                return True

        # Colocar palavra
        elif jogada[0] == "J":
            if jogada.count(" ") != 4:
                continua = False
            else:
                # Dividir a jogada em partes
                partes = jogada.split()
                
                if len(partes) < 5:
                    continua = False
                else:
                    #atribuir as várias partes da jogada a variáveis próprias
                    J, linha_str, coluna_str, direcao, palavra = partes

                    # Obter indicações de colocação da palavra
                    linha = int(linha_str)
                    coluna = int(coluna_str)
                    if direcao not in ("H", "V"):
                        continua = False
                    if not (1 <= linha <= 15 and 1 <= coluna <= 15):
                        continua = False

                    # Verificar se todas as letras são válidas
                    for letra in palavra:
                        if letra not in letras:
                            continua = False
                            break
                
                if continua:
                    casa_inicial = cria_casa(linha, coluna)
                    
                    if direcao == 'V':
                        casa_final = cria_casa(linha + len(palavra) - 1, coluna)
                    elif direcao == 'H':
                        casa_final = cria_casa(linha, coluna + len(palavra) - 1)
                        
                    padrao = obtem_padrao(tabuleiro, casa_inicial, casa_final)
                    
                    if not testa_palavra_padrao(vocabulario, palavra, padrao, jogador_letras(jogador)):
                            continua = False

                    if continua:
                        
                        tab = insere_palavra(tabuleiro, casa_inicial, direcao, palavra)
                        
                        pontuacao_jogada = obtem_pontos(vocabulario, palavra)
                        
                        jogador = soma_pontos(jogador, pontuacao_jogada)
                        
                        # Remover as letras jogadas do conjunto do jogador
                        letras_a_retirar = []
                        for i in range(len(palavra)):
                            if padrao[i] == '.':
                                letras_a_retirar.append(palavra[i])
                                
                        for letra in letras_a_retirar:
                            jogador = usa_letra(jogador, letra)
                        
                        # Repor as letras
                        jogador = distribui_letras(jogador, pilha, len(letras_a_retirar))
                        
                        return True


def jogada_agente (tabuleiro, jogador, vocabulario, pilha):
    """
    É uma função auxiliar que recebe um tabuleiro, um jogador agente, um
    vocabulário e uma lista de letras, e raliza uma das seguintes ações:
    
    - Passar: Se for a primeira jogada (tabuleiro vazio), ou, caso contrário, se
    não conseguir Jogar nem Trocar. Neste caso a função devolve False sem alterar
    nenhum dos argumentos.
    
    - Trocar: Caso não consiga Jogar e existam pelo menos sete letras no saco, troca
    todas as letras. Neste caso, a função devolve True, modifica o jogador retirando
    novas letras do final da lista de letras (que também é modificada).
    
    - Jogar: Devolve True e modifica o tabuleiro, atualiza o jogador, atualizando a sua
    pontuação e retirando novas letras do final da lista de letras (que é também
    modificada). Para escolher a palavra, a casa e a direção a função deve:
    
        1. Gerar todos os padrões possíveis para a configuaração atual do tabuleiro,
        através da função gera_todos_padroes, tendo em conta o número de letras do jogador;
        
        2. Selecionar um de cada N padrões (operação slicing [::N]) obtidos anteriormente,
        sendo N = 100, se nível for 'FACIL', N = 50, se nível for 'MEDIO', e N = 10, se nível
        for 'DIFICIL'.
        
        3. Sobre cada um dos padrões resultantes, invocar a função procura_palavra_padrao e
        selecionar a primeira palavra obtida com maior pontuação.
        
    A função apresenta a mensagem da jogada realizada imitando o formato utilizado pelos
    jogadores humanos.
    
    jogada_agente: {tabuleiro, jogador, vocabulario, list} -> {bool}
    """
    
    
    # Passar
    if eh_tabuleiro_vazio(tabuleiro):
        print(f'Jogada {jogador_identidade(jogador)}: P')
        return False
    
    #Jogar
    
    #Gerar todos os padrões com base no número de letras do jogador
    padroes, casas_i, direcoes= gera_todos_padroes(tabuleiro, len(jogador_letras(jogador)))
        
    #Slicing dos padrões conforme o nível do agente
    if jogador_identidade(jogador) == 'FACIL':
        padroes = padroes[::100]
        casas_i = casas_i[::100]
        direcoes = direcoes[::100]
            
    elif jogador_identidade(jogador) == 'MEDIO':
        padroes = padroes[::50]
        casas_i = casas_i[::50]
        direcoes = direcoes[::50]
            
    elif jogador_identidade(jogador) == 'DIFICIL':
        padroes = padroes[::10]
        casas_i = casas_i[::10]
        direcoes = direcoes[::10]
        
    melhor_pontuacao = 0
    melhor_jogada = None
        
    for i in range(len(padroes)):
            
        padrao = padroes[i]
        casa_i = casas_i[i]
        direcao = direcoes[i]
            
        #Procurar palavra para este padrao
            
        palavra, pontuacao = procura_palavra_padrao(vocabulario, padrao, jogador_letras(jogador), melhor_pontuacao)
            
        #Se encontrou uma palavra com melhor pontuação atualizar
            
        if pontuacao > melhor_pontuacao:
            melhor_pontuacao = pontuacao
            melhor_jogada = (palavra, casa_i, direcao, padrao)
                
    # Se encontrou uma jogada válida
    if melhor_jogada and melhor_jogada[0]:  # palavra não é vazia
        palavra, casa_i, direcao, padrao = melhor_jogada
        
        # Inserir palavra no tabuleiro
        tabuleiro = insere_palavra(tabuleiro, casa_i, direcao, palavra)
            
        #Atualizar pontuação
        jogador = soma_pontos(jogador, melhor_pontuacao)
            
        # Determinar as letras usadas (apenas as que preencheram espaços vazios)
        letras_usadas = []
        for i in range(len(palavra)):
            if padrao[i] == '.':
                letras_usadas.append(palavra[i])
                    
        #Remover as letras usadas
        for letra in letras_usadas:
            usa_letra(jogador, letra)
                
        #Repor letras
        distribui_letras(jogador, pilha, len(letras_usadas))
        
        # Mostrar jogada no formato correto
        print(f"Jogada {jogador_identidade(jogador)}: J {obtem_lin(casa_i)} {obtem_col(casa_i)} {direcao} {palavra}")
            
        return True
        
    #Trocar - se não conseguiu jogar e há letras suficientes
    elif len(pilha) >= 7:
        # Guardar letras atuais para mostrar na mensagem
        letras_atuais = jogador_letras(jogador)
        
        #Remover as letras
        for letra in jogador_letras(jogador):
            jogador = usa_letra(jogador, letra)
            
        #Adicionar as letras novas
        jogador = distribui_letras(jogador, pilha, 7)
        
        # Mostrar jogada de troca
        letras_formatadas = ' '.join(letras_atuais)
        print(f"Jogada {jogador_identidade(jogador)}: T {letras_formatadas}")
        
        return True
    
    else:
        print(f"Jogada {jogador_identidade(jogador)}: P")
        return False
    
    
def scrabble2 (jogadores, nome_fich, seed):
    """
    É a função principal que permite jogar um jogo completo de Scrabble2 de dois
    a quatro jogadores. A função recebe um tuplo com o nome dos jogadores humanos
    (cadeia de caracteres não vazia) e o nível dos jogadores agentes (cadeia de
    caracteres a começar por '@' seguido do nível) na ordem em que jogam, um nome
    de ficheiro com o vocabulário e um inteiro positivo representando o estado
    inicial do gerador pseudo-aleatório, e devolve o tuplo com a pontuação final
    obtida pelos jogadores.
    
    O Jogo começa baralhando o saco de letras e distribuindo o conjunto de 7 letras
    a cada um dos jogadores em ordem. O Jogo desenrola-se depois conforme as regras.
    
    O Jogo termina quando todos os jogadores passam ou quando um jogador fica sem
    letras e o saco está esgotado.  A função deve verificar a validade do seus argumentos,
    gerando um erro com a mensagem 'scrabble2: argumwntos inválidos'.
    
    scrabble2: {tuple, string, int} -> {tuple}
    """
    
    # Validação de argumentos
    if (not isinstance(jogadores, tuple) or not  2 <= len(jogadores) <= 4 or
        not isinstance(nome_fich, str) or nome_fich == '' or
        not isinstance(seed, int) or seed <= 0):
        
        raise ValueError("scrabble2: argumentos inválidos")
    
    for j in jogadores:
        if not isinstance(j, str) or j == '':
            raise ValueError('scrabble2: argumentos inválidos')
        if j[0] == '@' and len(j) == 1:
            raise ValueError('scrabble2: argumentos inválidos')
        if j[0] == '@':
            nivel = j[1:]
            if nivel not in {'FACIL', 'MEDIO', 'DIFICIL'}:
                raise ValueError('scrabble2: argumentos inválidos')
        
    # Inicialização
    print("Bem-vindo ao SCRABBLE2.")
    
    tabuleiro = cria_tabuleiro()
    
    pilha = baralha_saco(seed)
    
    vocabulario = ficheiro_para_vocabulario(nome_fich)
    
    # Criar listas de jogadores (humanos e agentes)
    lista_jogadores = []
    
    for nome in jogadores:
        if nome[0] == '@':
            lista_jogadores.append(cria_agente(nome[1::].upper()))
        else:
            lista_jogadores.append(cria_humano(nome))
            
    #Distribuir 7 letras a cada jogador
    for i in range(len(lista_jogadores)):
        lista_jogadores[i] = distribui_letras(lista_jogadores[i], pilha, 7)
        
    # Loop principal
    passes_consecutivos = 0
    num_jogadores = len(lista_jogadores)
    fim_jogo = False

    
    while not fim_jogo:
        for i in range(num_jogadores):
            
            #Interromper o jogo devido ao número de 'passo'
            if passes_consecutivos >= num_jogadores:
                fim_jogo = True
                break
            
            
             # Imprimir tabuleiro
            print(tabuleiro_para_str(tabuleiro), '\n')
            
            # Imprimir status dos jogadores
            for jogador in lista_jogadores:
                print(jogador_para_str(jogador))
            
            print()
            
            jogador = lista_jogadores[i]
            
            
            
            # Jogada
            nome = jogador_identidade(jogador)
            
            if eh_agente(jogador):
                resultado = jogada_agente(tabuleiro, jogador, vocabulario, pilha)
            elif eh_humano(jogador):
                resultado = jogada_humano(tabuleiro, jogador, vocabulario, pilha)
            
            # Verificar se o jogador passou
            if resultado is False:
                passes_consecutivos += 1
            else:
                passes_consecutivos = 0
                
            #Verificar se jogador ficou sem letras e o saco está vazio
            if len(jogador_letras(jogador)) == 0 and len(pilha) == 0:
                fim_jogo = True
                break
    
    # Cálculo das pontuações finais
    pontuacoes_finais = tuple(jogador_pontos(jogador) for jogador in lista_jogadores)
    
    return pontuacoes_finais
    

#endregion


#region Funções Acessórias
def adicionar_caracter(cadeia, caracter):
    """
    Separa os caracteres de uma string com espaços
    
    adicionar_espaços: {str} -> {str}
    """
    index = 0
    while index <= len(cadeia) -1:
        #Obeter parte da cadeia até ao elemento anterior ao índice,
        #adicionar um espaço, adicionar o resto da cadeia
        cadeia = cadeia[0:index:1] + f"{caracter}" + cadeia[index : len(cadeia) : 1]
        index += 2
    return cadeia


def chave(palavra):
    """
    Função utilizada como chave para a função sorted, de forma a ordenar 
    lexicograficamente as palavras.
    
    chave: {str} -> {int}
    """
    
    alfabeto = 'A B C Ç D E F G H I J L M N O P Q R S T U V X Z'.split()
    # Criar um dicionário de prioridade
    prioridade = {letra: i for i, letra in enumerate(alfabeto)}
    
    return [prioridade[letra] for letra in palavra]


def filtro_caracteres(ch):
    """
    Função acessória para filtrar os elementos de cada linha do tabuleiro

    filtro_linhas: {str} -> {bool}
    """

    if ch in ["[", "]", ","]:   #Se o caractere em análise estiver nesta lista, remove-o
        return False
    else:
        return True


def elementos_conjunto(conj):
    """
    Primeiro cria-se uma lista com todas as chaves. Depois, percorre-se essa
    lista e, para cada chave (letra), adiciona-se ao conjunto a letra um número
    vezes correspondente ao valor associado à chave (ocorrências). Por fim, a
    lista é ordenada.

    elementos_conjunto: {dict} -> {str}
    """

    chaves = list(conj.keys())
    conjunto = ''

    for letra in chaves:
        occ = conj[letra]
        for i in range(occ):
            conjunto += ''.join(letra)

    conjunto = sorted(conjunto, key=chave)  # Utiliza a função previamente definida para a ordenação

    return conjunto

def permuta_letras(letras, estado):
    """
    Permuta uma sequência recorrendo a um algoritmo de Fisher-Yates. Para gerar
    os números aleatórios dentro do intervalo desejado, recorre-se à função
    gera_numero_aleatorio(). Devolve ainda o último número aleatório gerado.

    permuta_letras: {list, int} -> {}
    """

    n = len(letras)
    for i in range(n - 1, 0, -1):
        estado = gera_numero_aleatorio(estado)
        j = estado % (i + 1)
        letras[j], letras[i] = letras[i], letras[j]
        

def gera_numero_aleatorio(estado):
    """
    Utiliza o layout fornecido no enunciado para gerar um número pseudo-aleatório.

    xorshift32: {int} -> {int}
    """

    estado ^= (estado << 13) & 0xFFFFFFFF
    estado ^= (estado >> 17) & 0xFFFFFFFF
    estado ^= (estado << 5) & 0xFFFFFFFF

    return estado & 0xFFFFFFFF

#endregion






# Exemplo de Jogo

jog = ('Leticia', '@MEDIO', '@DIFICIL', )

scrabble2(jog, 'vocab25k.txt', 32)