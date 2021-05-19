import pandas as pd

input_file_path = "SampleFile.csv"
export_file_name = "SplitColumn.csv"
input_file_column_name = "Full Name"


if __name__ == '__main__':
    df = pd.read_csv(input_file_path)
    df = df[input_file_column_name].str.split(expand=True)
    df.to_csv(export_file_name, index=False)
