class TextModel:
    def predict(self):
        print("Predicting text output")


class ImageModel:
    def predict(self):
        print("Predicting image output")


models = TextModel(), ImageModel()

for model in models:
    model.predict()
