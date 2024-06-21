n_layers = int(input("Enter the numbers of layers(2 to 5) = "))
top_layers = int(input("Enter the side length of the top layers = "))
growth = int(input("Enter the growth of each layers = "))
trunk_width = int(input("Enter the trunk width (odd number, 3 to 9) = "))
trunk_height = int(input("Enter the trunk_height (4 to 10) = "))


#the middle of last row
last = growth*n_layers

#top layer
for i in range(0, top_layers):
  #the number of sides in top layer
  t_n = 1+2*i
  #the number of blanks before tags in top laye
  t_blank = int(last-(t_n-1)/2)
  if top_layers <= growth :
    print(" "*t_blank, end="")
    print("#"*t_n)
  elif top_layers > growth :
    if i%growth == 0 :
      print(" "*t_blank, end="")
      print("#"*t_n)
    else :
      print(" "*t_blank, end="")
      print("#"+"@"*(t_n-2)+"#")


#rest of layers
for i in range(2, n_layers+1):
  #the number of sides in each layer
  side = top_layers+growth*(i-1)
  for j in range(1, side):
    #the number of tags in each sides
    n = 1+2*j
    #the number of blanks before tags
    blank = int(last - (n-1)/2)
    if j == side-1 :
      print(" "*blank, end="")
      print("#"*n)
    else :
      print(" "*blank, end="")
      print("#"+"@"*(n-2)+"#")

 
for i in range(1, trunk_height+1):
  print(" "*int(last-(trunk_width-1)/2), end="")
  print("|"*trunk_width)
