
N = int(input("Input an integer number :"))-1
n = 0
i = 0
j = 1
while n <= N:
    i, j = i+j, i
    n += 1
print("The", N+1, " -th Fibonacci sequence number is", i)    
        