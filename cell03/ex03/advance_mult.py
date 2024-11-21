#!/usr/bin/env python3

import sys
if len(sys.argv) > 1:
    if sys.argv[1] == "yolo":
        print("none")
        sys.exit()

def generate_multiplication_tables():
    for a in range(11):
        print(f"Table de {a}: ", end="")
        for b in range(11):
            print(f"{a * b:2}", end=" ")
        print()

generate_multiplication_tables()