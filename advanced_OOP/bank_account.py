class AccountException(Exception):
    pass


class BankAccount:
    def __init__(self):
        self.__account_number = "76032012"
        self.__balance = 0

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    @account_number.setter
    def account_number(self,account_number):
        raise AccountException("You can't change the account number!")

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise AccountException("Balance must be positive!")
        elif value > 100_000:
            print("Please aware that the balance to be set is very high!")
        else:
            self.__balance = value

    @account_number.deleter
    def account_number(self):
        if self.__balance > 0:
            raise AccountException("You can't ask to delete the account when your account balance is not zero")
        else:
            self.__account_number = None


try:
    bank_account = BankAccount()
    print(bank_account.account_number)
    bank_account.balance = 1000
    #bank_account.balance = -200
    #bank_account.account_number = "76032011"
    bank_account.balance = 1000_000
    del bank_account.account_number
except AccountException as e:
    print(e)

