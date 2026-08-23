# Debt Calculator

## About
This program helps users decide how much they want to put toward their debt by estimating how long it will take to pay it off based on different payment amounts.
I built this project because I wanted one place to keep track of all my debts and their estimated payoff times, rather than having to check multiple accounts and tabs separately.

## Features
It's pretty simple: you enter the name of your debt, its balance, monthly payment, and interest rate. You can also enter a target payment you'd like to contribute each month. The program then compares how long it would take to pay off the debt using the minimum monthly payment versus your target payment. It saves your debts so you can come back later and see how long they’ll take to pay off. You can also simulate making payments, so you don’t have to keep entering the same debt information over and over. If your debt has a variable interest rate, you can update the rate to see how it changes your estimated payoff time.

## How It Works
The program takes the debt information you provide and estimates the payoff time by applying the monthly interest, subtracting the payment, and repeating the calculation until the balance reaches zero.

## Getting Started

### Requirements

- Python 3.10 or newer

### Installation

Clone the repository:

​```bash
git clone https://github.com/JtorresBear/Debt_Calculator.git
​```

Move into the project directory:

​```bash
cd Debt_Calculator
​```

Run the program:

​```bash
python3 main.py
​```

## Testing

The project includes unit tests for the debt calculations, payment behavior, and JSON save/load functionality.

Run all tests with:

```bash
#python3 -m unittest
```

## What I Learned

I learned how to use JSON more effectively, including how to save and load custom objects. I also got more experience with object-oriented design, input validation, exception handling, and organizing a CLI application. This was also my first time writing unit tests for my own project, which helped me find bugs and improve some of my original code.