import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    "study_time": [1, 2, 3, 4, 5, 6, 7, 8, 2, 3, 5, 6, 7, 4, 8],
    "attendance": [50, 55, 60, 65, 70, 75, 80, 85, 58, 62, 72, 78, 82, 68, 88],
    "marks": [40, 45, 50, 55, 60, 65, 70, 75, 46, 52, 63, 67, 72, 58, 78]
}

df = pd.DataFrame(data)

X = df[["study_time", "attendance"]]
y = df["marks"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predicted_marks = model.predict([[5, 75]])

print("Predicted Marks:", predicted_marks[0])
