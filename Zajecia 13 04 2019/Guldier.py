import sys


class Board:
    player1_x = None
    player2_x = None
    player1_y = None
    player2_y = None

    def __init__(self):
        self.max_x = 10
        self.max_y = 10
        self.min_x = 0
        self.min_y = 0

    def show_board(self):
        for i in range(self.max_y):
            row=""
            for j in range(self.max_x):
                if player1.pos_y == i and player1.pos_x == j:
                     row += " o "
                if player2.pos_y == i and player2.pos_x == j:
                    row += " x "
                else:
                    row +=" . "
            print(row)
    def put_players(self, p1, p2):
        player1_x, player1_y = p1[0], p1[1]
        player2_x, player2_y = p2[0], p2[1]


class Item:
    def __init__(self, name, plus_attack, plus_defence, range):
        self.name = name
        self.plus_attack = plus_attack
        self.plus_defence = plus_defence
        self.range = range


class Player:
    def __init__(self, name, x, y):
        self.name = name
        self.health = 100
        self.defence = 10
        self.strengh = 5
        self.pos_x = x
        self.pos_y = y
        self.equipment = []

    def move(self, wsad):
        if wsad == 'w':
            self.pos_y += 1
        elif wsad == 's':
            self.pos_y -= 1
        elif wsad == 'a':
            self.pos_x -= 1
        elif wsad == 'd':
            self.pos_x += 1
        else:
            pass

    def introduce(self):
        print(f'Twoja postac to {self.name}\n'
              f'Health: {self.health}\n'
              f'Defance: {self.defence}\n'
              f'Strenth: {self.strengh}\n')

    @property
    def atakuj(self):
        atak = self.strengh
        for przedmiot in self.equipment:
            atak += przedmiot.plus_attack

    @property
    def obrona(self):
        return self.defence

    def add_equipment(self, item):
        self.equipment.append(item)


def show_board(x, y):
    for i in range(y):
        print(" . " * x)


player1 = Player("Waldek", 5, 5)
# player1.introduce()

player2 = Player("Pacek", 0, 0)
# player2.introduce()

main_board = Board()
main_board.put_players([player1.pos_x, player1.pos_y], [player2.pos_x, player2.pos_y])
main_board.show_board()


# bow = Item("Bow", 2, 0, 3)
# sword = Item("Sword", 3, 2, 1)
#
# player1 = Player("Waldek", 5, 5)
# player1.introduce()
#
# player2 = Player("Pacek", 0, 0)
# player2.introduce()
#
# while True:
#     input()
#     main_board.show_board()


def test_player_init():
    player1 = Player("Waldek", 5, 5)
    assert player1.name == "Waldek"
    # assert player1.equipment == "Sword"
    assert player1.pos_x == 5
    assert player1.pos_y == 5


def test_player_introduce(capsys):
    player1 = Player("Waldek", 5, 5)
    player1.introduce()
    captured = capsys.readouterr()
    assert captured.out == 'Twoja postac to Waldek\nHealth: 100\nDefance: 10\nStrenth: 5\n\n'


def test_player_add_equipment():
    player1 = Player("Waldek", 5, 5)
    sword = Item("Sword", 3, 2, 1)
    assert len(player1.equipment) == 0
    player1.add_equipment(sword)
    assert len(player1.equipment) == 1
