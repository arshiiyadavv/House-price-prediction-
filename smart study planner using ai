import pandas as pd
import matplotlib.pyplot as plt
data = {
"Subject": ["Math", "Physics", "English", "AIML", "Chemistry"],
"Difficulty": ["Hard", "Medium", "Easy", "Hard", "Medium"]
}
df = pd.DataFrame(data)
difficulty_map = {
"Easy": 1,
"Medium": 2,
"Hard": 3
}
df["Difficulty_Value"] = df["Difficulty"].map(difficulty_map)
total_hours = int(input("Enter total study hours: "))
total_weight = df["Difficulty_Value"].sum()
df["Allocated_Hours"] = (df["Difficulty_Value"] / total_weight) * total_hours
df["Allocated_Hours"] = df["Allocated_Hours"].round(1)
for index, row in df.iterrows():
print(row["Subject"], ":", row["Allocated_Hours"], "hours")
plt.bar(df["Subject"], df["Allocated_Hours"])
plt.show()
