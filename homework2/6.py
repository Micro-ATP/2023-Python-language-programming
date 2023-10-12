import time

startTime = time.time()

for _ in range(10000000):
    pass 

endTime = time.time()

elapsedTime = endTime - startTime

print(f"Program executed in {elapsedTime:.2f} seconds")
