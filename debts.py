

class Debt:
    def __init__(self,name,total, monthly_payment, target_payment,interest):
        self.name = name
        self.total = total
        self.monthly_payment = monthly_payment
        self.target_payment = target_payment
        self.interest = interest

    def months_left_with_monthly_payment(self):
        total = self.total
        monthly_interest_rate = self.interest / 100.0 / 12.0
        monthly_interest = total * monthly_interest_rate
        if self.monthly_payment <= monthly_interest:
            return "too many"
        mon_count = 0
        while total > 0:
            total = total + monthly_interest - self.monthly_payment
            monthly_interest = total * monthly_interest_rate
            mon_count +=1
        return mon_count

    def months_left_with_target_payment(self):
        total = self.total
        monthly_interest_rate = self.interest / 100.0 / 12.0
        monthly_interest = total * monthly_interest_rate
        if self.target_payment <= monthly_interest:
            return "too many"
        mon_count = 0
        while total > 0:
            total = total + monthly_interest - self.target_payment
            monthly_interest = total * monthly_interest_rate
            mon_count +=1
        return mon_count

    def make_payment(self,payment):
        if self.total == 0:
            raise ValueError("You completed paying off this Debt already according to these records.")     
        if payment < self.monthly_payment:
            raise ValueError("It cannot be less than your monthly payment")
        self.total = self.total - payment
        if self.total <= 0:
            self.total = 0
        return


    def __repr__(self):
        if self.total <= 0:
            return f"""{self.name} is paid off and can be deleted when you want. \nMonthly payment: {self.monthly_payment}.\nTarget payment: {self.target_payment}\n0 months left of payment""" 
        return f"""{self.name} has a Total Debt: {self.total}
        \nMonthly payment: {self.monthly_payment}.
        \nTarget payment: {self.target_payment}
        \nYou'll be paying for {self.months_left_with_monthly_payment()} months
        \nYou'll be paying for {self.months_left_with_target_payment()} months"""
    
