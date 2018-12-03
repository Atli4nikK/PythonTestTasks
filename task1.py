

# y=kx+b
# a=[x1,y1,x2,y2]
# equation(a)=[x1,y1,x2,y2,k,b]
#               0  1  2  3 4 5
def equation(a):
    if a[3] - a[1] != 0 and a[0] - a[2] != 0:
        # k =    ( y2   -  y1) / ( x2  -  x1)
        a.append((a[3] - a[1]) / (a[2] - a[0]))
    elif a[0] - a[2] == 0:
        a.append(999999)
    elif a[3] - a[1] == 0:
        a.append(0)
    a.append(a[1] - a[4] * a[0])
    return a


# точка пересечения прямых a , b
# a,b = [x1,y1,x2,y2,k,b]
#        0  1  2  3  4 5
# interseption(a,b) =[x,y]
def intersection(a, b):
    return [(a[5] - b[5]) / (a[4] - b[4]), (b[4] * a[5] - a[4] * b[5]) / (a[4] - b[4])]


# a,b = [x1,y1,x2,y2,k,b]
def parallelism(a, b):
    return a[4] == b[4]


# a = [[x0,y0],[x1,y1],[x2,y2]]
def area(a):
    print(a)
    return 0.5 * abs((a[0][0] - a[2][0]) * (a[1][1] - a[2][1]) - (a[1][0] - a[2][0]) * (a[0][1] - a[2][1]))


# Ввод данных

x = []
print('Введите координаты.')
for i in range(3):
    x.append([float(j) for j in input().split()])
    equation(x[i])
print(x)

if parallelism(x[1], x[2]) and parallelism(x[0], x[1]):
    print("a || b || c \n0")
elif parallelism(x[0], x[1]):
    print("a || b \n0")
elif parallelism(x[1], x[2]):
    print("b || c \n0")
elif parallelism(x[0], x[2]):
    print("a || c \n0")
elif intersection(x[0], x[1]) != intersection(x[0], x[2]):
    print("a /\ b /\ c \n" + str(area([intersection(x[0], x[1]), intersection(x[0], x[2]), intersection(x[1], x[2])])))
