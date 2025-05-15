def group():
    age = int(input("Enter the age: "))
    if 0 <= age <= 1:
        print("Infant")
    elif 2 <= age <= 4:
        print("Toddler")
    elif 5 <= age <= 12:
        print("Child")
    elif 13 <= age <= 19:
        print("Teenager")
    elif 20 <= age <= 59:
        print("Adult")
    else:
        print("Senior")
group()