import time

def solve_n_queens(n):
    # Esta função principal irá encontrar todas as soluções possíveis para o problema N-Queens.

    def create_board(state):
        # Esta função interna cria uma representação de tabuleiro com base no estado atual.
        # O estado é uma lista que mantém o índice da coluna onde uma rainha está localizada para cada linha.
        board = []
        for row in state:
            # Para cada rainha (representada por seu índice de coluna na lista 'state'),
            # uma string é criada com um 'Q' na posição da rainha e '.' em todas as outras posições.
            board.append('.' * row + 'Q' + '.' * (n - row - 1))
        return board

    def is_safe(state, row, col):
        # Esta função verifica se é seguro colocar uma rainha na posição (row, col).
        # Ela precisa verificar apenas para as rainhas já colocadas (acima da linha atual).
        for i in range(row):
            if state[i] == col or \
               state[i] - i == col - row or \
               state[i] + i == col + row:
                # Retorna False se há uma rainha na mesma coluna ou nas diagonais.
                return False
        return True

    def place_queens(row, state):
        # Esta função tenta colocar uma rainha na linha 'row' e chama-se recursivamente
        # para tentar colocar as próximas rainhas.
        if row == n:
            # Se todas as 'n' rainhas foram colocadas com sucesso,
            # adicione a configuração atual do tabuleiro à lista de resultados.
            result.append(create_board(state))
        else:
            # Caso contrário, tente colocar uma rainha em cada coluna da linha atual.
            for col in range(n):
                if is_safe(state, row, col):
                    # Se for seguro, escolha essa posição para a rainha.
                    state[row] = col
                    # Continue para a próxima linha (recursão).
                    place_queens(row + 1, state)
                    # Após retornar da recursão, desfaça a escolha para tentar uma nova posição.
                    state[row] = None

    result = []
    place_queens(0, [None]*n)
    # Começa a recursão a partir da linha 0 e com um estado inicial sem rainhas.
    return result
    # Retorna a lista de soluções encontradas.

# Exemplo de uso da função para um tabuleiro 4x4.
n = 12
solutions = solve_n_queens(n)
# Imprime todas as soluções encontradas.
solucoes = 0
start_time = time.time()
for solution in solutions:
    
    for row in solution:
        print(row)
    solucoes += 1
    print("")
    print(solucoes)
end_time = time.time()
print(f"Tempo de execução do BFS: {end_time - start_time:.2f} segundos")

