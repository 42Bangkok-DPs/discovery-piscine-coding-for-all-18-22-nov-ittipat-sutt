#!/usr/bin/env python3
def main():
    n1 = float(input("Enter the first number:\n"))
    
    n2 = float(input("Enter the second number:\n"))
    
    p = n1 * n2
    
    print(f"{n1} x {n2} = {p}")
    

    if p > 0:
        print("The result is positive.")
    elif p < 0:
        print("The result is negative.")
    else:
        print("The result is both positive and negative.")

if __name__ == "__main__":
    main()