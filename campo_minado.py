import random

class CampoMinado:
    def __init__(self, tamanho=5, bombas=5):
        self.tamanho = tamanho
        self.bombas = bombas
        self.grid = [[' ' for _ in range(tamanho)] for _ in range(tamanho)]
        self.bombas_posicionadas = set()
        self.jogo_terminado = False
        self.reveladas = set()

    def posicionar_bombas(self):
        while len(self.bombas_posicionadas) < self.bombas:
            linha = random.randint(0, self.tamanho - 1)
            coluna = random.randint(0, self.tamanho - 1)
            if (linha, coluna) not in self.bombas_posicionadas:
                self.bombas_posicionadas.add((linha, coluna))
                self.grid[linha][coluna] = 'B'

    def contar_bombas_adjacentes(self, linha, coluna):
        contador = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= linha + i < self.tamanho and 0 <= coluna + j < self.tamanho:
                    if (linha + i, coluna + j) in self.bombas_posicionadas:
                        contador += 1
        return contador

    def revelar_celula(self, linha, coluna):
        if (linha, coluna) in self.bombas_posicionadas:
            self.jogo_terminado = True
            return 'BOOM! Você ativou uma bomba!'
        
        if (linha, coluna) not in self.reveladas:
            self.reveladas.add((linha, coluna))
            contador = self.contar_bombas_adjacentes(linha, coluna)
            self.grid[linha][coluna] = str(contador) if contador > 0 else ' '
        
        if len(self.reveladas) == (self.tamanho ** 2) - self.bombas:
            self.jogo_terminado = True
            return 'Parabéns! Você venceu!'

    def mostrar_grid(self):
        for linha in self.grid:
            print(' '.join(linha))
        print()

def main():
    tamanho = 5
    while True:
        try:
            bombas = int(input(f'Quantas bombas (1 a 12) você quer colocar? '))
            if 1 <= bombas <= 12:
                break
            else:
                print('Por favor, escolha um número entre 1 e 12.')
        except ValueError:
            print('Por favor, insira um número válido.')

    jogo = CampoMinado(tamanho, bombas)
    jogo.posicionar_bombas()

    while not jogo.jogo_terminado:
        jogo.mostrar_grid()
        try:
            linha = int(input('Escolha uma linha (0-4): '))
            coluna = int(input('Escolha uma coluna (0-4): '))
            if 0 <= linha < tamanho and 0 <= coluna < tamanho:
                resultado = jogo.revelar_celula(linha, coluna)
                print(resultado)
            else:
                print('Por favor, escolha uma linha e coluna válidas.')
        except ValueError:
            print('Por favor, insira um número válido.')

    jogo.mostrar_grid()
    print('Jogo terminado.')

if __name__ == "__main__":
    main()
