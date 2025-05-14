"""
N
S


5
RLURU
"""

moves = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}

x = 0
y = 0

num_moves = int(input())
S = list(input())

visited = set()
visited.add((x, y))

for i in range(len(S)):
    move_x, move_y = moves[S[i]]
    x += move_x
    y += move_y

    if (x, y) in visited:
        print("Yes")
        exit()

    visited.add((x, y))

print("No")
