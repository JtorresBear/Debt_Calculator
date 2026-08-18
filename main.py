import debts
import tool_manager
from pathlib import Path
import json
import json_helper



def main():
    total_debts = json_helper.load_objects()
    kill_count = 5

    while True:
        if kill_count == 0:
            print("No more tries, its over!")
            json_helper.save_objects(total_debts)
            break
        print("Select one of the options by inputting the corresponding number")
        print("1 Add Debt")
        print("2 Show Debts by Name")
        if len(total_debts) > 0:
            print("3 Update or Delete")
        print("q Quit")
        selection = input()
        match selection:
            case "1":
                total_debts.append(tool_manager.add_dept())
            case "2":
                show_all_debts(total_debts)
            case "3":
                print("Select a Debt by corresponding number\n\n")
                show_all_debts(total_debts)
                debt_selection = tool_manager.get_debt(total_debts)
                print(total_debts[debt_selection-1])
            case "q":
                break
            case "Do a barrel roll":
                print("This isn't google. We can't do that. :( ")
            case _:
                kill_count -= 1
                if kill_count > 0 : print(f"Your option doesn't work. Try again or after {kill_count} more tries it will end automatically.")
    json_helper.save_objects(total_debts)



def show_all_debts(debts):
    print("\n" * 3)
    print("*" * 20)
    for i,debt in enumerate(debts, start=1):
        print(str(i) + " " + debt.name)
        print("*" * 20)
    print("\n"*3)


main()