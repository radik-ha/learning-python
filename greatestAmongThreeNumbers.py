a = int(input("Enter A First Number: "))
b = int(input("Enter A Second Number: "))
c = int(input("Enter A Last Number: "))

if a>b and a>c:
    print(a,"is greater")

elif b>a and b>c:
    print(b,"is greater")

elif a==b and b==c:
    print("All are Equal")

else:
    print(c,"is greater")
    
