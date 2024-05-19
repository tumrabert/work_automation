import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('icloud_template.csv')

# Convert the DataFrame to a list of lists excluding the header
data = df.values.tolist()

for row in data:
    print(row)