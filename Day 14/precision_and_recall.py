from sklearn.metrics import precision_score, recall_score

precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)

print("Precision:", precision)
print("Recall:", recall)
