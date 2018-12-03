class MyClass:
    __instances = []

    def __init__(self):
        MyClass.__instances.append(self)

    def getInstances():
        return MyClass.__instances


A = MyClass()
B = MyClass()
for obj in MyClass.getInstances():
    print(obj)
