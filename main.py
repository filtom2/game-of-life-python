import random


# create 2d array
def create_2d_list(cols, rows):
    arr = [[random.randint(0, 1) for i in range(cols)] for j in range(rows)]
    # only prints the shape of the list(array)
    for row in arr:
        print(row)

    return arr


cols = 10
rows = 10

grid = create_2d_list(cols, rows)


