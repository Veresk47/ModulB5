field = [['-'] * 3 for i in range(3)]
def hello() :
    say = ('Привет, сыграем в крестики нолики?\n '
           'Правила просты:\n '
           'формат ввода Х и У\n '
           'X - номер строки\n '
           'Y - номер столбца')
    print(say)

def show() :
    print()
    print('     | 0 | 1 | 2 | ')
    print('  ----------------')
    for i, row in enumerate(field):
        row_str = f"   {i} | {' | '.join(row)} | "
        print(row_str)
        print('  ----------------')
    print()

def ask():
    while True:
        cords = input('Ваш ход, введите координаты: ').split()
        if len(cords) != 2 :
            print('Введите 2 координаты')
            continue
        x, y = cords
        if not(x.isdigit()) or not(y.isdigit()):
            print('Введите только числа! ')
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2 :
            print('Координаты вне диапозона!')
            continue
        if field[x][y] != '-':
            print('Клетка занята!')
            continue
        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!")
            return True
    return False

count = 0
while True:
    hello()
    count += 1

    show()

    if count % 2 == 1:
        print("Ходит крестик")
    else:
        print('Ходит нолик')

    x, y = ask()
    if count % 2 == 1 :
        field[x][y] = 'X'
    else:
        field[x][y] = 'O'
    if count == 9 :
        print('Ничья! Победила дружба :) ')
        break
    if check_win():
        break





