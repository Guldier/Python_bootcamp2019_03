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
                elif item1._location_y == i and item1._location_x == j:
                    row += " * "
                elif item2._location_y == i and item2._location_x == j:
                    row += " * "
                else:
                    row += " . "
            print(row)
        print(player1._name, player1._emblemat, "+", player1._equipment._name, " | Life:", player1._health, " | A:",
              player1._strength, " | D:",
              player1._defence,
              " | R:", player1.attack_range, "/",
              "{:1.1f}".format(main_board.odleglosc_miedzy_playerami(player1, player2)), " | ", "Move: ")

    def odleglosc_miedzy_playerami(self, pl1, pl2):
        dist_x = math.fabs(pl1._pos_x - pl2._pos_x)
        dist_y = math.fabs(pl1._pos_y - pl2._pos_y)
        dist = math.sqrt(dist_x ** 2 + dist_y ** 2)
        return dist

    def ta_sama_loc(self, player, items):
        for i in items:
            if player._pos_y == i._location_y and player._pos_x == i._location_x:
                player.add_eq(i)
                i._location_y = -1
                i._location_x = -1


class Item:
    def __init__(self, name, plus_attack=random.randint(1, 10), plus_defence=random.randint(1, 10),
                 range=random.randint(1, 10), location_x=random.randint(1, 10), location_y=random.randint(1, 10)):
        self._name = name
        self._plus_attack = plus_attack
        self._plus_defence = plus_defence
        self._range = range
        self._location_x = location_x
        self._location_y = location_y


class Player:
    def __init__(self, name, emblemat):
        self._name = name
        self._health = 20
        self._defence = random.randint(1, 10)
        self._strength = random.randint(1, 10)
        self._pos_x = random.randint(1, 9)
        self._pos_y = random.randint(1, 9)
        self._equipment = None
        self.period_additional_def = 0
        self.attack_range = random.randint(1, 9)
        self._emblemat = emblemat

    def move(self, wsad):
        if wsad == 'w':
            if self._pos_y != 1:
                self._pos_y -= 1
        elif wsad == 's':
            if self._pos_y != 10:
                self._pos_y += 1
        elif wsad == 'a':
            if self._pos_x != 1:
                self._pos_x -= 1
        elif wsad == 'd':
            if self._pos_x != 10:
                self._pos_x += 1
        else:
            pass

    def introduce(self):
        print(f'Twoja postac to {self.name}\n'
              f'Health: {self.health}\n'
              f'Defance: {self.defence}\n'
              f'Strenth: {self.strengh}\n')

    @staticmethod
    def porownaj_postacie(self):
        

    def __str__(self):
        return f'{self._name}\n{self.attack_range}\n'

    def attack(self, distanse):
        if self.attack_range >= distanse:
            return self._strength + self._equipment._plus_attack
        else:
            return 0

    def defence(self, attack):

        additional_def = self._equipment._plus_defence
        if self.period_additional_def == 1:
            full_defence = self._defence + 1 + additional_def
        else:
            full_defence = self._defence + additional_def
        if attack - full_defence > 0:
            self._health -= attack - full_defence

    def add_eq(self, item):
        self._equipment = item

    def check_life(self):
        if self._health <= 0:
            return False


class Round:
    def __init__(self, turn):
        self._turn = 1
        self.end_game = False

    def next_round(self):
        self._turn += 1

    def walka(self, postac1, postac2, item1, item2):

        main_board.show_board(postac1, postac2, item1, item2)
        postac2.defence(postac1.attack(
            main_board.odleglosc_miedzy_playerami(postac1, postac2)))
        postac1.move(input())
        main_board.ta_sama_loc(postac1,[bow,sword])
        #if main_board.ta_sama_loc(postac1, [item1, item2]):
            #pass
        if postac2.check_life() is False:
            self.end_game = True


# ---------------------------------------------------------------------
if __name__ == "__main__":
    brak = Item('brak',0,0,0,-1,-1)

    player1 = Player("Waldek", " o ")
    player2 = Player("Pacek", " x ")

    player1.add_eq(brak)
    player2.add_eq(brak)

    bow = Item("Bow")
    sword = Item("Sword")

    main_board = Board()
    runda = Round(1)


    while True:
        runda.walka(player1, player2, sword, bow)
        if runda.end_game is True:
            break
        runda.walka(player2, player1, sword, bow)
        if runda.end_game is True:
            break

    for i in range(10):
        print()
    print("END")


# ---------------------------------------------------------------------

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

def test_porownanie_postaci(capsys):
    player1 = Player("Waldek", " o ")
    player2 = Player("Pacek", " x ")
    Player.porownaj_postac(player1,player2)
    captured = capsys.readouterr()
    assert captured == ""