"""
0 - 10 = BABY
10 - 20 = KID
20 above = MAN

"""
age = int(input("Age: "))
          
if age>=0 and age<10:
    print("BABY")
          
elif age>=10 and age<20:
    print("KID")
    
else:
    print("MAN")
