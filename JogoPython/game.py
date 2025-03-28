import json
import random

def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            return dados
    except:
        return { "jogadores": [], "pontuacao_media": 0 }

def armazenar_ranking_json(ranking):
    with open(nome_arquivo, "w") as arquivo:
        jsonStr = json.dumps(ranking, indent = 4)
        arquivo.write(jsonStr)
        
def inserir_ranking_jogador(rank_jogador, ranking):
    tentativas_jogador = rank_jogador['tentativas']
    possui_ranking = False
    
    if not 'jogadores' in ranking: ranking['jogadores'] = []
    
    for rank in ranking['jogadores']:
        if rank['nome'] == rank_jogador['nome']:
            possui_ranking = True
            if rank['tentativas'] > tentativas_jogador:
                    rank['tentativas'] = tentativas_jogador
    
    if not possui_ranking:
        ranking['jogadores'].append(rank_jogador)
              
def calcular_media_tentativas(ranking):
    total_tentativas = 0
    
    for rank in ranking['jogadores']: 
        total_tentativas += rank['tentativas']
    
    total_jogadores = len(ranking['jogadores'])
    media = total_tentativas / total_jogadores
    return round(media, 2) 

def obter_nome_valido():
    while True:
        nome = input('Bem-vindo! Digite seu nome com 3 letras: ')
        if len(nome) == 3 and nome.isalpha():
            return nome.upper()
        print('Por favor, digite apenas 3 letras.')
    
nome_arquivo = 'ranking.json'

numero_secreto = random.randint(1, 50)

ranking = ler_json(nome_arquivo)

nome = obter_nome_valido()
print(f'Olá, {nome}! Este é um jogo de adivinhação.')
print('Tente adivinhar o número secreto entre 1 e 50!')

tentativas = 0

while True:
    try:
        tentativa = int(input('Digite um numero: '))
    except ValueError:
        print('Digite um numero valido')
        continue

    tentativas += 1

    if tentativa == numero_secreto:
        print(f'\nParabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s).')
        
        inserir_ranking_jogador({"nome": nome, "tentativas": tentativas}, ranking)
        
        jogadores_ordenados = sorted(ranking['jogadores'], key=lambda x: x['tentativas'])
        ranking['jogadores'] = jogadores_ordenados
        
        media_pontuacao = calcular_media_tentativas(ranking)
        ranking['pontuacao_media'] = media_pontuacao
        
        armazenar_ranking_json(ranking)
        
        print('=== RANKING ===')
        for i, jogador in enumerate(ranking['jogadores']): 
            print(f'{i + 1}. {jogador["nome"]}: {jogador["tentativas"]} tentativa(s)')

        print(f'\nA pontuação média das tentativas dos jogadores é de: {media_pontuacao:}')
                
        break
    elif tentativa < numero_secreto:
        print(f'O número é maior do que {tentativa}.')
    else:
        print(f'O número é menor do que {tentativa}.')