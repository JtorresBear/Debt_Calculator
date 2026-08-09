import debts
import json
import json_helper


test_debt = debts.Debt("Firstmark","31,000","500","600",5)
random_arr = [5,6,22,3]
random_arr2 = [5,6,6,4,2,3]
random_arr3 = [5,6,2,34,2,3]
random_arr4 = {"debt": test_debt, "lists_of_lists":[random_arr,random_arr2,random_arr3],"list_of_less_2": [random_arr,random_arr3]}





def main():
    print("Eventually, this will all be something")
    test_debt = debts.Debt("Firstmark","31,000","500","600",5)
    #print(test_debt)
    is_running = False
    while is_running:
        print("is running")
    str_of_json_dump = json.dumps(random_arr4,indent=1,default=json_helper.json_defaults)
    print(str_of_json_dump)
    m = test_debt.months_left_with_monthly_payment()
    print(m)

main()