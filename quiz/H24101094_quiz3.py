print("Welcome !")

while  True:		
	n_1 = float(input("Enter the first number : "))
	n_2 = float(input("Enter the second number : "))
	ari = input("Select an arithmetic operation (+, -, *, /) : ")
	if ari == "+" :
		answer = n_1 + n_2
	elif ari == "-" :
		answer = n_1 - n_2
	elif ari == "*" :
		answer = n_1 + n_2
	elif ari == "/" :
		if n_2 == 0 :
			print("Division by zero")
			continue
		else :
			answer = n_1 / n_2
	print("Result", answer)
	again = input("Do you  want to perform another calculation ? (Yes or No) : ")
	if again == "Yes" :
		continue
	elif again == "No" :
		print("Goodbye")
		break