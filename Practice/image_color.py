array = []
for i in range(3):
    array.append([0, 0, 0])

import random

num = random.choices(range(8), k=9)
c = 0
for i in range(3):
    for j in range(3):
        array[i][j] += num[c]
        c += 1
def grid(array):
    for i in range(3):
        print(array[i][0], array[i][1], array[i][2])


def trans(p):
    p = p.split()
    p = [int(i) for i in p]
    return p

def around(p):
    x, y = p[0], p[1]
    a = [(i, j) for i in range(x-1, x+2) for j in range(y-1, y+2)]
    A = []
    for i in range(len(a)):
        r, c = a[i][0], a[i][1]
        if r in range(3) and c in range(3):
            A.append(a[i])
    A.remove((x, y))
    return A #周圍八塊

def replace_c(p):
    r, c = p[0], p[1]
    A = around(p)
    for i in range(len(A)):#遍歷周圍
        j = A[i]
        if array[j[0]][j[1]] == array[r][c]:#如果顏色跟選定塊相同
            array[j[0]][j[1]] = p[2]
    
    array[r][c] = p[2]       
    
    return array

while True:
    grid(array)
    p = input("Enter x y k ")
    if p == "q":
        break
    else:
        p = trans(p)
        replace_c(p)
        grid(array)