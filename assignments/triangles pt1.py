side1 = int(input("First: "))
side2 = int(input("Second: "))
side3 = int(input("Third: "))

def is_triangle(a,b,c):
    if a+b>c and b+c>a and c+a>b:
        print("that's a triangle!")
    else:
        print("not a triangle")

def is_right_triangle(a,b,c):
    sides = [a,b,c]
    sides.sort()
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("That's a tight triangle!")
    else:
        print("That's not a right triangle")

def perimeter(a,b,c):
    print("perimeter: "+str(a+b+c))
    return a+b+c

def area(a,b,c):
    
    p = (a+b+c)/2
    print((p*(p-a)*(p-b)*(p-c))**0.5)

def display_triangle(a,b,c):
    sides = [a,b,c]
    sides.sort()
    print("Smallest side: "+str(sides[0]))
    print("Medium side:"+str(sides[1]))
    print("Largest side: "+str(sides[2]))

is_triangle(side1,side2,side3)
is_right_triangle(side1,side2,side3)
perimeter(side1,side2,side3)
area(side1,side2,side3)
display_triangle(side1,side2,side3)