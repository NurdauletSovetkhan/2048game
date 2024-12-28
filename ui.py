from blessed import Terminal

# Создаем экземпляр терминала
term = Terminal()


def draw_board(game):
    with term.location(0, 0):
        print(term.clear)
        print(term.bold(term.blue("Game is  - Terminal Edition\n")))

        # Отображение текущего счета
        print(f"Score: {game.score}\n")

        # Отрисовка поля
        for row in game.board:
            line = ""
            for cell in row:
                if cell == 0:
                    line += term.on_white("     ")  # Пустая клетка
                else:
                    line += term.on_yellow(term.bold(f"{cell:5}"))
                line += " "  # Пробел между ячейками
            print(line)
            print()
        print("\nUse arrow keys to play. Press 'q' to quit.\n")


def show_game_over(game):
    with term.cbreak(), term.hidden_cursor():
        print(term.clear + term.home)
        print(term.red(term.bold("Game Over!")))
        print(f"Your final score: {game.score}\n")
        print("Press 'q' to quit.")


def get_user_input():

    with term.cbreak():
        key = term.inkey(timeout=None)
        if key.code == term.KEY_UP:
            return 'down'
        elif key.code == term.KEY_DOWN:
            return 'up'
        elif key.code == term.KEY_LEFT:
            return 'right'
        elif key.code == term.KEY_RIGHT:
            return 'left'
        elif key.lower() in ['q', 'Q']:
            return 'quit'
        return None
