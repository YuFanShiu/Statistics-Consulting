i = 9
l = list(range(1, 10))
l.sort(reverse=True)

while i >= 3:
    j = 0

    while j < len(l):
        k = l[j]
        n = 1
        m = i
        s = ""
        while n <= 3:
            s += (str(k)+"x"+str(m)+"="+str(m*k)+"\t")
            m -= 1
            n += 1
        print(s)

        j += 1
    if i != 3:
        print("\n")
    i -= 3