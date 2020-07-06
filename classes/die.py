from random import randint, choice


class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


dies = {
    "six": Die(6),
    "ten": Die(10),
    "twenty": Die(20),
}

# for (name, obj) in dies.items():
#     for val in range(0, 10):
#         print(f"Результат броска {obj.sides}-гранного кубика: {obj.roll_die()}")

lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "a", "b", "c", "d", "e"]


def play_lottery():
    combination = []
    lot = lottery[:]
    for i in range(0, 4):
        i
        number = lot.pop(randint(0, len(lot) - 1))
        combination.append(number)
    return combination


winner = play_lottery()
print(f"Комбинация {winner} является выигрышной")
counter = 0
while True:
    counter += 1
    combine = play_lottery()
    if winner == combine:
        print(f"Понадобилось {counter} попыток")
        break
