thief = 1
while thief <= 4:
	statment_1 = thief !=1  
	statment_2 = thief ==3 
	statment_3 = thief ==4 
	statment_4 = thief ==3
	statment = (statment_1, statment_2, statment_3, statment_4)
	num_False = statment.count(False)
	if num_False == 1:
		print("The true thief", thief)
	thief += 1