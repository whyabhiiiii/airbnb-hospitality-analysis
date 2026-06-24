import pandas as pd
import re
import psycopg2
from sqlalchemy import create_engine

# Redshift connection parameters
redshift_params = {
    'host': 'your_redshift_host',
    'port': '5439',
    'dbname': 'your_database',
    'user': 'your_username',
    'password': 'your_password'
}

# CSV file path and Redshift table name
csv_file = 'path/to/your/file.csv'
table_name = 'your_table_name'

# Read CSV file
df = pd.read_csv(csv_file)

# Function to clean column names
def clean_column_name(name):
    cleaned_name = re.sub(r'[^a-zA-Z_]', '_', name)
    return cleaned_name.strip('_').lower()

# Clean column names
df.columns = [clean_column_name(col) for col in df.columns]

# Create SQLAlchemy engine
engine = create_engine(f"postgresql://{redshift_params['user']}:{redshift_params['password']}@"
                       f"{redshift_params['host']}:{redshift_params['port']}/"
                       f"{redshift_params['dbname']}")

# Write DataFrame to Redshift table
df.to_sql(table_name, engine, index=False, if_exists='replace')

print(f"Data loaded successfully to table: {table_name}")
print(f"Number of rows: {len(df)}")
