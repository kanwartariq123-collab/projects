while True:

    choice = str(input(
        'Choose multiplication / division / subtraction / addition '
        '(a / m / s / d): '
    ))

    if choice not in ['a', 'm', 's', 'd']:
        print('Please enter a correct option (a / m / s / d)')
        continue

    try:

        if choice == 'a':
            add1 = int(input("Enter first addition number: "))
            add2 = int(input("Enter second addition number: "))
            print("Your value is:", add1 + add2)

        elif choice == 'm':
            mul1 = int(input("Enter first multiplication number: "))
            mul2 = int(input("Enter second multiplication number: "))
            print("Your value is:", mul1 * mul2)

        elif choice == 's':
            sub1 = int(input("Enter first value: "))
            sub2 = int(input("Enter second value: "))
            print("Your final value is:", sub1 - sub2)

        elif choice == 'd':
            div1 = int(input("Enter first division number: "))
            div2 = int(input("Enter second division number: "))
            print("That's your final value:", div1 / div2)

    except ValueError:
        print("Please enter numbers correctly.")
        continue

    final = str(input("Do you want to play again? (y/n): "))

    if final == 'n':
        print("Thank you for playing!!")
        break

    elif final == 'y':
        continue

    else:
        print("Invalid option. Exiting...")
        break 