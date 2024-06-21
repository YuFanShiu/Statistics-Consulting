
#最長回文
s = input("Enter a string : ")
pal = ""
for i in range(len(s)):
	for j in range(i+1, len(s)+1):
		sub = s[i:j]
		if sub == sub[::-1] and len(sub) > len(pal):
			pal = sub
print("Longest palindromic substring is :", pal)
print("Length is :", len(pal))

				

