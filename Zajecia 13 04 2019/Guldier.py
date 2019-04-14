import random
import math


class Board:

    def __init__(self):
        self._max_x = 10
        self._max_y = 10
        self._min_x = 0
        self._min_y = 0

    def show_board(self, player1, player2, item1, item2):
        for i in range(self._max_y):
            row = ""
            for j in range(self._max_x):
                if player1._pos_y == i and player1._pos_x == j:
                    row += player1._emblemat
                elif player2._pos_y == i and player2._pos_x == j:
                    row += player2._emblemat
                elif item1[1] == i and item1[0] == j:
                    row += " * "
                elif item2[1] == i and item2[0] == j:
                    row += " * "
                else:
                    row += " . "
            print(row)
        print(player1._name, player1._emblemat, " | Life:", player1._health, " | A:", player1._strength, " | D:",
              player1._defence,
              " | R:", player1.attack_range, " | ", "Move: ")
        # print(defensor, " | ", defe_life, " | ", "Move: ")

    def odleglosc_miedzy_playerami(self, pos1_x, pos1_y, pos2_x, pos2_y):
        dist_x = math.fabs(pos1_x - pos2_x)
        dist_y = math.fabs(pos1_y - pos2_y)
        dist = math.sqrt(dist_x ** 2 + dist_y ** 2)
        return dist


class Item:
    def __init__(self, name):
        self._name = name
        self._plus_attack = random.randint(1, 10)
        self._plus_defence = random.randint(1, 10)
        self._range = random.randint(1, 10)
        self._location_x = random.randint(1, 9)
        self._location_y = random.randint(1, 9)


class Player:
    def __init__(self, name, emblemat):
        self._name = name
        self._health = 20
        self._defence = random.randint(1, 10)
        self._strength = random.randint(1, 10)
        self._pos_x = random.randint(1, 9)
        self._pos_y = random.randint(1, 9)
        self._equipment = []
        self.period_additional_def = 0
        self.attack_range = random.randint(1, 9)
        self._emblemat = emblemat

    def move(self, wsad):
        if wsad == 'w':
            if self._pos_y != 1:
                self._pos_y -= 1
        elif wsad == 's':
            if self._pos_y != 11:
                self._pos_y += 1
        elif wsad == 'a':
            if self._pos_x != 1:
                self._pos_x -= 1
        elif wsad == 'd':
            if self._pos_x != 11:
                self._pos_x += 1
        else:
            pass

    def introduce(self):
        print(f'Twoja postac to {self.name}\n'
              f'Health: {self.health}\n'
              f'Defance: {self.defence}\n'
              f'Strenth: {self.strengh}\n')

    def attack(self, distanse):
        if self.attack_range >= distanse:
            if len(self._equipment) > 1:
                for items in self._equipment:
                    power = self._strength + items._plus_attack
            else:
                power = self._strength
            return power
        else:
            return 0

    def defence(self, attack):
        additional_def = 0
        for items in self._equipment:
            additional_def = items._plus_defence
        if self.period_additional_def == 1:
            full_defence = self._defence + 1 + additional_def
        else:
            full_defence = self._defence + additional_def
        if attack - full_defence > 0:
            self._health -= attack - full_defence

    def add_eq(self, item):
        self._equipment.append(item)

    def check_life(self):
        if self._health <= 0:
            return False


class Round:
    def __init__(self, turn):
        self._turn = 1
        self.end_game = False

    def next_round(self):
        self._turn += 1

    def walka(self, postac1, postac2):
        main_board.show_board(postac1, postac2,
                              [sword._location_x, sword._location_y], [bow._location_x, bow._location_y])
        postac1.move(input())
        postac2.defence(postac1.attack(
            main_board.odleglosc_miedzy_playerami(postac1._pos_x, postac1._pos_y, postac2._pos_x, postac2._pos_y)))
        if postac2.check_life() is False:
            self.end_game = True


player1 = Player("Waldek", " o ")
# player1.introduce()
player2 = Player("Pacek", " x ")
# player2.introduce()
bow = Item("Bow")
sword = Item("Sword")

main_board = Board()
runda = Round(1)
# main_board.put_players([player1.pos_x, player1.pos_y], [player2.pos_x, player2.pos_y])
while True:
    runda.walka(player1, player2)
    if runda.end_game is True:
        break
    runda.walka(player2, player1)
    if runda.end_game is True:
        break

for i in range(10):
    print()
print("END")


# print(main_board.odleglosc_miedzy_playerami(player1._pos_x, player1._pos_y, player2._pos_x, player2._pos_y))


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
