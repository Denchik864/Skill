from abc import ABC


class Wallet(ABC):
    def __init__(self, name: str, type: str = "General"):
        self.balanse: int = 0
        self.name: str = name
        self.type: str = type

    def get_balance(self) -> int:
        return self.balanse
    def change_balance(self, value: int):
        if self.balanse + value < 0:
            print(f"Not enough balanse {self.balanse}")
        else:
            self.balanse += value

class CreditCard(Wallet):
    def __init__(self, name, limit=-1000):
        self.limit = limit
        super().__init__(name)
    def change_balance(self, value: int):
        if self.balanse + value < self.limit:
            print(f"Not enough balanse {self.balanse}")
        else:
            self.balanse += value

class Card(Wallet):
    def __init__(self, name):
        super().__init__(name)

    def change_type(self):
        if self.balanse < 100:
            print(f"Not enough balanse {self.balanse}")
        else:
            self.balanse -= 100
            card = ProCard(self.name)
            card.balanse = self.balanse
            return card

class ProCard(Wallet):
    def __init__(self, name, type="PRO"):
        super().__init__(name, type)
    def change_balance(self, value: int):
        if self.balanse + value * 0.95< 0:
            print(f"Not enough balanse {self.balanse}")
        else:
            self.balanse += value * 0.95 if self.balanse + value * 0.95 < self.balanse else value
      
card = Card("Sam")
print(card.get_balance())
card.change_balance(1000)
print(card.get_balance())
card.change_balance(-800)
print(card.get_balance())
card.change_balance(-300)
print(card.get_balance())
card = card.change_type()
print(card.type)
card.change_balance(-100)
print(card.get_balance())    
