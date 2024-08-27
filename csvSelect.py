import pandas as pd

def select_columns(input_csv, output_csv, columns):
    """
    Select specific columns from a CSV file and save to a new CSV file.

    :param input_csv: Path to the input CSV file.
    :param output_csv: Path to the output CSV file where the result will be saved.
    :param columns: List of column names to select.
    """
    # Read the input CSV file
    df = pd.read_csv(input_csv)

    # Check if the requested columns are in the dataframe
    missing_columns = [col for col in columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Columns not found in the CSV file: {', '.join(missing_columns)}")

    # Select the specified columns
    df_selected = df[columns]

    # Save the selected columns to a new CSV file
    df_selected.to_csv(output_csv, index=False)
    print(f"Selected columns saved to {output_csv}")

# Example usage
input_csv_path = 'wpndatabase_Notification.csv'  # Replace with the path to your input CSV file
output_csv_path = 'output.csv'  # Replace with the path where you want to save the output
columns_to_select = ['Payload']  # Replace with the columns you want to select

select_columns(input_csv_path, output_csv_path, columns_to_select)