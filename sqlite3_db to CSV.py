import sqlite3, pandas as pd, os

# Path to your SQLite database file
db_path = r"C:\Users\shaik\Downloads\Datasets\Murder Mystery Data\sql-murder-mystery.db"
export_folder = r"C:\Users\shaik\Downloads\Datasets\Murder Mystery Data\CSV"  # Folder to save CSV files

# Ensure export folder exists
os.makedirs(export_folder, exist_ok=True)

# Connect to SQLite database
conn = sqlite3.connect(db_path)

# Get list of all tables
query_tables = "SELECT name FROM sqlite_master WHERE type='table';"
tables = pd.read_sql(query_tables, conn)

# Export each table as a CSV file
for table in tables["name"]:
    df = pd.read_sql_query(f"SELECT * FROM {table};", conn)
    csv_path = os.path.join(export_folder, f"{table}.csv")  # File path
    df.to_csv(csv_path, index=False)  # Export to CSV (no index)
    print(f"Exported {table} to {csv_path}")

# Close database connection
conn.close()

print("\n✅ All tables have been exported successfully!")
