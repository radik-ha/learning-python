"""
0 – 12 வயதுப் பெண் - பேதை.
12 – 24 வயதுப் பெண் - பெதும்பை.
24 – 36 வயதுப் பெண் - மங்கை.
36 – 48 வயதுப் பெண் - மடந்தை.
48 – 60 வயதுப் பெண் - அரிவை.
60 – 72 வயதுப் பெண் - தெரிவை.
72 வயதுக்கு மேல் பெண் - பேரிளம்பெண்
"""
wage = int(input("AGE: "))

if wage>=0 and wage<12:
    print("பேதை")
elif wage>=12 and wage<24:
    print("பெதும்பை")
elif wage>=24 and wage<36:
    print("மங்கை")
elif wage>=36 and wage<48:
    print("மடந்தை")
elif wage>=48 and wage<60:
    print("அரிவை")
elif wage>=60 and wage<72:
    print("தெரிவை")
else:
    print("பேரிளம்பெண்")
