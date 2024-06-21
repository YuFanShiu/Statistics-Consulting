p = "X^4+23*X^3+17*X^2+9453"
X = -11
l = p.split("+")
i = 0
l_n = []
while i < len(l):
	if "-" in l[i]:
		j = l[i]
		l.remove(l[i])
		j = j.split("-")
		j.remove("")
		l_n.extend(j)
	i += 1

i = 0
while i < len(l_n):
	if "X^" in l_n[i]:
		j = l_n[i]
		if "*X" in j:
			k = j.index("*")
			n = j[:k]
			if n == "X":
				n = X
			else :
				n = int(n)
			k2 = j.index("^")
			n2 = j[k2+1:]
			if n2 == "X":
				n2 = X
			else :
				n2 = int(n2)
			l_n[i] = n*X**n2
		else :
			k3 = l_n[i].index("^")
			l_n[i] = X**int(l_n[i][k3+1:])
	elif "*X" in l_n[i]:
		n3 = l_n[i].index("*")
		if n3 == "X":
			n3 = X
		else :
			n3 = int(n3)
		l_n[i] = int(l_n[:n3])*X
	l_n[i] = -l_n[i]
	i += 1
i = 0
while i < len(l):
	if "X^" in l[i]:
		j = l[i]
		if "*X" in j:
			k = j.index("*")
			n = int(j[:k])
			if n == "X":
				n = X
			else :
				n = int(n)
			k2 = j.index("^")
			n2 = int(j[k2+1:])
			if n2 == "X":
				n2 = X
			else :
				n2 = int(n2)
			l[i] = n*X**n2
		
		else :
			k3 = l[i].index("^")
			n4 = l[i][k3+1:]
			if n4 == "X":
				n4 = X
			else :
				n4 = int(n4)
			l[i] = X**n4
	elif "*X" in l[i]:
			n3 = l[i].index("*")
			if n3 == "X":
				n3 = X
			else :
				n3 = int(n3)
			n5 = l[i][:n3]
			if n5 == "X":
				n5 = X
			else :
				n5 = int(n5)
			l[i] = n5*X
	else :
		if l[i] == "X":
			l[i] = X
		else:
			l[i] = int(l[i])
	i += 1
print(sum(l)+sum(l_n))

	




