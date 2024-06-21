amount = int(input("Enter the shopping amount:"))
membership = input("Enter the membership level (Regular or Gold):")
if membership == "Gold" :
	if amount >= 3000:
		amount = (0.75)*amount
	elif amount >= 2000:
		amount = (0.8)*amount
	elif amount >= 1000:
		amount = (0.85)*amount
	print(membership, "\t$", amount)

elif membership == "Regular":
	if amount >= 3000:
		amount = (0.8)*amount
	elif amount >= 2000:
		amount = (0.85)*amount
	elif amount >= 1000:
		amount = (0.9)*amount
	print(membership, "\t$", amount)

else:
	print("Invalid member level. Please enter", "\'"+"Regular"+"\'", "or", "\'"+"Gold"+"\'")
	





