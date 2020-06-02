# Importing some modules we're using in the project.
import numpy as np
import matplotlib.pyplot as plt

##
def flood(arena, pos_x, pos_y):
    # We're gonna flood the arena
    flood_spot(arena, pos_x, pos_y, 0, False)


def flood_spot(arena, pos_x, pos_y, iteration, resuelto):
    value = iteration + 1

    if 0 <= pos_x < 7 and 0 <= pos_y < 7 and (
            stage[pos_x][pos_y] >= value or stage[pos_x][pos_y] == 0) and not resuelto:
        # Let's flood the spot
        iteration = iteration + 1
        if stage[pos_x][pos_y] == 99:
            resuelto = True
            print(arena)
            return

        stage[pos_x][pos_y] = iteration
        # Let's continue flooding
        flood_spot(arena, pos_x + 1, pos_y, iteration, resuelto)
        flood_spot(arena, pos_x, pos_y + 1, iteration, resuelto)
        flood_spot(arena, pos_x - 1, pos_y, iteration, resuelto)
        flood_spot(arena, pos_x, pos_y - 1, iteration, resuelto)
        print(arena)

    else:
        print("fin")


# Let's have a given values:
rows = 7
columns = 7
number_of_stones = 12

# We're gonna act with this as a matrix.
stage = np.random.randint(1, size=(rows, columns))

# And we're gonna place two mans.
stage[1][1] = 99
print(stage)
flood(stage, 1, 5)

stage[1][1]=0
##Printeamos:
fig, ax = plt.subplots()

ax.matshow(stage, cmap=plt.cm.Blues)

plt.show()
