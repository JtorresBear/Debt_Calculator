

class Debt:
    def __init__(self,name,total, monthly_payment, target_payment,months_left):
        self.name = name
        self.total = total
        self.monthly_payment = monthly_payment
        self.target_payment = target_payment
        self.months_left = months_left

    def months_left_with_monthly_payment(self):
        return int(self.total.replace(',',""))/int(self.monthly_payment.replace(',',""))

    def __repr__(self):
        return f"{self.name} has a Total Debt: {self.total}\nMonthly_payment: {self.monthly_payment}.\nWith target payment of {self.target_payment} your debt will be settled in {self.months_left} months"
    

#fix this 
#still needs fixing. 
def custom_json(obj):
    if isinstance(obj, complex):
        return {'__complex__': True, 'real': obj.real, 'imag': ["this","that","the other"]}
    raise TypeError(f'Cannot serialize object of {type(obj)}')