a, b = 63, 105
while b : #while b != 0
	a, b = b, a % b # % 餘數
	print(a, b)
#最大公因數

print("next")

n = 21
while n != 1:
	print(n, end=", ")
	if n % 2 == 0:
 		n = n // 2
	else:
 		n = n * 3 + 1
print(n, end=".\n") 
# Collatz 猜想，對於任何正整數 n，遵循以下遞歸規則，最終都會收斂到 1：