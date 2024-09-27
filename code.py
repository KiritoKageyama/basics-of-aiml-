import os
import pandas as pd

# Function to load the dataset from a manually uploaded file
def load_dataset(file_path):
    # Check if the file exists
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        print(f"\nDataset '{file_path}' loaded successfully!")
        return df
    else:
        print(f"File '{file_path}' not found. Please check the path.")
        return None

# Function to export the dataset and display information
def export_dataset(df, file_path):
    if df is None:
        print("No dataset to export. Exiting.")
        return
    
    # Export the dataset to a CSV file
    df.to_csv(file_path, index=False)
    print(f"\nDataset exported successfully to {file_path}") 

    # Display basic dataset information
    print("\n1. Number of Rows and Columns:")
    print(df.shape)

    print("\n2. First Five Rows:")
    print(df.head())

    print("\n3. Number of Missing Values per Column:")
    print(df.isnull().sum())

    print("\n4. Summary of Numerical Columns:")
    print("Sum of values:")
    print(df.select_dtypes(include='number').sum())

    print("\nAverage of values:")
    print(df.select_dtypes(include='number').mean())

    print("\nMinimum values:")
    print(df.select_dtypes(include='number').min())

    print("\nMaximum values:")
    print(df.select_dtypes(include='number').max())

    return df

# Main execution
if __name__ == "__main__":
    # Set your file path here
    file_path = "california_housing_test.csv"

    # Load and process dataset
    df = load_dataset(file_path)

    # Export the dataset (optional)
    output_file = 'output_data.csv'
    export_dataset(df, output_file)
