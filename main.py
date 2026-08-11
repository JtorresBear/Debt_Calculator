import debts
import json
import json_helper


test_debt = debts.Debt("Firstmark","31,000","500","600",5)
test_debt2 = debts.Debt("Firstmark","31,000","500","600",5)
test_debt3 = debts.Debt("Firstmark","31,000","500","600",5)
test_debt4 = debts.Debt("Firstmark","31,000","500","600",5)
test_debt5 = debts.Debt("Firstmark","31,000","500","600",5)
test_debts = [test_debt,test_debt2,test_debt3,test_debt4,test_debt5]
random_arr = [5,6,22,3]
random_arr2 = [5,6,6,4,2,3]
random_arr3 = [5,6,2,34,2,3]
random_arr4 = {"debt": test_debt, "lists_of_lists":[random_arr,random_arr2,random_arr3],"list_of_less_2": [random_arr,random_arr3]}





def main():
    test_debt = debts.Debt("Firstmark","31,000","500","600",5)
    #print(test_debt)
    is_running = True
    while is_running:
        print("please input 1, 2 or 3")
        inp = input("press 1")

        if inp == "1":
            is_running = False
    
    str_of_json_dump = json.dumps(test_debts,indent=1,default=json_helper.json_defaults)
    #print(str_of_json_dump)
    m = test_debt.months_left_with_monthly_payment()
    objects = json.loads(str_of_json_dump,object_hook=json_helper.json_object_hook)
    print(objects)
    

main()