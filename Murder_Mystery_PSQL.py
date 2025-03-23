import psycopg2 as psql, sqlalchemy, pandas as pd, glob, re

def exporting_to_postgres(df, conf, table_name):
    engine = f"postgresql+psycopg2://{conf['user']}:{conf['password']}@{conf['host']}:{conf['port']}/{conf['database']}"
    df.to_sql(
        name = table_name,
        con = engine,
        schema = conf['schema_name'],
        if_exists ='replace',
        index = False,
        method = 'multi',
        chunksize = 1000
    )
    print('The exporting process done.')

# to get the table name need to extract it from the csv file name and splitting the folder structure into csv and further split the .csv

def creating_dataframe(csv, conf):
    df = pd.read_csv(csv)
    table_name = csv.split('/')
    table_name = table_name[-1]
    table_name = table_name.split('.')[0]
    exporting_to_postgres(df, conf, table_name)

# getting the column names from the extracted CSV file

def get_col_name(files, conf):
    file_name = []
    for file in files:
        file_names = re.split(r'\\', file)
        file_name.append('/'.join(file_names))
    for csv_file in file_name:
        creating_dataframe(csv_file, conf)
        # print(csv_file)

if __name__ == '__main__':
    files = glob.glob(r"C:\Users\shaik\OneDrive\Documents\Codes\SQL\Murder_Mystery\Dataset\CSV\*")

    conf = {
        'host' : "localhost",
        'port' : "5432",
        'database' : "murder_mystery",
        'schema_name' : 'murd_myst',
        'user' : "SQLTools",
        'password' : "root"
    }

    get_col_name(files, conf)