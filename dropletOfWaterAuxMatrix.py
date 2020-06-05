# Importing some modules we're using in the project.
import numpy as np
import matplotlib.pyplot as plt
import queue as queue


##
def flood(arena, pos_x, pos_y):
    # Let's prepare the workspace for the algorithm
    q = queue.Queue()
    q.put([pos_x, pos_y, 1])
    while q.not_empty:
        values = q.get()
        flood_spot(arena, values, q)

    plot(arena)


def flood_spot(arena, values, q):
    if arena[values[0]][values[1]] > values[2] or arena[values[0]][values[1]] == 0:

        print("\n")
        arena[values[0]][values[1]] = values[2]
        print(arena)
        print("\n")

        if values[0] < 3:
            q.put([values[0] + 1, values[1], values[2] + 1])

        if values[1] < 3:
            q.put([values[0], values[1] + 1, values[2] + 1])

        if values[0] > 0:
            q.put([values[0] - 1, values[1], values[2] + 1])

        if values[1] > 0:
            q.put([values[0], values[1] - 1, values[2] + 1])
    return


def plot(arena):
    fig, ax = plt.subplots()
    ax.matshow(arena, cmap=plt.cm.Greens)
    plt.show()


# Let's have a given values:
rows = 4
columns = 4
number_of_stones = 12

# We're gonna act with this as a matrix.
stage = np.random.randint(1, size=(rows, columns))

# And we're gonna place two mans.
stage[1][1] = 999
print(stage)
flood(stage, 1, 3)
print("FINALIZADO")
stage[1][1] = 0
