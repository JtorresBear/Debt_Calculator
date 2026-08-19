
import tool_manager
from pathlib import Path
import json_helper
import os



def main():
    total_debts = json_helper.load_objects()
    kill_count = 5
    try:
        main_loop(total_debts,kill_count)
    except SystemExit:
        json_helper.save_objects(total_debts)
    json_helper.save_objects(total_debts)

def main_loop(total_debts,kill_count):
    while True:
            if kill_count == 0:
                print("No more tries, its over!")
                json_helper.save_objects(total_debts)
                break
            print("Select one of the options by inputting the corresponding number")
            print("1 Add Debt")
            if len(total_debts) > 0:
                print("2 Show Debts by Name")
                print("3 Update or Delete")
                print("4 View Singular debt")
            print("q Quit (q works at any selection point)")
            selection = input()
            match selection:
                case "1":
                    os.system("clear")
                    print("\n")
                    total_debts.append(tool_manager.add_dept())
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
                case "q":
                    break
                case "Do a barrel roll":
                    os.system("clear")
                    print("This isn't google. We can't do that. :( \n" * 10)
                case _:
                    kill_count -= 1
                    if kill_count > 0 : print(f"Your option doesn't work. Try again or after {kill_count} more tries it will end automatically.")

main()