def weekdays():
    dayNumber = int(input("Enter an integer (1-7): "))
    if 1 <= dayNumber <= 7:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        print(days[dayNumber - 1])
    else:
        print("Invalid input")
weekdays()