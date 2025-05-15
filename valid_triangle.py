def triangle():
    side1 = float(input("Enter the first side of the triangle: "))
    side2 = float(input("Enter the second side of the triangle: "))
    side3 = float(input("Enter the third side of the triangle: "))
    if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
        print("Valid triangle")
    else:
        print("Invalid triangle")
triangle()