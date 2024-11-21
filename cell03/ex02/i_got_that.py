#!/usr/bin/env python3
def main():
    while True:
        y = input("What you gotta say : ")

        if y.strip().upper() == "STOP":
            break
        
        print("I got that Anything else : ")

if __name__ == "__main__":
    main()