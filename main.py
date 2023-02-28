from abc import ABC


class Wallet(ABC):
    def __init__(self, name: str, _type: str = 'General'):
        self.balance: int = 0
        self.name: str = name
        self.type: str = _type

    def get_balance(self) -> int:
        return self.balance

    def change_balance(self, value: int):
        if self.balance + value < 0:
            print(f'Not enough balance {self.balance}')
        else:
            self.balance += value


class CreditBalance:
    def change_balance(self, value: int):
        if self.balance + value < self.limit:
            print(f'Not enough balance {self.balance}')
        else:
            self.balance += value


class ProBalance:
    def change_balance(self, value: int):
        if self.balance + value * 0.95 < 0:
            print(f'Not enough balance {self.balance}')
        else:
            self.balance += value * 0.95 if self.balance + value * 0.95 < self.balance else value


class CreditCard(CreditBalance, Wallet):
    def __init__(self, name, limit=-1000):
        self.limit = limit
        super().__init__(name)


class Card(Wallet):
    def __init__(self, name):
        super().__init__(name)

    def change_card(self):
        if self.balance < 100:
            print(f'Not enough balance {self.balance}')
        else:
            self.balance -= 100
            _card = ProCard(self.name)
            _card.balance = self.balance
            return _card


class ProCard(ProBalance, Wallet):
    def __init__(self, name, _type='PRO'):
        super().__init__(name, _type)


card = ProCard('Sam')
print(card.get_balance())
card.change_balance(1000)
print(card.get_balance())
card.change_balance(-800)
print(card.get_balance())
card.change_balance(-250)
print(card.get_balance())
