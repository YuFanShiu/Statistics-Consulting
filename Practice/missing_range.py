l = input("enter the list ").split()
l = [int(i) for i in l]
low = int(input("entrer the lowerbound "))
up = int(input("enter the upperbound "))

if l[0] > low:
    l.insert(0, low-1)
if l[-1] < up:
    l.append(up)

L = []
for i in range(len(l)-1):
    if l[i+1] != l[i]+1:
        
        if len(range(l[i]+1, l[i+1])) > 1:
            s = "%d"%(l[i]+1) + "-"+"%d"%(l[i+1]-1)
            L.append(s)
        else:
            L.append("%d"%(l[i]+1))
                

n = L[-1].find("-")+1  
L[-1] = L[-1][:n]
if l[-1] <= up:#記<=
    L[-1] += str(up)
elif l[-1] > up:
    L[-1] += str(l[-1]-1)
print(L)