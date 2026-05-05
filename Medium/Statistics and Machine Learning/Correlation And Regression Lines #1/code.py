# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

physics = [15,12,8,8,7,7,7,6,5,3]
history = [10,25,17,11,13,17,20,13,9,15]

n = len(physics)

mean_x = sum(physics)/n
mean_y = sum(history)/n

num = sum((x - mean_x)*(y - mean_y) for x, y in zip(physics, history))
den_x = sum((x - mean_x) ** 2 for x in physics)
den_y = sum((y - mean_y)** 2 for y in history)

r = num/math.sqrt(den_x * den_y)

print(f"{r:.3f}")