import pandas as pd

data = {
    'Name': ['Ram Roy', 'Jack Tom', 'Susan Jit', 'Jilt Joy'],
    'Age': [35, 37, 33, 40],
    'City': ['Mumbai', 'Delhi', 'Chennai', 'Kolkata'],
    'Occupation': ['Teacher', 'Doctor', 'Engineer', 'Architect'],
    'Salary': [75000, 90000, 85000, 70000]
}

df = pd.DataFrame(data)
df.to_csv('people.csv', index=False)
