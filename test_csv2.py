import pandas as pd

# Replace 'graft_data.csv' with the path to your actual CSV file
df = pd.read_csv('graft_data.csv', delimiter=',', engine='python', on_bad_lines='skip')

# Print the DataFrame columns
print("Columns in DataFrame:", df.columns)

