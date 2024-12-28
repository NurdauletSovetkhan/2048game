from ui import draw_board, show_game_over, get_user_input
from game import Game2048

def main():
    # Создаем объект игры
    game = Game2048()

    while True:
        # Рисуем игровое поле
        draw_board(game)

        # Получаем пользовательский ввод
        command = get_user_input()

        if command == 'quit':
            # Завершение игры
            show_game_over(game)
            break

        if command in ['up', 'down', 'left', 'right']:
            # Делаем движение и добавляем новую плитку, если поле изменилось
            previous_board = [row[:] for row in game.board]  # Сохраняем копию доски
            game.move(command)

            if previous_board != game.board:
                game.spawn_tile()

            # Проверяем окончание игры
            if game.is_game_over():
                draw_board(game)
                show_game_over(game)
                break

if __name__ == "__main__":
    main()
