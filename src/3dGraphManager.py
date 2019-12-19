import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import string
from itertools import product

def show3dgraph(n_nodes):
    ### Блок с генерацией слов
    letters = [l for l in string.ascii_lowercase]
    word_size = 3
    comb = product(letters, repeat=word_size)
    words = [''.join(c) for c in comb]
    wrds = [random.choice(words) for _ in range(n_nodes)]
    ###

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    nodes = {(string.ascii_lowercase.index(j[0]), string.ascii_lowercase.index(j[1]), string.ascii_lowercase.index(j[2])): j for j in wrds}
    X, Y, Z = zip(*[(i[0], i[1], i[2]) for i in nodes.keys()])

    ax.scatter(X, Y, Z, c='r', marker='o')

    ages = []
    for n1 in nodes:
        for n2 in nodes:
            if (
                    (nodes[n1][0] == nodes[n2][0] or
                        nodes[n1][1] == nodes[n2][1] or
                        nodes[n1][2] == nodes[n2][2]) and
                    (n1, n2) not in ages and n1 != n2
            ):
                ages.append((n1, n2))

    for line in ages:
        x, y, z = zip(*((dot[0], dot[1], dot[2]) for dot in line))
        ax.plot(x, y, z, color='r')

    for i, txt in enumerate(wrds):
        ax.text(X[i], Y[i], Z[i], txt, size=10)

    plt.show()

show3dgraph(20)