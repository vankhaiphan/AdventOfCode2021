import numpy as np
import re


class Board:
    # Implement boards as a class
    def __init__(self, nums):
        self.board = [
            [[nums[i][j], False] for j in range(5)]
            for i in range(5)
        ]

    def detect_win(self):
        for row in range(5):
            if all([self.board[row][i][1] for i in range(5)]):
                return True
        for col in range(5):
            if all([self.board[i][col][1] for i in range(5)]):
                return True
        return False

    def get_score(self, last_called):
        uncalled_sum = 0
        for row in range(5):
            for col in range(5):
                if not self.board[row][col][1]:
                    uncalled_sum += self.board[row][col][0]

        return uncalled_sum * last_called

    def mark(self, num):
        for row in self.board:
            for el in row:
                if el[0] == num:
                    el[1] = True


def parse_board(lines):
    """
    lines: a list of 5 strings
    """
    return [[int(i) for i in re.split(" +", line.strip())] for line in lines]


# Parsing input...
with open("input.txt") as fin:
    data = fin.read().strip().split("\n")

nums = [int(i) for i in data[0].split(",")]

boards = []
i = 2
while i < len(data):
    x = parse_board(data[i:i+5])
    boards.append(Board(x))
    i += 6

# Run the simulation!
winning_order = []
for x in nums:
    for i in range(len(boards)):
        boards[i].mark(x)

        if i not in winning_order and boards[i].detect_win():
            winning_order.append(i)

    # If all the boards are done, break
    if len(winning_order) == len(boards):
        break

# Find the board that wins last
ans = boards[winning_order[-1]].get_score(x)
print(ans)