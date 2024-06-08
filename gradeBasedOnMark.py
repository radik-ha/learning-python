"""
Inputs: Tamil Mark, English Mark, Maths Mark
Add these marks.
If sum is,
    0 to 25, BAD
    25 to 50, AVERAGE
    50 to 75, GOOD
    75 to 100, EXCELLENT
"""
tm = int(input("Tamil Mark: "))
em = int(input("English Mark: "))
mm = int(input("Maths Mark: "))
sm = int(input("Science Mark: "))
s = tm+em+mm+sm

if s>=0 and s<25:
    print('BAD')
elif s>=25 and s<50:
    print('AVERAGE')
elif s>=50 and s<75:
    print('GOOD')
else:
    print('EXCELLENT')
