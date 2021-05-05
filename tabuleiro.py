from random import randint
import operacoes

def gerar_tabuleiro():
    tabuleiro = []
    for i in range(0, 3):
        linha = []
        for j in range(0, 3):
            numero_invalido = True
            while numero_invalido:
                numero_aleatorio = randint(1, 9)
                numero_invalido = verificar_numero_existe_lista(numero_aleatorio, linha) or \
                                    veificar_numero_existe_tabuleiro(numero_aleatorio, tabuleiro)

            linha.append(numero_aleatorio)

        tabuleiro.append(linha)
    return tabuleiro

def verificar_numero_existe_lista(numero, lista):
    return numero in lista

def veificar_numero_existe_tabuleiro(numero, tabuleiro):
    for lista in tabuleiro:
        if verificar_numero_existe_lista(numero, lista):
            return True
    return False

def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(linha)

def validar_tabuleiro_e_quadrado_magico(tabuleiro):
    result_soma_linha1 = operacoes.soma_linha(tabuleiro[1])
    result_soma_linha2 = operacoes.soma_linha(tabuleiro[2])
    result_soma_linha3 = operacoes.soma_linha(tabuleiro[0])
    result_soma_coluna1 = operacoes.soma_coluna(tabuleiro, 0)
    result_soma_coluna2 = operacoes.soma_coluna(tabuleiro, 1)
    result_soma_coluna3 = operacoes.soma_coluna(tabuleiro, 2)
    result_soma_diagonal_esq_dir = operacoes.soma_diagonal_esq_dir(tabuleiro)
    result_soma_diagonal_dir_esq = operacoes.soma_diagonal_dir_esq(tabuleiro)

    return result_soma_linha1 == result_soma_linha2 and \
           result_soma_linha1 == result_soma_linha3 and \
           result_soma_linha1 == result_soma_coluna1 and \
           result_soma_linha1 == result_soma_coluna2 and \
           result_soma_linha1 == result_soma_coluna3 and \
           result_soma_linha1 == result_soma_diagonal_esq_dir and \
           result_soma_linha1 == result_soma_diagonal_dir_esq


tabuleiro_valido_mock = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]

tabuleiro_invalido_mock = [
    [8, 3, 10],
    [1, 5, 9],
    [6, 7, 2]
]

assert validar_tabuleiro_e_quadrado_magico(tabuleiro_valido_mock)
assert not validar_tabuleiro_e_quadrado_magico(tabuleiro_invalido_mock)

print('Testes ok!')
