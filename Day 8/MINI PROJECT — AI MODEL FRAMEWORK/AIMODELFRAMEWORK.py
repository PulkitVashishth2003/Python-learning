## fetching abstract base class module to work on
from abc import ABC, abstractmethod
class AIModel(ABC):
##  by securig the object details it shows encapsulation
    def __init__(self,data):
        self.__data = data  # encapsulated data

  ## example of abstraction in the program
    @abstractmethod
    def predict(self):
        pass

## by taking AIModel as in another class it shows inheritence
class FraudDetector(AIModel):
    def predict(self):
        print("Fraud detected in ", self._AIModel__data)


class MalwareDetector(AIModel):
    def predict(self):
        print("Malware detected in ", self._AIModel__data)

## by making two object of same method in different class it bring polymorphism
models = [FraudDetector("Data1"), MalwareDetector("Data2")]

for model in models:
    model.predict()