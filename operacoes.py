
def soma_linha(linha):
    return sum(linha)

def soma_coluna(tabuleiro, indice_coluna):
    soma = 0
    for linha in tabuleiro:
        soma += linha[indice_coluna]
    return soma

def soma_diagonal_esq_dir(tabuleiro):
    soma = 0
    for indice, linha in enumerate(tabuleiro):
        soma += linha[indice]
    return soma

def soma_diagonal_dir_esq(tabuleiro):
    soma = 0
    for indice, linha in enumerate(tabuleiro):
        ultimo_indice = len(linha) - 1
        soma += linha[ultimo_indice - indice]
    return soma

tabuleiro_mock = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]

assert soma_linha(tabuleiro_mock[0]) == 15
assert soma_linha(tabuleiro_mock[1]) == 15
assert soma_linha(tabuleiro_mock[2]) == 15

assert soma_coluna(tabuleiro_mock, 0) == 15
assert soma_coluna(tabuleiro_mock, 1) == 15
assert soma_coluna(tabuleiro_mock, 2) == 15

assert soma_diagonal_esq_dir(tabuleiro_mock) == 15
assert soma_diagonal_dir_esq(tabuleiro_mock) == 15

print('Testes ok!')
