import pandas as pd

# Path to the CSV file
csv_file_path = 'test.csv'

try:
    # Read the CSV file with explicit delimiter and proper handling
    df = pd.read_csv(csv_file_path, delimiter=',', skipinitialspace=True)
    
    # Print DataFrame columns and a preview of the data
    print("Columns in DataFrame:", df.columns)
    print("DataFrame preview:\n", df.head())
except Exception as e:
    print(f"Error reading CSV file: {e}")

