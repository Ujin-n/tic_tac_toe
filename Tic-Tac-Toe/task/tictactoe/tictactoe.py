def print_field():
    print("---------")
    print(f'| {tic_tac_toe_list[0][0]} {tic_tac_toe_list[0][1]} {tic_tac_toe_list[0][2]} |')
    print(f'| {tic_tac_toe_list[1][0]} {tic_tac_toe_list[1][1]} {tic_tac_toe_list[1][2]} |')
    print(f'| {tic_tac_toe_list[2][0]} {tic_tac_toe_list[2][1]} {tic_tac_toe_list[2][2]} |')
    print("---------")


def check_win(letter):
    for i in range(3):
        # check rows
        if tic_tac_toe_list[i][0] == letter and tic_tac_toe_list[i][1] == letter and tic_tac_toe_list[i][2] == letter:
            return True
        # check columns
        elif tic_tac_toe_list[0][i] == letter and tic_tac_toe_list[1][i] == letter and tic_tac_toe_list[2][i] == letter:
            return True

    # check diagonal
    if (tic_tac_toe_list[0][0] == letter and tic_tac_toe_list[1][1] == letter and tic_tac_toe_list[2][2] == letter) or \
            (tic_tac_toe_list[0][2] == letter and tic_tac_toe_list[1][1] == letter and tic_tac_toe_list[2][0] == letter):
        return True

    return False


coord_mapping = {'1 1': '2 0',
                 '1 2': '1 0',
                 '1 3': '0 0',
                 '2 1': '2 1',
                 '2 2': '1 1',
                 '2 3': '0 1',
                 '3 1': '2 2',
                 '3 2': '1 2',
                 '3 3': '0 2'}

tic_tac_toe_list = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

print_field()

count = 1
while True:
    turn = 'X' if count % 2 != 0 else 'O'

    coordinates = input("Enter the coordinates: > ")
    try:
        v1, v2 = coordinates.split()
        v1, v2 = int(v1), int(v2)
    except ValueError:
        print("You should enter numbers!")
        continue

    if (v1 < 1 or v1 > 3) or (v2 < 1 or v2 > 3):
        print("Coordinates should be 1 to 3!")
        continue

    x, y = coord_mapping.get(coordinates).split()
    x, y = int(x), int(y)

    if tic_tac_toe_list[x][y] == '_':
        tic_tac_toe_list[x][y] = turn
    else:
        print("This cell is occupied! Choose another one!")
        continue

    print_field()

    count += 1
    empty_count = tic_tac_toe_list[0].count('_') + tic_tac_toe_list[1].count('_') + tic_tac_toe_list[2].count('_')

    if check_win(turn):
        print(turn + ' wins')
        exit()
    elif not empty_count:
        print('Draw')
        exit()
