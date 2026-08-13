

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
            return f"You'll be paying forever if your monthly payment is below or the same as {monthly_interest}"
        mon_count = 0
        while total >= 0:
            total = total + monthly_interest - self.monthly_payment
            monthly_interest = total * monthly_interest_rate
            mon_count +=1
        return f"You'll have {mon_count} left with your monthly payment of {self.monthly_payment}"

    def months_left_with_target_payment(self):
        total = self.total
        monthly_interest_rate = self.interest / 100.0 / 12.0
        monthly_interest = total * monthly_interest_rate
        if self.target_payment <= monthly_interest:
            return f"You'll be paying forever if your target monthly payment is below or the same as {monthly_interest}"
        mon_count = 0
        while total >= 0:
            total = total + monthly_interest - self.target_payment
            monthly_interest = total * monthly_interest_rate
            mon_count +=1
        return f"You'll have {mon_count} left with your target monthly payment of {self.target_payment}"
        

    def __repr__(self):
        return f"{self.name} has a Total Debt: {self.total}\nMonthly payment: {self.monthly_payment}.\nTarget payment: {self.target_payment}\n{self.months_left_with_monthly_payment()}\n{self.months_left_with_target_payment()}"
    
