from fill_gamefield import fill_gamefield
from press_key import press_key
from print_gamefield import fprint
from move import move
from check_moves import check_moves


def start_2048():                   # Основна функція гри
    # Створення ігрового поля
    field = [
        # 0  1  2  3
        [0, 0, 0, 0], # 0
        [0, 0, 0, 0], # 1
        [0, 0, 0, 0], # 2
        [0, 0, 0, 0]  # 3
    ]
    # field = [
    #   # 0  1  2  3
    #    [0, 0, 0, 0], # 0
    #    [2, 8, 0, 256], # 1
    #    [2, 1024, 8, 0], # 2
    #    [32, 4, 2, 2]  # 3
    # ]

    # Ініціалізація початкових змінних
    score = 0               # очки гравця
    first_iteration = True  # показує чи це перша ітерація циклу (перед першим ходом дві комірки заповнюються двійками)
    is_moved = False        # показує чи змінилося поле після ходу гравця
    is_won = False          # показує, чи виграв гравець (зібрав 2048)

    # початок циклу гри – гра триватиме, поки ми примусово не вийдемо з циклу за допомогою break
    while True:
        # перевіряємо чи це не перша ітерація і чи гравець виграв
        if not first_iteration and is_won:
            # якщо це не перша ітерація і граеець виграв,
            # виводимо в консоль ігрове поле, фінальний рахунок і закриваємо гру (виходимо з циклу гри)
            fprint(field, score)
            print(f'\nВітаємо! Ви перемогли!\nВаш фінальний рахунок: {score}')
            break

        # заповнюємо випадковим чином пусту комірку (або дві, якщо це перша ітерація) двійкою
        # змінна empty_space містить список кортежів, які є координатами пустих комірок
        empty_space = fill_gamefield(field, score, first_iteration, is_moved)

        # перевірямо, чи залишились на ігровому полі пусті комірки
        if not empty_space:
            # якщо пустих комірок немає, викликаємо функцію, яка перевіряє чи є у гравця доступні ходи
            # результат виконання функції (True, False) записуємо в змінну moves_available
            moves_available = check_moves(field)
        else:
            # якщо пусті комірки є, то у гравця точно є доступні ходи (як мінімум 1)
            moves_available = True
        
        # перевіряємо, чи є у гравця доступні ходи
        if not moves_available:
            # якщо немає, гравець програв
            # виводимо фінальний рахунок і виходимо з циклу гри (break)
            print(f'\nНе залишилось доступних ходів. Ви програли.\nВаш фінальний рахунок: {score}')
            break

        # у змінну pressed_key записуємо кнопку, яку натиснув гравець
        pressed_key = press_key()

        # перевіряємо, яку кнопку натиснув гравець і викликаємо відповідну функцію
        # записуємо в змінні результат виконання функції:
        #   is_won      показує чи гравець аиграв
        #   score       оновлений рахунок гравця
        #   is_moved    показує чи змінилося ігрове поле

        is_won, score, is_moved = move(pressed_key, field, score)

        # У кінці ітерації перевіряємо, чи це була перша ітерація
        # якщо перша, то змінюємо значення на False
        if first_iteration:
            first_iteration = False


# Запускаємо основну функцію гри
while True:
    start_2048()
    continue_game = input("\nХочете зіграти знову?\n(так/ні): ")
    if continue_game.lower() not in ['так', 'т', 'yes', 'y']:
        print('\nДякуємо за гру!')
        break

