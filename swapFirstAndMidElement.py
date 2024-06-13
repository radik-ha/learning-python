l = [1,2,3,4,5]
t = l[0]
l[0] = l[int(len(l)/2)]
l[int(len(l)/2)] = t
print(l)
