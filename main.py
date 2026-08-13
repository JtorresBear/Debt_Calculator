import debts
import tool_manager
import json
import json_helper

firstmark = debts.Debt("FirstMark", 31000,497,500,10)


def main():
    total_debts = []
    kill_count = 5

    while True:
        if kill_count == 0:
            print("No more tries, its over!")
            break
        print("Select one of the options by inputting the corresponding number")
        print("1 Add Debt")
        print("2 Quit")
        selection = input()
        match selection:
            case "1":
                total_debts.append(tool_manager.add_dept())
            case "2":
                break
            case "Do a barrel roll":
                print("This isn't google. We can't do that. :( ")
            case _:
                kill_count -= 1
                if kill_count > 0 : print(f"Your option doesn't work. Try again or after {kill_count} more tries it will end automatically.")

    for debt in total_debts:
        print(debt)



main()