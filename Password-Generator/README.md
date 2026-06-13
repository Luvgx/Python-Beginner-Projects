# Password Generator 🔐

A simple and customizable Password Generator built using Python.

This project allows users to generate secure random passwords by choosing which character types to include, such as uppercase letters, lowercase letters, digits, and special characters.

## Features

* 🔠 Include Uppercase Letters (A-Z)
* 🔡 Include Lowercase Letters (a-z)
* 🔢 Include Digits (0-9)
* 🔣 Include Special Characters (!, @, #, $, etc.)
* 📏 Custom Password Length
* 💪 Password Strength Indicator
* ✅ Input Validation
* 🔄 Generate Multiple Passwords in One Session
* 🧩 Function-Based Code Structure

## Concepts Used

* Python Functions
* Loops (`while`, `for`)
* Conditional Statements (`if`, `elif`, `else`)
* Lists
* User Input Validation
* Random Module
* String Module

## How It Works

1. Select the character types to include.
2. Enter the desired password length.
3. The program generates a random password.
4. Password strength is displayed based on length.
5. Choose whether to generate another password.

## Example Usage

```text
================================
PASSWORD GENERATOR
================================

Please Answer in (y/n):-

Uppercase : y
Lowercase : y
Digits : y
Special : y

Enter the password length : 12

=========================

Generated Password : K@8f#P2m!Q7x
Length : 12
Strength : Strong

=========================
```

## Password Strength Rules

| Length | Strength |
| ------ | -------- |
| 1 - 5  | Weak     |
| 6 - 10 | Medium   |
| 11+    | Strong   |

## Project Structure

```text
Password-Generator/
│
├── password_generator.py
└── README.md
```

## Future Improvements

* Error handling using `try-except`
* Password copy to clipboard feature
* Custom strength requirements
* Ensure at least one character from each selected category
* Save generated passwords to a file

## Learning Outcomes

Through this project, I practiced:

* Working with Python's `random` module
* Using the `string` module
* Creating reusable functions
* Building command-line applications
* Handling user input and validation
* Generating random secure passwords

## Author

**Siddhant Tripathi**

Built as part of my Python learning journey and GitHub portfolio.
