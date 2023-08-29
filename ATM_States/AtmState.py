from abc import ABC, abstractmethod

class ATMState(ABC):

    @abstractmethod
    def Insercard(self, card):
        pass

    @abstractmethod
    def authenticateCard(self, card, pin):
        pass

    @abstractmethod
    def SelectionState(self, pin, card, txntype):
        pass

    @abstractmethod
    def withdrawMoneyState(self, card, amount):
        pass

    @abstractmethod
    def displaBalance(self, card):
        pass

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def returncard(self):
        pass