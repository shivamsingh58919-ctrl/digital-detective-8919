#!/usr/bin/env python3
"""
The Digital Detective - Number Converter
Mission 05: Number Systems, Python and Text Encoding

This program prompts the user for a decimal integer,
converts the value into binary and hexadecimal notations using
Python's built-in conversion functions, and displays the results.
"""

def main():
    print("=== The Digital Detective: Number System Converter ===")
    user_input = input("Enter a positive decimal number: ").strip()
    
    try:
        decimal_val = int(user_input)
        if decimal_val < 0:
            print("Please enter a positive decimal number.")
            return

        binary_val = bin(decimal_val)
        hex_val = hex(decimal_val)

        print("-" * 50)
        print(f"Decimal (Base 10)     : {decimal_val}")
        print(f"Binary (Base 2)       : {binary_val}")
        print(f"Hexadecimal (Base 16) : {hex_val.upper()}")
        print("-" * 50)
    except ValueError:
        print(f"Error: '{user_input}' is not a valid integer.")

if __name__ == "__main__":
    main()
