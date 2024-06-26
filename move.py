# функція прораховує зміну поля після ходу гравця
# приймає 3 аргументи:
#   direction           хід гравця (вверх, вниз, вліво, вправо)
#   field               ігрове поле у вигляді двовимірного списку (матриця 4х4)
#   score               рахунок гравця (ціле число)

# АЛГОРИТМ ПЕРЕВІРКИ:
#                               Яку кнопку натиснув гравець, у ту сторону мають зміститися числа.
#        0  1  2  3             Наприклад, якщо гравець натиснув кнопку вверх, числа в нульвому рядку ми
#        ----------             змістити вверх не зможемо, бо вийдемо за межі поля, тому початковий рядок матиме
#   0 |  0  2  2  4             індекс 1, наступний рядок – індекс 2 (+1), а останній – 3, тобто під час перевірки
#   1 |  0  0  0  0             ми завжди рухаємось у зворотньому напрямку.
#   2 |  0  0  0  0             Якщо гравець натиснув кнопку вниз, то початковий рядок матиме індекс 2
#   3 |  0  0  0  0             наступний – 1 (-1), а останній – 0.
#
#                               У випадку вліво/вправо перевірка буде йти по стовпцях, а не рядках, але логіка
#                               лишається тою самою:
#                                 * якщо гравець натиснув вліво, індекс почтакового стовпця буде 1,
#                                   наступного – 2 (+1), останнього – 3
#
#                                 * якщо гравець натиснув вправо, індекс почтакового стовпця буде 2,
#                                   наступного – 1 (-1), останнього – 0
#
#                               До того ж, кожен наступний рядок/стовпець робить свою перевірку + повторює
#                               всі попередні.
#
#                               Для прикладу візьмемо рядок 0 2 2 4, який після завершення ходу має перетворитись на
#                               4 4 0 0, за умови, що гравець натиснув вліво.
#                               Чому 4 4 0 0, а не 8 0 0 0? Гра має правило, що одна комірка за один хід може
#                               буде об’єднана лише 1 раз.
#
#                               Згідно інформації вище, індекс початкового стовпця - 1, наступного - 2, останнього - 3.
#
#                               1. Перевіримо елемент[0][1] (цифра 2) і елемент[0][0] (цифра 0).
#                                  Оскільки 2 > 0, зміщуємо 2 вліво, і тепер елемент[0][0] == 2, а елемент[0][1] == 0.
#                                  Рядок має такий вигляд: 2 0 2 4
#                               2. Рухаємось далі, індекс початкового стовпця - 2, наступного - 3, останнього - 3.
#                                  Перевіримо елемент[0][2] (цифра 2) і елемент[0][1] (цифра 0).
#                                  2 > 0, зміщуємо 2 вліво, елемент[0][1] == 2, елемент[0][2] == 0, рядок -> 2 2 0 4
#
#                               3. Тепер нам знову треба перевірити елементи з кроку 1:
#                                    * [0][1] (цифра 2) і елемент[0][0] (цифра 2)
#                                    * оскільки 2 == 2, до елемента[0][0] додаємо елемент[0][1]
#                                    * тепер елемент[0][0] == 4, елемент[0][1] == 0, рядок -> 4 0 0 4
#                               4. Рухаємось далі, індекс початкового стовпця - 3, останнього - 3.
#                                  Оскільки індекс початкового стовпця == індексу останнього, отже, ми дійшли до кінця.
#                                  Перевіримо елемент[0][3] (цифра 4) і елемент[0][2] (цифра 0).
#                                  Оскільки 4 > 0, зміщуємо 4 вліво, і тепер елемент[0][2] == 4, елемент[0][3] == 0,
#                                  рядок -> 4 0 4 0
#                               5. Перевіримо елемент[0][3] (цифра 4) і елемент[0][1] (цифра 0).
#                                  Оскільки 4 > 0, зміщуємо 4 вліво, і тепер елемент[0][1] == 4, елемент[0][2] == 0,
#                                  рядок -> 4 4 0 0
#                               6. Оскільки в елементі[0][0] вже відбулось об’єднання на кроці 3, об’єднувати 4 і 4
#                                  цього ходу ми вже не можемо, тому перевірку для цього рядка закінчено.
#
#                               Повний цикл перевірки одного рядка/стовпця:
#                                   0 2 2 4 -> 2 0 2 4 -> 2 2 0 4 -> 4 0 0 4 -> 4 0 4 0 -> 4 4 0 0
#


def move(direction, field, score):
    # start_position    індекс початкового рядка/стовпця
    # out_of_bounds     індекс рядка/стовпця за межами ігрового поля
    # end_index         індех останнього рядка/стовпця
    # next_index        індекс наступного рядка/стовпця буде меншим на 1 (вниз*вправо), або більшим на 1 (вверх/вліво)

    if direction == 'down' or direction == 'right':
        start_position = 2
        out_of_bounds = -1
        end_index = 3
        next_index = 1
    else:
        start_position = 1
        out_of_bounds = 4
        end_index = 0
        next_index = -1

    is_moved = False        # змінилося поле чи ні
    is_won = False          # чи зібрав гравець 2048
    already_shifted = []    # список, який містить координати комірок, де вже відбулось об’єднання
    while (direction in ['left', 'up'] and start_position < out_of_bounds) or (
            direction in ['right', 'down'] and start_position > out_of_bounds):
        i = start_position
        while (direction in ['left', 'up'] and i > end_index) or (direction in ['right', 'down'] and i < end_index):
            j = 0
            if direction in ['up', 'down']:
                x1, x2 = (i + next_index, i)    # якщо вверх/вниз, спочатку рухаємось по рядках, а потім по стовпцях
            else:  # left, right
                y1, y2 = (i + next_index, i)    # якщо вліво/вправо, спочатку рухаємось по стовпцях, а потім по рядках

            while j <= 3:
                if direction in ['up', 'down']:
                    y1, y2 = (j, j)             # якщо вверх/вниз, спочатку рухаємось по рядках, а потім по стовпцях
                else:  # left, right
                    x1, x2 = (j, j)             # якщо вліво/вправо, спочатку рухаємось по стовпцях, а потім по рядках

                # якщо елемент, в сторону якого відбувається зміщення == 0, а інший > 0, то робимо зміщення
                if field[x1][y1] == 0 and field[x2][y2] > 0:
                    field[x1][y1] = field[x2][y2]
                    field[x2][y2] = 0
                    is_moved = True

                # якщо елемент, в сторону якого відбувається зміщення == іншому елементу, і вони не == 0
                # (якщо два елементи == 0, то робити зміщення немає сенсу)
                elif field[x1][y1] == field[x2][y2] and (field[x1][y1] + field[x2][y2]) != 0:
                    # якщо в комірці ще не було об’єднання, то робимо зміщення
                    if (x1, y1) not in already_shifted and (x2, y2) not in already_shifted:
                        field[x1][y1] += field[x2][y2]
                        field[x2][y2] = 0
                        score += field[x1][y1]              # додаємо суму до загального рахунку
                        is_moved = True
                        already_shifted.append((x1, y1))    # додаємо координати комірки до списку об’єднаних комірок
                        if field[x1][y1] == 2048:           # якщо гравець зібрав 2048, вказуємо, що він виграв
                            is_won = True

                j += 1

            i += next_index

        start_position -= next_index

    return is_won, score, is_moved
