def BMI():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        classification = "Underweight"
    elif 18.5 <= bmi < 24.9:
        classification = "Normal weight"
    elif 25 <= bmi < 29.9:
        classification = "Overweight"
    else:
        classification = "Obesity"
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Classification: {classification}")
BMI()