"""
N
S


5
RLURU
"""

moves = {
    "R": "+x",
    "L": "-x",
    "U": "+y",
    "D": "-y",
}

x = 0
y = 0

num_moves = int(input())
S = list(input())

cord = set()
cord.add((x, y))
for i in range(len(S)):
    if moves[S[i]] == "+x":
        x += 1
    elif moves[S[i]] == "-x":
        x -= 1
    elif moves[S[i]] == "+y":
        y += 1
    elif moves[S[i]] == "-y":
        y -= 1

    if len(cord) != (i + 1):
        print("Yes")
        exit()
    cord.add((x, y))

print("No")
