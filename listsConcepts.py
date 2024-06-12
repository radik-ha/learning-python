l = [1,2,"ari",3.4,True]
print(l[0])
print(l[-1]) # same as l[len(l)-1]
print(l[0:-1:2])
l[0] = 3 # Mutable
print(l)
l.append(False)
print(l)
l.remove(False) #Data specified removed
print(l)
l.pop() #Last Element Removed
l.pop(0) #Index Element Removed
print(l)
