# IART-g39

## Executar o programa

* Instalar o [Python3](https://www.python.org/);
* Instalar o módulo [pygame](https://www.pygame.org/);

```
pip install pygame
```

* Para correr o programa, basta fazer Run do ficheiro `main.py` se for corrido num IDE ou então utilizando a linha de comandos, com o comando:

```
#Windows: python main.py

#Linux: python3 main.py
```

## Como jogar

Quando o jogo já estiver a ser executado, são apresentadas duas opções: "Player Mode" e "Computer Mode".

Escolhendo o "Player Mode", é possível selecionar um dos 20 níveis existentes. Os níveis estão ordenados por ordem crescente do número de movimentos otimo para os resolver. A cada nível o jogador deve utilizar as setas para mover as peças sincronamente e colocá-las nas posições corretas com o menor número de movimentos possível.

No modo computador, é possível escolher um dos 6 algoritmos implementados e um dos 20 níveis e observar a solução do computador carregando na tecla "Enter" a cada jogada.

Quando se completa o nível, a aplicação espera 2 segundos antes de fechar o jogo.

No canto superior direito do tabuleiro é possível observar o número de jogadas efetuadas e o número de jogadas ótimas para resolver o puzzle.

Do lado direito do tabuleiro, apresentam-se 3 opções:

 * Hint, para obter uma ajuda para o próximo movimento a executar. Caso ainda seja possível resolver o tabuleiro, entao o computador executa a melhor jogada possível. Caso contrário, o nível é reiniciado;
 * Reset, para reiniciar o nível;
 * Quit, para sair do nível e regressar ao menu inicial.


