# Jogo de Adivinhação com Ranking

Este projeto é um jogo de adivinhação desenvolvido como parte de um trabalho acadêmico de lógica de programação. O objetivo do jogo é que o jogador tente adivinhar um número secreto gerado aleatoriamente. O jogo também possui um sistema de ranking que registra e ordena os jogadores com base no menor número de tentativas.

## Funcionalidades
- O jogador deve inserir um nome válido composto por exatamente 3 letras.
- O jogo gera um número aleatório entre 1 e 50.
- O jogador deve tentar adivinhar o número, recebendo dicas se o valor é maior ou menor.
- O jogo registra o nome do jogador e o número de tentativas no ranking.
- O ranking é armazenado em um arquivo JSON (`ranking.json`).
- A média de tentativas entre todos os jogadores é calculada e exibida.
- O ranking é atualizado automaticamente para manter os jogadores ordenados por desempenho.

## Como Executar
1. Certifique-se de ter o Python instalado em sua máquina.
2. Salve o arquivo do código-fonte com a extensão `.py`.
3. Execute o script no terminal ou prompt de comando:
   ```sh
   python nome_do_arquivo.py
   ```
4. Digite seu nome e siga as instruções para jogar.

## Estrutura do Projeto
- `ranking.json`: Arquivo onde são armazenados os dados do ranking.
- `jogo.py` (ou nome semelhante): Arquivo principal contendo a lógica do jogo.

## Exemplo de Uso
```
Bem-vindo! Digite seu nome com 3 letras: DIE
Olá, DIE! Este é um jogo de adivinhação.
Tente adivinhar o número secreto entre 1 e 50!
Digite um numero: 25
O número é maior do que 25.
Digite um numero: 40
O número é menor do que 40.
...
Parabéns! Você acertou o número 37 em 5 tentativa(s).

=== RANKING ===
1. ANA: 3 tentativa(s)
2. DIE: 5 tentativa(s)
3. LUC: 7 tentativa(s)

A pontuação média das tentativas dos jogadores é de: 5.0
```

## Tecnologias Utilizadas
- Python 3
- Biblioteca `json` para manipulação do ranking
- Biblioteca `random` para geração do número secreto

## Melhorias Futuras
- Implementar um menu interativo.
- Permitir diferentes níveis de dificuldade.
- Melhorar a interface com elementos visuais.
- Adicionar suporte para mais estatísticas no ranking.

## Autor
Este projeto foi desenvolvido para fins acadêmicos como exercício de lógica de programação.

