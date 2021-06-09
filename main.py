a0, a1, a2, b0, b1, b2, c0, c1, c2 = '-', '-', '-', '-', '-', '-', '-', '-', '-',
X_moves, O_moves = [], []

def check_winning_x():
    if ['0', '0'] in X_moves and ['0', '1'] in X_moves and ['0', '2'] in X_moves:
        return True
    elif ['1', '0'] in X_moves and ['1', '1'] in X_moves and ['1', '2'] in X_moves:
        return True
    elif ['2', '0'] in X_moves and ['2', '1'] in X_moves and ['2', '2'] in X_moves:
        return True
    elif ['0', '0'] in X_moves and ['1', '0'] in X_moves and ['2', '0'] in X_moves:
        return True
    elif ['0', '1'] in X_moves and ['1', '1'] in X_moves and ['2', '1'] in X_moves:
        return True
    elif ['0', '2'] in X_moves and ['1', '2'] in X_moves and ['2', '2'] in X_moves:
        return True
    elif ['0', '0'] in X_moves and ['1', '1'] in X_moves and ['2', '2'] in X_moves:
        return True
    elif ['2', '0'] in X_moves and ['1', '1'] in X_moves and ['2', '0'] in X_moves:
        return True
    else:
        return False

def check_winning_o():
    if ['0', '0'] in O_moves and ['0', '1'] in O_moves and ['0', '2'] in O_moves:
        return True
    elif ['1', '0'] in O_moves and ['1', '1'] in O_moves and ['1', '2'] in O_moves:
        return True
    elif ['2', '0'] in O_moves and ['2', '1'] in O_moves and ['2', '2'] in O_moves:
        return True
    elif ['0', '0'] in O_moves and ['1', '0'] in O_moves and ['2', '0'] in O_moves:
        return True
    elif ['0', '1'] in O_moves and ['1', '1'] in O_moves and ['2', '1'] in O_moves:
        return True
    elif ['0', '2'] in O_moves and ['1', '2'] in O_moves and ['2', '2'] in O_moves:
        return True
    elif ['0', '0'] in O_moves and ['1', '1'] in O_moves and ['2', '2'] in O_moves:
        return True
    elif ['2', '0'] in O_moves and ['1', '1'] in O_moves and ['2', '0'] in O_moves:
        return True
    else:
        return False

def check_draw():
    if ((['0', '0'] in X_moves or ['0', '0'] in O_moves) and
            (['0', '1'] in X_moves or ['0', '1'] in O_moves) and
            (['0', '2'] in X_moves or ['0', '2'] in O_moves) and
            (['1', '0'] in X_moves or ['1', '0'] in O_moves) and
            (['1', '1'] in X_moves or ['1', '1'] in O_moves) and
            (['1', '2'] in X_moves or ['1', '2'] in O_moves) and
            (['2', '0'] in X_moves or ['2', '0'] in O_moves) and
            (['2', '1'] in X_moves or ['2', '1'] in O_moves) and
            (['2', '2'] in X_moves or ['2', '2'] in O_moves)):
        return True
    else:
        return False


def draw_the_field():
    global a0, a1, a2, b0, b1, b2, c0, c1, c2
    print(' ', 0, 1, 2)
    print(0, a0, a1, a2)
    print(1, b0, b1, b2)
    print(2, c0, c1, c2)

def check_moves(move_f):
    if move_f in X_moves or move_f in O_moves:
        print('Клетка занята. Введите координаты снова.', end=' ')
        return False
    elif not 0 <= int(move_f[0]) <= 2 or not 0 <= int(move_f[1]) <= 2:
        print('Введенный номер клетки некорректен. Введите координаты снова.', end=' ')
        return False
    return True

def make_x_move(move_func):
    global a0, a1, a2, b0, b1, b2, c0, c1, c2, X_moves, O_moves
    if move_func[0] == '0':
        if move_func[1] == '0':
            a0 = 'X'
            X_moves.append(['0', '0'])
        elif move_func[1] == '1':
            a1 = 'X'
            X_moves.append(['0', '1'])
        elif move_func[1] == '2':
            a2 = 'X'
            X_moves.append(['0', '2'])
    elif move_func[0] == '1':
        if move_func[1] == '0':
            b0 = 'X'
            X_moves.append(['1', '0'])
        elif move_func[1] == '1':
            b1 = 'X'
            X_moves.append(['1', '1'])
        elif move_func[1] == '2':
            b2 = 'X'
            X_moves.append(['1', '2'])
    elif move_func[0] == '2':
        if move_func[1] == '0':
            c0 = 'X'
            X_moves.append(['2', '0'])
        elif move_func[1] == '1':
            c1 = 'X'
            X_moves.append(['2', '1'])
        elif move_func[1] == '2':
            c2 = 'X'
            X_moves.append(['2', '2'])

def make_o_move(move_func):
    global a0, a1, a2, b0, b1, b2, c0, c1, c2, X_moves, O_moves
    if move_func[0] == '0':
        if move_func[1] == '0':
            a0 = 'O'
            O_moves.append(['0', '0'])
        elif move_func[1] == '1':
            a1 = 'O'
            O_moves.append(['0', '1'])
        elif move_func[1] == '2':
            a2 = 'O'
            O_moves.append(['0', '2'])
    elif move_func[0] == '1':
        if move_func[1] == '0':
            b0 = 'O'
            O_moves.append(['1', '0'])
        elif move_func[1] == '1':
            b1 = 'O'
            O_moves.append(['1', '1'])
        elif move_func[1] == '2':
            b2 = 'O'
            O_moves.append(['1', '2'])
    elif move_func[0] == '2':
        if move_func[1] == '0':
            c0 = 'O'
            O_moves.append(['2', '0'])
        elif move_func[1] == '1':
            c1 = 'O'
            O_moves.append(['2', '1'])
        elif move_func[1] == '2':
            c2 = 'O'
            O_moves.append(['2', '2'])

for i in range(1000):
    draw_the_field()
    if i % 2 == 0:
        while True:
            print('Введите строку и столбец через пробел:')
            move = input().split()
            if check_moves(move):
                make_x_move(move)
                break
            else:
                continue
    elif i % 2 == 1:
        while True:
            print('Введите строку и столбец через пробел:')
            move = input().split()
            if check_moves(move):
                make_o_move(move)
                break
            else:
                continue
    if check_winning_x():
        draw_the_field()
        print('Крестики победили. Игра окончена.')
        break
    elif check_winning_o():
        draw_the_field()
        print('Нолики победили. Игра окончена.')
        break
    elif check_draw():
        draw_the_field()
        print('Ничья. Игра окончена.')
        break