
import debts

def add_dept():
    print("Name of your debt")
    name = input()

    total = input_loop("the total")
    mon_payment = input_loop("your monthly payment")
    targ_payment = input_loop("your target payment, or total you would like to pay")
    interest = input_loop("the debt's interest rate, just the number not \'%\'")
    return debts.Debt(name,total,mon_payment,targ_payment,interest)
    


def input_loop(key_word):
    while True:
        try:
            print(f"Give me {key_word}")
            number = float(input())
            return number
        except ValueError:
            print("That doesn't work, give a Number")


