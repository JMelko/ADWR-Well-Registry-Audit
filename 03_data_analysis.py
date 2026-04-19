import pandas as pd
import psycopg2

# Database credentials
DB_PARAMS = {
    "host": "localhost",
    "port": "5432",
    "database": "adwr_groundwater",
    "user": "env_analyst",
    "password": "tucson_water"
}

try:
    # 1. Connect and Load Data
    print("Connecting to database and pulling records...")
    connection = psycopg2.connect(**DB_PARAMS)
    query = "SELECT * FROM pima_wells_production;"
    df = pd.read_sql_query(query, connection)
    
    print("-" * 50)
    
    # 2. Explore the Categories (Value Counts)
    print("TOP 5 WELL TYPES IN PIMA COUNTY:")
    # .value_counts() groups the data by type and counts the rows
    print(df['well_type'].value_counts().head(5)) 
    print("-" * 50)

    # 3. Filter the Data (The Boolean Mask)
    # ADWR classifies standard domestic wells as "EXEMPT". We want to remove them.
    # We are asking Pandas to keep rows where the well_type is NOT EQUAL (!=) to EXEMPT
    commercial_wells = df[df['well_type'] != 'EXEMPT']
    
    print(f"Total wells: {len(df)}")
    print(f"Commercial/Industrial/Monitor wells: {len(commercial_wells)}")
    print("-" * 50)

    # 4. Calculate Descriptive Statistics
    print("DEPTH STATISTICS FOR COMMERCIAL WELLS (in feet):")
    # .describe() automatically calculates count, mean, std, min, max, and percentiles
    depth_stats = commercial_wells['well_depth'].describe()
    
    # We round it to 2 decimal places to make it look professional
    print(depth_stats.round(2))
    print("-" * 50)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'connection' in locals():
        connection.close()