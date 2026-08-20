import os
import debts

def add_dept():
    print("Name of your debt")
    name = input()

    total = input_loop("the total")
    mon_payment = input_loop("your monthly payment")
    targ_payment = input_loop("your target payment, or total you would like to pay")
    interest = input_loop("the debt's interest rate, just the number not \'%\'")
    debt = debts.Debt(name,total,mon_payment,targ_payment,interest)
    pretty_print(debt)
    return debt



def get_debt(debts):
    while True:
        try:
            os.system("clear")
            show_all_debts(debts)
            selection = input_loop("the corresponding number")
            selection = int(selection)
            if selection > len(debts):
                raise ValueError("That doesn't work, it's not a selection")
            if selection <= 0:
                raise ValueError("Can't be 0 or less")
            return selection
        except ValueError as e:
            print(e)


def input_loop(key_word):
    while True:
        try:
            print(f"Give me {key_word}")
            number = input()
            if number == "q":
                raise SystemExit
            else:
                number = float(number)
            return number
        except ValueError:
            os.system("clear")
            print("\n\nThat doesn't work, give a Number")


def update(debts, debt):
    os.system("clear")
    print("\n")
    print(f"1 to update, 2 to delete {debt.name}")
    while True:
        selection = input()
        match selection:
            case "1":
                update_debt(debt)
                return
            case "2":
                debts.remove(debt)
                os.system("clear")
                return
            case "q":
                raise SystemExit
            case _:
                os.system("clear")
                print("that doesn't work try 1 or 2")



def update_debt(debt: debts.Debt):
    print("Select what you'd like to update")
    while True:
        print("1 Update Total\n2 Update Monthly Payment\n3 Update Target Payment\n4 Update Interest\n5 Update Name\n6 Make Payment")
        selection = input()
        match selection:
            case "1":
                total = input_loop("the total")
                debt.total = total
                pretty_print(debt)
                return
            case "2":
                mon_payment = input_loop("your monthly payment")
                debt.monthly_payment = mon_payment
                pretty_print(debt)
                return
            case "3":
                targ_payment = input_loop("your target payment, or total you would like to pay")
                debt.target_payment = targ_payment
                pretty_print(debt)
                return
            case "4":
                interest = input_loop("the debt's interest rate, just the number not \'%\'")
                debt.interest = interest
                pretty_print(debt)
                return
            case "5":
                print("Give the new name you would like to call this debt")
                new_name = input()
                debt.name = new_name
                pretty_print(debt)
                return
            case "6":
                while True:
                    payment = input_loop("the Payment you want to apply")
                    try:
                        debt.make_payment(payment)
                        pretty_print(debt)
                        return
                    except ValueError as e:
                        print(e)
            case "q":
                raise SystemExit
            case _:
                os.system("clear")
                print("That doesn't work, Select from options")
    
                
def show_all_debts(debts):
    print("\n" * 3)
    print("*" * 20)
    for i,debt in enumerate(debts, start=1):
        print(str(i) + " " + debt.name)
        print("*" * 20)
    print("\n"*3)


def pretty_print(debt):
    os.system("clear")
    print("\n")
    print(debt)
    print("\n" * 3)
