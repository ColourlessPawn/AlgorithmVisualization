# Importing some modules we're using in the project.
import numpy as np
import matplotlib.pyplot as plt

ROWS = 12
COLUMNS = 11


# Starting the algorithm
def flood(arena, pos_x, pos_y):
    # We're gonna flood the arena
    flood_spot(arena, pos_x, pos_y, 0)


def flood_spot(arena, pos_x, pos_y, iteration):
    value = iteration + 1

    if 0 <= pos_x < ROWS and 0 <= pos_y < COLUMNS and (
            stage[pos_x][pos_y] >= value or stage[pos_x][pos_y] == 0):
        # Let's flood the spot
        iteration = iteration + 1
        if stage[pos_x][pos_y] == 999:
            return

        stage[pos_x][pos_y] = iteration
        # Let's continue flooding
        flood_spot(arena, pos_x + 1, pos_y, iteration)
        flood_spot(arena, pos_x, pos_y + 1, iteration)
        flood_spot(arena, pos_x - 1, pos_y, iteration)
        flood_spot(arena, pos_x, pos_y - 1, iteration)


# We're gonna act with this as a matrix.
stage = np.random.randint(1, size=(ROWS, COLUMNS))

# And we're gonna place two mans.
stage[1][1] = 999
print(stage)
flood(stage, 1, 6)
flood(stage, 8, 2)
stage[1][1] = 0

# Printing the graph.
fig, ax = plt.subplots()
ax.matshow(stage, cmap=plt.cm.Greens)
plt.show()
