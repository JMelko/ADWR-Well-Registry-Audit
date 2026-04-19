import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

# Database credentials
DB_PARAMS = {
    "host": "localhost",
    "port": "5432",
    "database": "adwr_groundwater",
    "user": "env_analyst",
    "password": "tucson_water"
}

print("Querying database for plotting...")

try:
    connection = psycopg2.connect(**DB_PARAMS)
    
    # We can write the filter directly into our SQL query to save Python some work
    # We also ensure we don't pull blank/null depths which would crash the plotter
    query = """
        SELECT well_type, well_depth 
        FROM pima_wells_production 
        WHERE well_type != 'EXEMPT' 
        AND well_depth >0;
    """
    df = pd.read_sql_query(query, connection)
    
    print(f"Data loaded. Generating histogram for {len(df)} wells...")

    # --- Plotting the Data ---
    # 1. Set the canvas size
    plt.figure(figsize=(10, 6))
    
    # 2. Create a histogram
    # We limit the x-axis to 2000 feet so that the 8000ft outlier doesn't squash all 
    # the normal data into a single invisible bar on the far left of the screen.
    plt.hist(df['well_depth'], bins=40, range=(0, 2000), color='#2ca02c', edgecolor='black')
    
    # 3. Add professional labels
    plt.title('Distribution of Commercial/Monitor Well Depths in Pima County (0 - 2000 ft)', fontsize=14, fontweight='bold')
    plt.xlabel('Well Depth (feet)', fontsize=12)
    plt.ylabel('Frequency (Number of Wells)', fontsize=12)
    
    # 4. Add a subtle grid for readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # 5. Save the output as a high-res image
    output_filename = 'well_depth_distribution.png'
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    
    print(f"Success! Chart saved to your project folder as: {output_filename}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'connection' in locals():
        connection.close()