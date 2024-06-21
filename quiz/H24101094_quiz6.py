import random
answer_n = random.sample(range(24), 1)
answer_n = answer_n[0]
L = "abcdefghijklmnopqrstuwhxyz"
answer = L[answer_n]
C = 0#計數器
#為了畫histogram
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
while True:
    n = input("Guess the lowercase alphabet ")
    n = L.find(n)
    if n != answer_n:
        if n > answer_n:
            print("The alphbet you are looking for is alphabetically lower ")
        elif n < answer_n:
            print("The alphbet you are looking for is alphabetically higher ")
        C += 1
        if n // 4 == 0:
            a += 1
        elif n // 4 == 1:
            b += 1
        elif n // 4 == 2:
            c += 1
        elif n // 4 == 3:
            d += 1
        elif n // 4 == 4:
            e += 1
        elif n // 4 == 5:
            f += 1
        elif n // 4 == 6:
            g += 1        
    elif n == answer_n:
        print("congratulation ! You guess the aiphbet %s in " % answer, C, "tries")
        print("Guess histogram")
        s1 = "*"*a
        print("a-d :", s1)
        s2 = "*"*b
        print("e-h :", s2)
        s3 = "*"*c
        print("i-l :", s3)
        s4 = "*"*d
        print("m-p :", s4)
        s5 = "*"*e
        print("q-t :", s5)
        s6 = "*"*f
        print("u-x :", s6)
        s7 = "*"*g
        print("y-t :", s7)
        break
