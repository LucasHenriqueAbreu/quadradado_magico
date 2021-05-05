from tabuleiro import gerar_tabuleiro, mostrar_tabuleiro, validar_tabuleiro_e_quadrado_magico

tabuleiro_magico_valido = False
while not tabuleiro_magico_valido:
    print('-=' * 30)
    tabuleiro = gerar_tabuleiro()
    mostrar_tabuleiro(tabuleiro)
    tabuleiro_magico_valido = validar_tabuleiro_e_quadrado_magico(tabuleiro)
    print('-=' * 30)

if tabuleiro_magico_valido:
    print('Ihuuull, quadrado mágico!!')

