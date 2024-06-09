"""
1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators
5. Identity operators
6. Membership operators
7. Bitwise operators
"""

#Arithmetic Operators: +,-,/,*,**,%,//
print(2+3)
print(2-3)
print(2/3)
print(2*3)
print(2**3)
print(12%3)
print(12//3)
#-----------------------------------------------------------------------

#Assignment Operators: =, +=, -=, *=, /=, %=, //=
a = 2    # =
#Following are shorthand assignment operators
a += 1   # same as "a = a+1"   i.e., a = 2+1 = 3
a -= 1   # same as "a = a-1"   i.e., a = 3-1 = 2
a *= 2   # same as "a = a*2"   i.e., a = 2*2 = 4
a /= 2   # same as "a = a/2"   i.e., a = 4/2 = 2
a %= 2   # same as "a = a%2"   i.e., a = 2%2 = 0
print(a)

a = 34
a //= 7 # same as "a = a//2"   i.e., a = 34//7 = 4
print(a)
#-----------------------------------------------------------------------

#Comparison Operators: ==, >, <, >=, <=
x = 10
print(x==10)
y = x==10
print(y)

print(x>5)
print(x<5)
print(x>=10)
print(x<=100)
#-----------------------------------------------------------------------

#Logical Operators: and, or, not
y = x==10 and x>5
print(y) #True
print(x==10 and x>100) #False
print(x==10 or x>100) #True
print(not x==10)    #False
#-----------------------------------------------------------------------

#Identity Operators: is
a = 10
b = 20
print(a is not b)
b = 10
print(a is b)
#-----------------------------------------------------------------------

#Membership Operator: in
l = ["apple", 12, "orange", 2.3] #list
print("apple" in l)

t = ("cat", 23, "dog") #tuple
print(43 in t)

s = {"cat", "cat", "34", "tiger"} #set
print("cat" in s)

d = {"tiger": "panthera tigris", "cat": "felis familiaris", "neem": "azadirachta indica"}
print("tiger" not in d)

s = "aeiou"
print("w" in s)
#-----------------------------------------------------------------------

#Bitwise Operators: &, |, ~, ^
a = 0b101
b = 0b111
print(a&b)
print(a|b)
print(~b)
print(a^b)
print(a>>1)
print(a<<1)
