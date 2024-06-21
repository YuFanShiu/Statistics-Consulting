def p_grid(array):
    n = len(array)
    A= list("abcdefghi")
    S = "  "
    for i in range(n):
        s = " "+A[i]+"  "
        S += s
    print(S)
    for i in range(0, n):
        s = " +"
        s += "---+"*n
        print(s)
        s2 = str(i+1)+"|"
        for j in range(0, n):
            s2 += " "+str(array[i][j])+" |"
        print(s2)
    S2 = " +"+"---+"*9
    print(S2)


n = 9
array = [[' ' for _ in range(n)] for _ in range(n)]
pos = [(i, j) for i in range(n) for j in range(n)]#所有位置的list
a = list("abcdefghi")
a = {a[i]:i for i in range(len(a))}#將字母映射到數字

def trans(step):#將輸入轉換成位置
    step = list(step)
    r, c = int(step[1])-1, a[step[0]]
    l = [r,c]
    return l
def around(l):#獲得周圍位置
    r, c = l[0], l[1]
    L = [(i, j) for i in range(r-1, r+2) for j in range(c-1, c+2)]
    L = [i for i in L if i in pos]    
    return L

import random
def initial(first):
    mines = random.sample([p for p in pos if p not in around(trans(first))], 10)
    D = {p: 0 for p in pos}#所有位置資訊的字典
    for mine in mines:
        D[mine] = 'b'
    for (i, j) in pos:
        if D[(i, j)] != 'b':  
            count = 0
            a_p = around((i,j))
            a_p.remove((i, j))
            for p in a_p:
                if D[p] == 'b':
                    count += 1
            D[(i, j)] = count

    return mines, D

first = input('Enter first step : ')
mines, D = initial(first)

def aro_0(array):
    while True:  # 添加一个循环，直到没有更多变化
        changed = 0  # 每次循环开始时设为 False
        for i in range(len(array)):
            for j in range(len(array[i])):
                if array[i][j] == 0:
                    a = around((i, j))  
                    if any(D[k] == 0 for k in a):  # 检查D字典中对应坐标是否为0
                        for m in a:
                            if D[m] == 0 and array[m[0]][m[1]] != 0:
                                array[m[0]][m[1]] = 0
                                changed = 1  # 只要发生了变化，就将changed设为True
        if changed == 0:  # 如果在一次完整的遍历后没有变化，结束循环
            break
    return array



def unfold(step):
    s_l = trans(step)
    r, c = s_l[0], s_l[1]
    array[r][c] = D[(r, c)]
    aro_0(array)
    
    return array



def flag(step):
    r, c = trans(step[:2])
    if step[-1] == "f" and step[-2:] != "rf":
            if array[r][c] == " ":
                array[r][c] = "F"
    return array

def unflag(step):
    r, c = trans(step[:2])
    if array[r][c] == "F":
        array[r][c] = " "
    return array

array =unfold(first)


import time

start_time = time.time()
c = 0
while True:
    c = 0#正確標記
    w = 0#錯誤標記
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 'F' and D[(i, j)] == 'b':
                c += 1
            elif array[i][j] == 'F' and D[(i, j)] != 'b':
                w += 1
    if c == 10 and w == 0:
        print('You win')
        again = input('Play again y/n : ')
        if again == 'n':
            break
        elif again == 'y':
            array = [[' ' for _ in range(n)] for _ in range(n)]
            first = input('Enter first step : ')
            mines, D = initial(first)
            array = unfold(first)
            p_grid(array)
            continue
    print("%d left"%(10-c))

    p_grid(array)
    step = input("Enter step ")

    if step == "done":
        break
    elif step == 'help':
        print('Enter the column followed by the row(ex.a5)')
        print('To add or remove a flag, add f or rf to the cell(ex.a5f, a5rf)')

    else:
        S = trans(step[:2])
        if (S[0], S[1]) not in pos:
            print('Out of range')
        else:
            P = array[S[0]][S[1]]

            if D[(S[0], S[1])] == 'b'and len(step) == 2:
                print('Game over')
                again = input('Play again y/n : ')
                if again == 'n':
                    break
                elif again == 'y':
                    array = [[' ' for _ in range(n)] for _ in range(n)]
                    first = input('Enter first step : ')
                    mines, D = initial(first)
                    array = unfold(first)
                    p_grid(array)

                    continue
        
            elif P == " " and step[-1] != 'f':
                array = unfold(step)
            elif P == " " and step[-1] == 'f':
                if step[-2:] != 'rf':
                    array = flag(step)
            elif P == "F" and step[-1] == 'f':
                if step[-2:] == 'rf':
                    array = unflag(step)
            elif P != " " and P != "F":
                print('That cell is already shown')
            elif P != " " and P == "F":
                print('There is a flag there')
            elif P != " " and step[-1] == 'f':
                print('Cannot put a flag there')
            
        
        

end_time = time.time()

execution_time = end_time - start_time
print("执行时间:", execution_time, "秒")


        
        
    