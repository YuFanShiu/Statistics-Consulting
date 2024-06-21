s = "-2 0 3 4 5 6 1 2 3"
#s = input("seq ")
l = s.split()
#l = list(s)
l = [int(i) for i in l]
L = []
for i in range(len(l)):
    for j in range(i+1, len(l)):
        s = l[i:j+1]
        l2 = list(s)
        l2.sort()
        if s == l2:
            s = list(set(s))
            s.sort()
            L.append(s)

f = []
for i in range(len(L)):
    f.append(len(L[i]))

i = f.index(max(f))
print(L[i])





