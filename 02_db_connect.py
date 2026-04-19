import pandas as pd
import psycopg2

# 1. Define the connection parameters (same as DBeaver)
DB_PARAMS = {
    "host": "localhost",
    "port": "5432",
    "database": "adwr_groundwater",
    "user": "env_analyst",
    "password": "tucson_water"
}

print("Connecting to the PostGIS database...")

try:
    # 2. Establish the connection using psycopg2
    connection = psycopg2.connect(**DB_PARAMS)
    
    # 3. Write our SQL query
    query = "SELECT * FROM pima_wells_production;"
    
    # 4. Use Pandas to run the query and store the result in a DataFrame
    df = pd.read_sql_query(query, connection)
    
    # 5. Print a success message and the first 5 rows
    print(f"Success! Loaded {len(df)} deduplicated well records.")
    print("-" * 50)
    print(df.head())

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # 6. Always close the connection when finished
    if 'connection' in locals():
        connection.close()
        print("-" * 50)
        print("Database connection closed safely.")