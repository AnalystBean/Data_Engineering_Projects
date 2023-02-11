import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Load the dataset
df = pd.read_csv('creditcard.csv')

# Preprocessing
# - Split the data into features and labels
X = df.drop('Class', axis=1)
y = df['Class']

# - Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# - Scale the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Modeling
# - Train a logistic regression model
model = LogisticRegression(solver='lbfgs')
model.fit(X_train, y_train)

# Evaluation
# - Make predictions on the test set
y_pred = model.predict(X_test)

# - Evaluate the model performance
print(classification_report(y_test, y_pred))