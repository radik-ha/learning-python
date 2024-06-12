a = 1
b = 2

#Can't do like this
a = b #a=2
b = a #b=2

#------------------------------------------------
#Using Temporary Variable
a = 1
b = 2
print("Before Swapping: ",a,b)
c = a
a = b
b = c
print("After Swapping: ",a,b)

#------------------------------------------------
#Without temp variable
a = 1
b = 2
print("Before Swapping: ",a,b)
a = a+b
b = a-b
a = a-b
print("After Swapping: ",a,b)

#Method2
a = 1
b = 2
print("Before Swapping: ",a,b)
a = a*b
b = a/b
a = a/b
print("After Swapping: ",a,b)
#------------------------------------------------
a = 1
b = 2
print("Before Swapping: ",a,b)
a,b = b,a
print("After Swapping: ",a,b)
