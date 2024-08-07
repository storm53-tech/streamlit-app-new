import pandas as pd

def read_local_csv(file_path):
    try:
        df = pd.read_csv(file_path, delimiter=',', header=0)
        print("Columns in DataFrame:", df.columns)
        print("DataFrame preview:\n", df.head())
    except pd.errors.EmptyDataError:
        print("No data found in CSV file.")
    except pd.errors.ParserError:
        print("Error parsing CSV file.")
    except Exception as e:
        print(f"General error: {e}")

if __name__ == "__main__":
    read_local_csv('test_local.csv')  # Ensure this path matches your file location

