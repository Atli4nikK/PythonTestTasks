import numpy as np
from task3 import decorator

@decorator
def symmetryCheck(pointsX, axis):
    x = np.array(pointsX)
    average = sum(x[:, axis]) / len(x[:, axis])
    check = True
    for point in pointsX:
        if axis == 0:
            symmetryPoint = [(average + average - point[0]), point[1]]
        else:
            symmetryPoint = [point[0], (average + average - point[1])]
        if not (symmetryPoint in pointsX):
            check = False
    return check

points = []
print('Введите координаты, по окончанию нажмите еще раз \'Enter\'')
point = input()
while point:
    points.append([float(j) for j in point.split()])
    point = input()

if symmetryCheck(points, 0) or symmetryCheck(points, 1):
    print("YES")
else:
    print("NO")
