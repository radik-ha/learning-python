import time

start = time.time()
for i in range(100):
    print(i)
print(time.time()-start,"time units")

start = time.time()
for i in range(10):
    print(i)
end = time.time()
print(end-start,"time units")
