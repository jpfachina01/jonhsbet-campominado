from campo_minado import CampoMinado

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
