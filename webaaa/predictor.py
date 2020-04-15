import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

loto_data = pd.read_csv('outputs.csv')
X = loto_data['Year', 'day', 'month', 'date', 'index', 'LetterN']
Y = loto_data['No01', 'No02', 'No03', 'No04']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)


# X = loto_data.drop(columns=['Letter', 'No01', 'No02', 'No03', 'No04', 'DateFull'])
# Y = loto_data.drop(columns=['Letter', 'Year', 'day', 'month', 'date', 'index', 'LetterN', 'DateFull'])

model = DecisionTreeClassifier()
model.fit(X_train, Y_train)
predictions = model.predict(X_test)
score = accuracy_score(Y_test, predictions)
print(score)
