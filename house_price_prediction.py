import pandas as pd
from sklearn.linear_model import LinearRegression

data = {'area': [1000, 1500, 2000, 2500],
        'price': [10, 15, 20, 25]}

df = pd.DataFrame(data)

X = df[['area']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

print(model.predict([[1800]]))
