import pandas as pd
import zipfile
import io
from google.cloud import storage

def fetch_latest_data():
    """
    Fetch data from Google Cloud Storage and return it as a DataFrame.
    """
    try:
        client = storage.Client()
        bucket_name = 'lindyscore'  # Update with your actual bucket name
        file_name = 'Files.zip'
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        zip_content = blob.download_as_bytes()

        # Extract the zip file
        with zipfile.ZipFile(io.BytesIO(zip_content)) as z:
            print(f"Zip file contains: {z.namelist()}")
            for file_info in z.infolist():
                print(f"Extracting file: {file_info.filename}")  # Debugging
                with z.open(file_info) as file:
                    # Read and print the content to check
                    content = file.read().decode('utf-8')
                    print("File content:\n", content)  # Debugging
                    
                    # Convert string content to a file-like object
                    csv_file = io.StringIO(content)
                    
                    # Read CSV with different options
                    try:
                        df = pd.read_csv(csv_file, delimiter=',', engine='python', on_bad_lines='skip')
                        print("Columns in DataFrame:", df.columns)  # Debugging
                        print("DataFrame preview:\n", df.head())  # Debugging
                    except pd.errors.EmptyDataError:
                        print("No data found in CSV file.")
                        return pd.DataFrame()
                    except pd.errors.ParserError:
                        print("Error parsing CSV file.")
                        return pd.DataFrame()
                    except Exception as e:
                        print(f"General error: {e}")
                        return pd.DataFrame()
                    
                    break  # Assuming there's only one file in the zip

        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()

def main():
    df = fetch_latest_data()
    print("Final DataFrame:\n", df)

if __name__ == "__main__":
    main()

