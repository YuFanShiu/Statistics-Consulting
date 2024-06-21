RSV = float(input("Please input a Richter scale value : "))
print("Richter scale value:", RSV)
energy =  10**(1.5 * RSV + 4.8)
print("Equivalence in Joules:", energy)
TNT = energy/(4.184e+9)
print("Equivalence in tons of TNT:", TNT)
lunch = energy/2930200
print("Equivalence in the number of nutritious lunches:", lunch)

