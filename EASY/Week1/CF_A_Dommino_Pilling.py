#codeForce
prod = 1
x = input()
p = x.index(" ")
for i in range(2):
    if i == 0:
        prod *= int(x[i:p])
    else:
        prod *= int(x[i+1:])
print(prod//2)