h1 = float(input("Input the height of the 1st ball :"))
m1 = float(input("Input the mass of the 1st ball:"))
m2 = float(input("Input the mass of the 2nd ball:"))
g = 9.8
U1 = m1 * g * h1
v1 = (U1 * 2 / m1) ** 0.5
v2 = (U1 * 2 / m2) ** 0.5
print("The velocity of the 1st ball after slide:", v1)
print("The velocity of the 2nd ball after collision:", v2)
