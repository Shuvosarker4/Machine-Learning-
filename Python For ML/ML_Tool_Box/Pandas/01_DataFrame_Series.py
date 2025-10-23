import pandas as pd

# Pandas is used for
# --> Data Cleaning
# --> Data Manipulation, Analysis and Visualization

data = {
    "Product": ["Laptop", "Tablet", "Mobile", "Headphones", "Charger"],
    "Price": [80000, 30000, 20000, 5000, 1500],
    "Quantity": [10, 25, 50, 40, 60],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories"],
}

# DataFrame (two dimensional labeled data structure)
df = pd.DataFrame(data)
print(df) # Excel Sheet like Table(row*col) with index from 0

# Series (one dimentional labeled array)
s = pd.Series(data)
print(s) # Product [Laptop, Tablet, Mobile, Headphones, Charger]