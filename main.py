import math
import time

def S_sqrt(number):
    return 1/math.sqrt(number)

start = time.time()
for i in range(100000000):
    S_sqrt(0.748343)
end = time.time()
print(f"The time S_sqrt took was: {end-start}")