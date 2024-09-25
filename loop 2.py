D = 0 
deret = []

for i in range(1, 40):
    deret.append(i)
    D += i

print (" + ". join(map(str, deret)))