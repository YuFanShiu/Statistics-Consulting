Y = int(input("Please enter Year:"))
m = int(input("Please enter Month:"))

if m<3:
	m = m+12
	Y = Y-1
elif m>=3:
	m = m

c = Y // 100
y = Y % 100

#當月第一天禮拜幾:日W=1~五:W=6, 六:W=0
W = (1+y+y//4+c//4-2*c+13*(m+1)//5)%7 
W = round(W)
if W<0:
	W = W+7
#對應日歷位置，Sun:0, Sat:6
if W == 0:
	W = 6
elif W in range(1, 7):
	W = W-1

print("Sun Mon Tue Wed Thu Fri Sat")
first_row_num = " ".join("%02d " % i  for i in range(1, 8-W))
print(" "*4*W + first_row_num)

if m in [3, 5, 7, 8, 10, 12, 13]:
	num_day = 31
elif m in [4, 6, 9, 11]:
	num_day = 30
elif m == 14 and (((Y+1)%4 == 0 and (Y+1)%100 != 0) or ((Y+1)%400 == 0)):
	num_day = 29
else :
	num_day = 28

i=8-W
count = 1
while i <= num_day+1 and count <= num_day-7+W:
	if count%7 == 0:
		print("%02d "%i)
	else :
		print("%02d "%i, end=" ")
	i += 1
	count += 1
