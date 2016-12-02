map = "L4, R2, R4, L5, L3, L1, R4, R5, R1, R3, L3, L2, L2, R5, R1, L1, L2, R2, R2, L5, R5, R5, L2, R1, R2, L2, L4, L1, R5, R2, R1, R1, L2, L3, R2, L5, L186, L5, L3, R3, L5, R4, R2, L5, R1, R4, L1, L3, R3, R1, L1, R4, R2, L1, L4, R5, L1, R50, L4, R3, R78, R4, R2, L4, R3, L4, R4, L1, R5, L4, R1, L2, R3, L2, R5, R5, L4, L1, L2, R185, L5, R2, R1, L3, R4, L5, R2, R4, L3, R4, L2, L5, R1, R2, L2, L1, L2, R2, L2, R1, L5, L3, L4, L3, L4, L2, L5, L5, R2, L3, L4, R4, R4, R5, L4, L2, R4, L5, R3, R1, L1, R3, L2, R2, R1, R5, L4, R5, L3, R2, R3, R1, R4, L4, R1, R3, L5, L1, L3, R2, R1, R4, L4, R3, L3, R3, R2, L3, L3, R4, L2, R4, L3, L4, R5, R1, L1, R5, R3, R1, R3, R4, L1, R4, R3, R1, L5, L5, L4, R4, R3, L2, R1, R5, L3, R4, R5, L4, L5, R2"
# solver
#map = "R8, R4, R4, R8"

# movements = N E S W
movements = ((0, 1), (1, 0), (0, -1), (-1, 0))
position = [0, 0]

d = 0

visited_positions = dict()
found = False

for splitted in map.split(", "):
    direction = -1 if splitted[0] == "L" else 1
    len = int(splitted[1:])

    d = (d + direction) % 4

    for i in range(0, len):
        position[0] = position[0] + movements[d][0]
        position[1] = position[1] + movements[d][1]

        if tuple(position) in visited_positions:
            found = True
            break
        else:
            visited_positions[tuple(position)] = True

    if found == True:
        break

print abs(position[0]) + abs(position[1])
