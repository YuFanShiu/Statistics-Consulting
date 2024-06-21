
        
n = int(input("enter n"))
grid = [['_' for _ in range(n)] for _ in range(n)]
print(grid)
while True:
    p = input("continue ? ")
    if p == "n" :
        break
    else :
        i = int(input("enter row "))
        j = int(input("ener col "))
        v = input("enter value ")
        grid[i][j] = v
        for k in range(len(grid)):
            s = " ".join(grid[k])
            s += "\n"
            print(s)
        
