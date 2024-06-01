import keyboard

# функція, яка повертає назву натиснутої гравцем кнопки


def press_key():

    # цикл функції буде виконуватись, доки гравець не натисне одну з кнопок зі списку controls
    while True:
        controls = ['left', 'up', 'right', 'down']

        # викликаємо функцію з бібліотеки keyboard,
        # яка зчитує кнопки і записуємо назву натиснутої кнопки в змінну key_pressed
        key_pressed = keyboard.read_event(suppress=True)

        # перевіряємо, чи гравець відпустив кнопку
        if key_pressed.event_type == keyboard.KEY_UP:
            # якщо відпустив, перевіряємо, чи кнопка є в списку controls
            if key_pressed.name in controls:
                # якщо є, повертаємо назву цієї кнопки і закінчуємо виконання функції
                return key_pressed.name
