class Model:
    def __init__(self,value):
        self.__value = value

    def print_value(self):
        return self.__value

model = Model(10)
print(model.print_value())