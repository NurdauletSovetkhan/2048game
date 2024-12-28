import random

class Game2048:
    def __init__(self):
        self.board = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.spawn_tile()
        self.spawn_tile()

    def spawn_tile(self):
        """Добавляем новую плитку 2 или 4 на случайную пустую клетку."""
        empty = [(x, y) for x in range(4) for y in range(4) if self.board[x][y] == 0]
        if empty:
            x, y = random.choice(empty)
            self.board[x][y] = 2 if random.random() < 0.9 else 4

    def can_merge(self):
        """Проверяем, есть ли возможность движения или слияния."""
        for x in range(4):
            for y in range(4):
                if self.board[x][y] == 0:
                    return True
                if x < 3 and self.board[x][y] == self.board[x + 1][y]:
                    return True
                if y < 3 and self.board[x][y] == self.board[x][y + 1]:
                    return True
        return False

    def compress(self, row):
        """Сдвиг строки влево (убираем нули)."""
        new_row = [x for x in row if x != 0]
        return new_row + [0] * (4 - len(new_row))

    def merge(self, row):
        """Объединяем одинаковые числа в строке."""
        for i in range(3):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i] *= 2
                row[i + 1] = 0
                self.score += row[i]
        return row

    def move_left(self):
        """Двигаем все строки влево."""
        new_board = []
        for row in self.board:
            compressed = self.compress(row)
            merged = self.merge(compressed)
            new_row = self.compress(merged)
            new_board.append(new_row)
        self.board = new_board

    def rotate_board(self):
        """Поворачиваем матрицу против часовой стрелки."""
        self.board = [list(row) for row in zip(*self.board[::-1])]

    def move(self, direction):
        if direction == 'left':
            self.rotate_board()
            self.rotate_board()
            self.move_left()
            self.rotate_board()
            self.rotate_board()
        elif direction == 'up':
            self.rotate_board()
            self.move_left()
            self.rotate_board()
            self.rotate_board()
            self.rotate_board()
        elif direction == 'down':
            self.rotate_board()
            self.rotate_board()
            self.rotate_board()
            self.move_left()
            self.rotate_board()
        elif direction == 'right':
            self.move_left()

    def is_game_over(self):
        """Проверяем, завершена ли игра."""
        if any(0 in row for row in self.board):
            return False
        if self.can_merge():
            return False
        return True
