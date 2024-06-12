l = ["xys", "lmn", "app", "exe"]
vlist = []

def isVowelExist(w):
    vowels = "aeiou"
    for c in w:
        if c in vowels:
            return True
    return False

for word in l:
    if(isVowelExist(word)):
        vlist.append(word)
print(vlist)
