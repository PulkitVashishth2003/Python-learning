from abc import ABC, abstractmethod
## example of abstraction in the program
class AIModel(ABC):
    @abstractmethod
    def predict(self):
        pass

## by taking AIModel as in another class it shows inheritence
class FraudDetector(AIModel):
    def predict(self):
        print("Fraud detected")


class MalwareDetector(AIModel):
    def predict(self):
        print("Malware detected")

## by making two object of same method in different class it bring polymorphism
models = [FraudDetector(), MalwareDetector()]

for model in models:
    model.predict()
## and if i give some data to the on=bject and make it private to access in the 
## code it will show the example of encapsulation