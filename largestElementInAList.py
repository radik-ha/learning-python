l = [1,2,3,4,5,100,2]
print(max(l))

LARGE = l[0]
for i in l:
    if i>LARGE:
        LARGE = i

print(LARGE)
