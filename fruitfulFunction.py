def add_two_numbers(n1, n2): # n1 and n2 are formal parameters
    print('I do Addition')
    return n1+n2

a = int(input("Number 1: "))
b = int(input("Number 2: "))
c = add_two_numbers(a,b) # a and b are arguments
print("The function returned",c)
