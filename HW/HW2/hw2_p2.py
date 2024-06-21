n = 10000
for i in range(2, n+1):
	div = 0
	for j in range(1, i+1):
		if i % j == 0 and i != j:
			div = div+j

	if i == div:
		print(i)