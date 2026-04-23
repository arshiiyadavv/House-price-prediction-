import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
data = {
’Study_Hours’: [1,2,3,4,5,6,7,8,3,2,6,7,5,4,8],
’Attendance’: [50,55,60,65,70,75,80,85,58,52,78,82,74,66,90],
’Internal_Marks’: [40,42,45,50,55,60,65,70,48,41,62,68,58,52,75],
’Assignments’: [2,2,3,3,4,4,5,5,3,2,4,5,4,3,5],
’Grade’: [’F’,’F’,’D’,’D’,’C’,’C’,’B’,’A’,’D’,’F’,’B’,’A’,’C’,’D’,’A’]
}
df = pd.DataFrame(data)
encoder = LabelEncoder()
df[’Grade’] = encoder.fit_transform(df[’Grade’])
X = df.drop(’Grade’, axis=1)
y = df[’Grade’]
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42
)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
new_student = [[6, 78, 65, 4]]
prediction = model.predict(new_student)
print("Predicted Grade:", encoder.inverse_transform(prediction)[0])
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
