import sys
import pandas as pd

#input_file_path = "SampleFile.xlsx"
export_file_name = "SplitColumn.xlsx"
input_file_column_name = "name"


if __name__ == '__main__':
    print("Split Column program")
    input_file_path=sys.argv[1]
    df = pd.read_excel(input_file_path)
    df = df[input_file_column_name].str.split(expand=True, pat=',')
    df = df.apply(lambda x: x.str.capitalize())
    df = pd.DataFrame(data={"First":df[1], "Last":df[0]})
    df.to_excel(export_file_name, index=False)
    print("Ending Split Column Program")
