

def print_field(field: list) -> None:
    for row in field:
        for cell in row:
            print((cell, end= ''))
    print()

from logic import init_field, set_cell, is_win, is_available_cell
def get_step(field:list,player_symbol: str) -> tuple[int,int]:
    while True:
    step = input(f"Игрок {player_symbol} введите координату от 1-9: ")
    if not step.isdigit():
        print("Вы ввели не число. Повторите ввод")
        continue

    int_step = int (step)
    if not 1 <= int_step <= 9:
        print("Вы не вввкли правильный индекс")
        continue
    field_size = 3
    X = int_step // field_size -1
    Y = int_step % field_size - 1
    if not is empty_cell (x, y, field):
        print("Ячейка занята. Повторите ввод")
        continue
    return x, y

def main():
    size_field = 3
    field = init_field()
    print_field(field)
    first_player, second_player = "X", "0"

    while True:

    row_index, col_index = get_step(field, first_player)
    set_cell(field, row_index, col_index, first_player)
    print_field(field)
    if is_win(field):
        print(f"Победил игрок {first_player}")
        breake


    row_index, col_index = get_step(field, second_player)
    set_cell(field, row_index, col_index, second_player)

    if is_win(field):
        print(f"Победил игрок {second__player}")
        breake
    if not is_available_cell(field)
        print("Ничья")
        break

if __name__ == '__main__'