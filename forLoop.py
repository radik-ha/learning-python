for x in "banana":
    print(x)

flowers = ["lotus","rose","jasmine"]
for x in flowers:
    print(x)
    
for x in flowers:
    if x == "rose":
        break
    print(x)
    
for x in flowers:
    if x == "lotus":
        continue
    print(x)

colr = ["red","big","tasty",]
fruits = ["apple","banana","cherry"]
for x in colr:
    for y in fruits:
        print(x,y)
