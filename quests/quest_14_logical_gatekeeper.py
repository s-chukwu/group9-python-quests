#!/usr/bin/env python3
age = int(input("Enter your age: "))
gold = int(input("Enter your gold coins: "))

if age >= 18 and gold >= 20:
    print("You may enter the club!")
else:
    print("Access Denied. You need to be 18+ and have 20+ gold coins.")
