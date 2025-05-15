def Discount():
    productPrice = float(input("Enter the product price: "))
    if productPrice > 1000:
        discount = 0.10 * productPrice
    elif 500 <= productPrice <= 1000:
        discount = 0.05 * productPrice
    else:
        discount = 0
    finalPrice = productPrice - discount
    print("Final price:", finalPrice)
Discount()