# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

physics = [15,12,8,8,7,7,7,6,5,3]
history = [10,25,17,11,13,17,20,13,9,15]

n = len(physics) #quantidade de alunos, nao das notas

mean_x = sum(physics)/n #calcula a media
mean_y = sum(history)/n

num = sum((x-mean_x) * (y - mean_y) for x, y in zip(physics, history)) #tem q por sum se n n roda
den = sum((x - mean_x) **2 for x in (physics))

m = num/den

print(f"{m:.3f}")