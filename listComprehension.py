l = list(range(1,11))
print(l)


l = []
for i in range(1,11):
    l.append(i)             #i is called loop variable
print(l)

l = [i for i in range(1,11)] #ListComp
print(l)
l = [i+1 for i in range(1,11)]
print(l)
l = [i for i in range(1,11) if i%2==0]
print(l)
