#AreaOfTriangles.py
#Compute the area of triangles using Heron's formula
import math
def isValidTriangle(a,b,c):
    if (a+b>c and a+c>b and b+c>a):
        return True
    return False
def triangleArea(a,b,c):
    if isValidTriangle(a,b,c):
        s = (a+b+c)/2.0
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("The area of the triangle is", format(area, '.2f'))
    else:
        print("Not a valid triangle")
    
n = int(input("How many triangles are to be processed? "))
for t in range (n):
    a = float(input("Enter the length of side 1: "))
    b = float(input("Enter the length of side 2: "))
    c = float(input("Enter the length of side 3: "))
    triangleArea(a,b,c)


