def deposit():
    while True:
        amount = input("Enter your deposit amount: $")
        if amount.isdigit():
            amount = int(input())
        else:
            print("Enter a number: ")
    return amount
deposit()