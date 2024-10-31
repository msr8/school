import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('1.csv')


# 1.1) Convert the categorical dataset into numerical format
les = {col: LabelEncoder() for col in df.columns}
for col in df.columns:
    df[col] = les[col].fit_transform(df[col])

# 1.2) Build a Decision Tree Classifier using the scikit-learn library
model = DecisionTreeClassifier()


# 1.3) Train the decision tree on the given dataset
X = df.drop('Buys Computer', axis=1)
y = df['Buys Computer']

model.fit(X, y)


# 1.4) Visualize the decision tree
plot_tree(model, feature_names=X.columns, class_names=['No', 'Yes'], filled=True)
plt.savefig('1.png', bbox_inches='tight')
plt.show()


# 2) Use the trained decision tree to predict whether the following individual will buy a computer or not:
# Age: 35; Income: Medium; Student: No; Credit Rating: Excellent
X_new = pd.DataFrame({'Age': ['31...40'], 'Income': ['Medium'], 'Student': ['No'], 'Credit Rating': ['Excellent']})
X_new = X_new.apply(lambda x: les[x.name].transform(x))

new_pred = model.predict(X_new)
new_pred = les['Buys Computer'].inverse_transform(new_pred)


# 3) Print the accuracy of the decision tree model and the predicted class for the individual
y_pred = model.predict(X)
accuracy = accuracy_score(y, y_pred)

print(f'Accuracy: {accuracy}')
print(f'Predicted class for the individual: {new_pred[0]}')


