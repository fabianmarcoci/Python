
class Account:

    def __init__(self, full_name, personal_id):
        self.full_name = full_name
        self.personal_id = personal_id
        self.funds = 0

    def deposit(self, amount):
        if amount <= 0:
            print("Amount should be positive.")
            return
        self.funds += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount should be positive.")
            return
        if amount > self.funds:
            print("Insufficient funds.")
            return
        self.funds -= amount
        return amount


class SavingsAccount(Account):
    used_ids = set()

    def __init__(self, full_name, personal_id, interest_percent=1.6):
        if personal_id in SavingsAccount.used_ids:
            print("Personal ID already in use for a saving account.")
            return
        super().__init__(full_name, personal_id)
        self.interest_percent = interest_percent / 100
        SavingsAccount.used_ids.add(personal_id)

    def calculate_monthly_interest(self):
        return self.interest_percent * self.funds


class CheckingAccount(Account):
    used_ids = set()

    def __init__(self, full_name, personal_id):
        if personal_id in CheckingAccount.used_ids:
            print("Personal ID already in use for a checking account.")
            return
        super().__init__(full_name, personal_id)
        CheckingAccount.used_ids.add(personal_id)

    def calculate_monthly_interest(self):
        print("Checking accounts don't have an interest.")
        return 0
