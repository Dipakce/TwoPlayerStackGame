import random


def is_empty(lis1):
    if len(lis1) == 0:
        return 1
    else:
        return 0


class TwoPlayerGame:
    def __init__(self, sample_size):
        self.inputSize = int(sample_size)
        self.player1Numbers = random.sample(range(1, self.inputSize + 1), self.inputSize)
        self.player2Numbers = random.sample(range(1, self.inputSize + 1), self.inputSize)
        pass

    def play_game(self):
        print("Initial Number", self.player1Numbers, self.player2Numbers)

        while True:
            if is_empty(self.player1Numbers):
                print("Congratulation! Player1 won")
                break
            if is_empty(self.player2Numbers):
                print("Congratulation! Player2 won")
                break
            n1 = self.player1Numbers.pop()
            n2 = self.player2Numbers.pop()
            print(n1, n2)
            if n1 > n2:
                number_to_pop_from_p1 = n1 - n2
                i = 0
                while i < number_to_pop_from_p1:
                    if i >= len(self.player1Numbers):
                        break
                    num1 = self.player1Numbers.pop()
                    self.player2Numbers.append(num1)
                    i += 1
            elif n2 > n1:
                number_to_pop_from_p2 = n2 - n1
                j = 0
                while j < number_to_pop_from_p2:
                    if j >= len(self.player2Numbers):
                        break
                    num2 = self.player2Numbers.pop()
                    self.player1Numbers.append(num2)
                    j += 1
            else:
                continue

        if is_empty(self.player1Numbers) and is_empty(self.player2Numbers):
            print("Hard luck guys! Game has drawn")
