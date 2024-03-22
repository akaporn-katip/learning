import pandas as pd

inventory = pd.read_csv("./data.csv")

print(inventory["QuantitySold"].mean())
print(inventory.to_json(orient='records', lines=False))

