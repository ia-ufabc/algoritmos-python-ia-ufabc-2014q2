# Nome: Alamo Pereira Saravali
# RA: 11097810
# Email: alamo.saravali@gmail.com / alamo.saravali@aluno.ufabc.edu.br

from random import shuffle, randrange
 
def make_maze(w = 3, h = 3):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]
 
    def walk(x, y):
        vis[y][x] = 1
 
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "+  "
            if yy == y: ver[y][max(x, xx)] = "   "
            walk(xx, yy)
 
    walk(randrange(w), randrange(h))
    lab = ''
    for (a, b) in zip(hor, ver):
        if lab:
            lab += '\n'
        lab += ''.join(a + ['\n'] + b)

    return lab
 
lab = make_maze()

print lab