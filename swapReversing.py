l = [1,2,3,4]
t = l[0]
l[0] = l[-1]
l[-1] = t
t = l[1]
l[1] = l[-2]
l[-2] = t
print(l)