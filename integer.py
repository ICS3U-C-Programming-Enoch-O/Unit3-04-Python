def main():
    # Ask user for number
    user_number = int(input("choose a number greater or lesser than 0: "))

    # Check if user input is less than 0
    if user_number < 0:
        print("your number is a negative integer")
    elif user_number > 0:
        print("your number is a positive integer")
    else:
        print("your number is 0")


if __name__ == "__main__":
    main()
