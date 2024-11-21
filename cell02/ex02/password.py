#!/usr/bin/env python3

# Define the correct password
password = "1234567"

def main():
    user_input = input("Enter password: ")

    if user_input == password:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")

if __name__ == "__main__":
    main()