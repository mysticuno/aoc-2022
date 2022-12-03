with open('input.txt') as f:
    total_score = 0
    '''
    A = Rock = 1
    B = Paper = 2
    C = Scissors = 3
    X = Lose = 0
    Y = Draw = 3
    Z = Win = 6

                    1            2           3
                    Lose X       Draw Y      Win Z
    Rock        A   3+0 (s)      1+3 (r)     2+6 (p)
    Paper       B   1+0 (r)      2+3 (p)     3+6 (s)
    Scissors    C   2+0 (p)      3+3 (s)     1+6 (r)
    '''
    score_matrix = {('A', 'X'): 3, ('A', 'Y'): 4, ('A', 'Z'): 8,
                    ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9,
                    ('C', 'X'): 2, ('C', 'Y'): 6, ('C', 'Z'): 7}
    for line in f:
        total_score += score_matrix[tuple(line.split())]
    print(f'The total score is {total_score}')
