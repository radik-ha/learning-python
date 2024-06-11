N, START, SUM = int(input("Enter N: ")), 1, 0

for i in range(START,N+1):
    SUM += i
print("Average of First",N,"Numbers is",SUM/N)
