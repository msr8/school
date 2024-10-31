from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 500


# 1) Use the Titanic dataset available from seaborn library in Python
df = sns.load_dataset('titanic')
le = LabelEncoder()
df['sex'] = le.fit_transform(df['sex'])


# 2) Split the dataset into training and testing sets (80/20)
X = df[['pclass', 'sex', 'age', 'fare']]
y = df['survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# 3) Train a decision tree model using scikit-learn
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)


# 4) Evaluate the model using accuracy and confusion matrix
acc = accuracy_score(y_test, clf.predict(X_test))
cm  = confusion_matrix(y_test, clf.predict(X_test))
ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['No', 'Yes']).plot()
plt.savefig('2-1.png', bbox_inches='tight')
plt.show()
print(f'Accuracy: {acc}')


# 5) Predict the survival for a new passenger with the following attributes:
# Class:1st; Sex:Female; Age:25; Fare:100
X_new = pd.DataFrame({'pclass': [1], 'sex': le.transform(['female'])[0], 'age': [25], 'fare': [100]})
new_pred = clf.predict(X_new)
print(f'Predicted survival for the new passenger: {new_pred[0]}')


# 6) Visualize the decision tree
plot_tree(clf, feature_names=X.columns, class_names=['No', 'Yes'], filled=True)
plt.savefig('2-2.png', bbox_inches='tight')
plt.show()


