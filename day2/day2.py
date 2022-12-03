with open('input.txt') as f:
    total_score = 0
    '''
    A = X = Rock = 1
    B = Y = Paper = 2
    C = Z = Scissors = 3
    L = 0, D = 3, W = 6

                    1       2          3
                    Rock X    Paper Y   Scissors Z
    Rock        A    1+3        2+6         3+0
    Paper       B    1+0        2+3         3+6
    Scissors    C    1+6        2+0         3+3
    '''
    score_matrix = {('A', 'X'): 4, ('A', 'Y'): 8, ('A', 'Z'): 3,
                    ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9,
                    ('C', 'X'): 7, ('C', 'Y'): 2, ('C', 'Z'): 6}
    for line in f:
        total_score += score_matrix[tuple(line.split())]
    print(f'The total score is {total_score}')
