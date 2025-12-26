## import abstact base class and abstract method from abstract module
from abc import ABC, abstractmethod
## create abstract class named as payment
class Payment(ABC):
## define abstract method process_payment
    @abstractmethod
    ## this is madatory for every class who inherit Payment class  to implemet this method
    def process_payment(self,amount):
        pass
## created Phonepay class which inherit Payment class
class PhonePay(Payment):
    def process_payment(self,amount):
        return ("Processing Payment of RS.", amount)
 ## created GooglePay class which inherit Payment class   
class GooglePay(Payment):
    def process_payment(self,amount):
        return ("Processing Payment of RS.", amount)

phonepay = PhonePay()
googlepay = GooglePay()
print(phonepay.process_payment(500))
print(googlepay.process_payment(1000))  


