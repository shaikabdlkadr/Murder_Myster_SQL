import psycopg2, csv, pandas as pd, glob, re

def creating_dataframe(csv):
    df = pd.read_csv(csv)
    return df

# getting the column names from the extracted CSV file
def get_col_name(files):
    file_name = []
    for file in files:
        file_names = re.split(r'[\\]', file)[-1]
        file_name.append(file_names.split('.')[0])
    return file_name


if __name__ == '__main__':
    files = glob.glob(r"C:\Users\shaik\OneDrive\Documents\Codes\SQL\Murder_Mystery\Dataset\CSV\*")
    print(get_col_name(files))

    conf = {
        'host' : "localhost",
        'port' : "5432",
        'database' : "murder_mystery",
        'user' : "SQLTools",
        'password' : "root"
    }