import unittest
from debts import Debt
import json_helper
from pathlib import Path

class TestDebt(unittest.TestCase):

    def test_make_payment(self):
        main_debt = Debt("First Debt",123456,200,400,1)
        main_debt.make_payment(400)
        self.assertEqual(main_debt.total,123056)

    def test_monthly_payoff_months(self):
        test_debt = Debt("Test",1000,200,300,5)
        months_left = test_debt.months_left_with_monthly_payment()
        self.assertEqual(months_left,6)

    def test_target_payoff_months(self):
        test_debt = Debt("Test",1000,200,300,5)
        months_left = test_debt.months_left_with_target_payment()
        self.assertEqual(months_left,4)

    def test_months_with_0_interest(self):
        test_debt = Debt("Test",1000,200,300,0)
        mon_months = test_debt.months_left_with_monthly_payment()
        targ_months = test_debt.months_left_with_target_payment()
        self.assertEqual(mon_months,5)
        self.assertEqual(targ_months,4)

    def test_payment_less_than_monthly(self):
        test_debt = Debt("Test",1000,200,300,0)

        with self.assertRaises(ValueError):
            test_debt.make_payment(100)

    def test_paid_off_debt_payment(self):
        test_debt = Debt("Test",0,200,300,0)

        with self.assertRaises(ValueError):
            test_debt.make_payment(200)

    def test_for_0(self):
        test_debt = Debt("Test",1000,200,300,0)
        test_debt.make_payment(1200)

        self.assertEqual(test_debt.total,0)

    def test_payments_too_low(self):
        test_debt = Debt("Test",10000,200,300,50)

        self.assertEqual(test_debt.months_left_with_target_payment(),"too many")
        self.assertEqual(test_debt.months_left_with_monthly_payment(),"too many")
    def test_json(self):
        original_debt = Debt("Done_debt",20000,500,550,10)
        json_helper.save_objects(original_debt, Path("test_case"))
        loaded_debt = json_helper.load_objects(path=Path("test_case"))
        self.assertEqual(loaded_debt.name,original_debt.name)




if __name__ == "__main__":
    unittest.main()