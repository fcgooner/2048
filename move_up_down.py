def move_up_down(direction, field, score):
    if direction == 'down':
        main_iter = 2
        last_index = -1
        first_index = 3
        change_iter = 1
    else:
        main_iter = 1
        last_index = 4
        first_index = 0
        change_iter = -1

    is_moved = False
    is_won = False

    while (direction == 'up' and main_iter < last_index) or (direction == 'down' and main_iter > last_index):
        k = main_iter
        while (direction == 'up' and k > first_index) or (direction == 'down' and k < first_index):
            y = 0
            while y < 4:
                if field[k + change_iter][y] == 0 and field[k][y] != 0:
                    field[k + change_iter][y] = field[k][y]
                    field[k][y] = 0
                    is_moved = True
                elif field[k + change_iter][y] == field[k][y] and (field[k + change_iter][y] + field[k][y]) != 0:
                    field[k + change_iter][y] += field[k][y]
                    field[k][y] = 0
                    score += field[k + change_iter][y]
                    is_moved = True
                    if field[k + change_iter][y] == 2048:
                        is_won = True

                y += 1

            k += change_iter

        main_iter -= change_iter

    return is_won, score, is_moved
