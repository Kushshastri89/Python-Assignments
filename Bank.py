def Bank():
    balance = 1000
    while True:
        print("\nATM Menu:")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Current balance:", balance)
        elif choice == '2':
            depositAmount = float(input("Enter the amount to deposit: "))
            if depositAmount > 0:
                balance += depositAmount
                print("Deposit successful. New balance:", balance)
            else:
                print("Invalid amount.")
        elif choice == '3':
            withdrawAmount = float(input("Enter the amount to withdraw: "))
            if 0 < withdrawAmount <= balance:
                balance -= withdrawAmount
                print("Withdrawal successful. New balance:", balance)
            else:
                print("Insufficient balance or invalid amount.")
        elif choice == '4':
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")
Bank()