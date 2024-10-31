import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv('3.csv')


# 1) Preprocess the dataset (handle missing values and encode categorical variables)
cols = ['Education', 'Marital Status', 'Credit History', 'Loan Approved']
les  = {col: LabelEncoder() for col in cols}
for col in cols:
    df[col] = les[col].fit_transform(df[col])
# As we can see in the below output, we don't have any missing values in the dataset
print(pd.isna(df).sum())


# 2) Train a decision tree model on the dataset
X = df.drop('Loan Approved', axis=1)
y = df['Loan Approved']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)


# 3) Test the model using a test dataset and evaluate its accuracy
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f'Accuracy: {acc}')


# 4) Predict whether a loan will be approved for a new applicant with the following details:
# Income: 50000; Loan Amount: 200000; Education: Graduate; Marital Status: Married; Credit History: Good
X_new = pd.DataFrame({'Income': [50000], 'Loan Amount': [200000], 'Education': ['Graduate'], 'Marital Status': ['Married'], 'Credit History': ['Good']})
for col in cols[:-1]:
    X_new[col] = les[col].transform(X_new[col])

new_pred = model.predict(X_new)
new_pred = les['Loan Approved'].inverse_transform(new_pred)
print(f'Predicted loan approval for the new applicant: {new_pred[0]}')


