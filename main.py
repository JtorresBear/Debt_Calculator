
import tool_manager
import json_helper
import os
import debts



def main():
    total_debts = json_helper.load_objects()
    tries_left = 5
    try:
        main_loop(total_debts,tries_left)
    except SystemExit:
        pass
    json_helper.save_objects(total_debts)

def main_loop(total_debts,tries_left):
    while True:
            if tries_left == 0:
                print("No more tries, its over!")
                break
            print("Select one of the options by inputting the corresponding number")
            print("1 Add Debt")
            if len(total_debts) > 0:
                print("2 Show Debts by Name")
                print("3 Update or Delete")
                print("4 View Singular Debt")
                print("5 View total debt between all Debts")
            print("q Quit (q works at any selection point)")
            selection = input()
            match selection:
                case "1":
                    os.system("clear")
                    print("\n")
                    total_debts.append(tool_manager.add_debt())
                case "2":
                    os.system("clear")
                    print("\n")
                    tool_manager.show_all_debts(total_debts)
                case "3":
                    debt_selection = tool_manager.get_debt(total_debts)
                    debt = total_debts[debt_selection-1]
                    tool_manager.update(total_debts,debt)
                case "4":
                    debt_selection = tool_manager.get_debt(total_debts)
                    debt = total_debts[debt_selection-1]
                    os.system("clear")
                    print("\n")
                    print(debt)
                    print("\n\n")
                case "5":
                    total_debt_owed = 0
                    for debt in total_debts:
                        total_debt_owed += debt.total
                    os.system("clear")
                    print("\n")
                    print(f"Between all your debts you owe a total amount of ${total_debt_owed}")
                    print("\n"* 3)
                case "q":
                    break
                case "Do a barrel roll":
                    os.system("clear")
                    print("This isn't google. We can't do that. :( \n" * 10)
                case _:
                    tries_left -= 1
                    if tries_left > 0 : print(f"Your option doesn't work. Try again or after {tries_left} more tries it will end automatically.")

main()