
import pandas as pd

data = {
    "Name": ["Arun", "Priya", "Kavi", "Ravi", "Divya"],
    "Age": [22, 20, 24, 21, 20],
    "Department": ["MCA", "BCA", "MCA", "BCA", "MCA"],
    "Mark": [85, 92, 76, 88, 92]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

print("\n1. Ascending Order by Age:")
print(df.sort_values(by="Age", ascending=True))

print("\n2. Descending Order by Mark:")
print(df.sort_values(by="Mark", ascending=False))

print("\n3. Sorting by Department and Mark:")
print(df.sort_values(
    by=["Department", "Mark"],
    ascending=[True, False]
))
