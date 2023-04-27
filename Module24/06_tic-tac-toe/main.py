class Cell:
    def __init__(self, num: int, symbol: str):
        self.num = num
        self.symbol = symbol
        self.busy = False

    def __str__(self):
        return self.symbol


class Board:
    victories_lines = ((0, 1, 2), (3, 4, 5), (6, 7, 8),     # Выигрышные комбинации
                       (0, 3, 6), (1, 4, 7), (2, 5, 8),
                       (0, 4, 8), (2, 4, 6))

    def __init__(self):
        self.cells = []
        for i in range(9):
            self.cells.append(Cell(i, str(i + 1)))

    def display(self):
        for i in range(3):
            print('-------------')
            out = '| '
            for j in range(3):
                out += str(self.cells[i * 3 + j]) + ' | '
            print(out)
        print('-------------')

    def update(self, cell_num, symbol):
        if self.cells[cell_num - 1].busy is False:
            self.cells[cell_num - 1].symbol = symbol
            self.cells[cell_num - 1].busy = True
            return True
        else:
            return False

    def check_game_over(self):
        for i in self.victories_lines:
            if self.cells[i[0]].symbol == self.cells[i[1]].symbol == self.cells[i[2]].symbol:
                return True
        return False


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.score = 0

    def make_move(self):
        try:
            cell_num = int(input(f'{self.name}, введите номер клетки: '))
            return cell_num
        except ValueError:
            print('Вы ввели не число.')
            return self.make_move()


class Game:
    def __init__(self, _player1, _player2):
        self.player1 = _player1
        self.player2 = _player2
        self.board = Board()
        self.current_player = _player1

    def play_turn(self):
        self.board.display()
        cell_num = self.current_player.make_move()
        while not self.board.update(cell_num, self.current_player.symbol):
            print('Клетка занята')
            cell_num = self.current_player.make_move()

        if self.board.check_game_over():
            print(f'{self.current_player.name} Победил!\n')
            self.board.display()
            self.current_player.score += 1
            return True

        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

        return False

    def play_game(self):
        while True:
            print('Новая игра!')
            turn_counter = 0
            self.board = Board()
            self.current_player = self.player1

            while not self.board.check_game_over():     # Игроки ходят
                if self.play_turn():
                    break
                turn_counter += 1
                if turn_counter == 9:   # Ходы закончились
                    player1.score += 0.5
                    player2.score += 0.5
                    print('\nНичья')
                    break

            print('Текущий счёт:')
            print(f'{self.player1.name}: {str(self.player1.score)}')
            print(f'{self.player2.name}: {str(self.player2.score)}')

            new_game = input('Начать новую игру? (Y/N): ')
            if new_game.lower() != 'y':
                break


name1 = input('Имя первого игрока: ')
name2 = input('Имя второго игрока: ')
player1 = Player(name1, 'X')
player2 = Player(name2, 'O')

game = Game(player1, player2)
game.play_game()

print('Программа завершена!')
