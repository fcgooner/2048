from random import choice, randint, sample
from print_gamefield import fprint


# функція для заповнення пустих комірок на ігровому полі
# приймає 4 аргументи:
#   field               ігрове поле у вигляді двовимірного списку (матриця 4х4)
#   score               рахунок гравця (ціле число)
#   first_iteration     показує, чи перша ітерація циклу
#   is_moved            чи змінилося ігрове поле після ходу гравця

def fill_gamefield(field: list, score: int, first_iteration: bool = False, is_moved: bool = False):
    empty_space = []    # список кортежів (tuple) з координатами пустих комірок, наприклад [(0, 1), (3, 0)]

    # пробігаємось по ігровому полю по координатах
    for i in range(0, 4):
        for j in range(0, 4):
            # якщо значення в комірці == 0 (тобто, пусте), додаємо координати цієї комірки в список empty_space
            if field[i][j] == 0:
                empty_space.append((i, j))

    # перевіряємо, чи список не пустий
    if empty_space:
        # якщо не пустий, перевіряємо, чи це перша ітерація основного циклу
        if first_iteration:
            # якщо перша, створюємо список cells_to_fill, який містить дві випадкові комірки зі списку empty_space
            cells_to_fill = sample(empty_space, 2)
            # проходимо циклом по списку cells_to_fill з двох комірок
            for cell in cells_to_fill:
                x, y = cell                 # розпаковуємо кортеж в координати x, y
                field[x][y] = 2             # заповнюємо комірку значенням 2
                empty_space.remove(cell)    # видаляємо комірку зі списку пустих комірок
        else:
            # якщо не перша, перевіряємо, чи змінилось поле після ходу гравця
            if is_moved:
                # якщо змінилось, обираємо випадкову пусту комірку і заповнюємо її значенням 2
                x, y = (choice(empty_space))
                # генеруємо випадкове число від 1 до 100
                chance = randint(1, 100)
                if chance < 91:         # 90% шанс на пусте місце поставити 2
                    field[x][y] = 2
                else:                   # 10% шанс на пусте місце поставити 4
                    field[x][y] = 4
                empty_space.remove((x, y))  # видаляємо комірку зі списку пустих комірок

    # якщо це перша ітерація, або якщо ігрове поле змінилось після дій гравця, виводимо поле в консоль
    if first_iteration or is_moved:
        fprint(field, score)

    return empty_space
