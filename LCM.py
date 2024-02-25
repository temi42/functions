#LCM.py
#Code for GCD
def gcd(x, y):
    while y != 0:
        t = y
        y = x % y
        x = t
    return x

#Code for LCM
def lcm(x, y): 
    return (x * y) // gcd(x,y)

#This program calculates the LCM (Least Common Multiple) for three integers
def main():
    a = int(input("Please enter an integer: "))
    b = int(input("Please enter an integer: "))
    c = int(input("Please enter an integer: "))
    lcmFound = lcm(lcm(a,b),c)
    print("lcm of values", a, b, c, "is:", lcmFound)

main()
