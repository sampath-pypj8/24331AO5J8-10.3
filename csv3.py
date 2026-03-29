import pandas as pd
import numpy as np

data = {
    "Name": ["Ravi", "Sai", "Ram", "Kiran", None],
    "Marks": [85, 90, None, 88, 92],
    "Age": [20, None, 21, 22, 23]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Age"] = df["Age"].fillna(0)
df["Name"] = df["Name"].fillna("Unknown")

print("\nAfter filling missing values:")
print(df)
df_clean = df.dropna()

print("\nAfter dropping missing values:")
print(df_clean)
df["Marks"] = df["Marks"] + 5
df["Status"] = ["Pass" if m >= 90 else "Fail" for m in df["Marks"]]

print("\nModified DataFrame:")
print(df)