s = "ASSIST"
caesar = ""
k = 8
for i in s:
    e_c = chr((ord(i) - ord("A") + k)%26 + ord("A"))
    caesar += e_c
a = 12
b = 5
affine = ""
for i in caesar:
    e_a = chr((a * (ord(i) - ord('A')) + b) % 26 + ord('A'))
    affine += e_a
print(affine)