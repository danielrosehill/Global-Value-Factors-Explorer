import pandas as pd
import os

# Paths provided
csv_path = "/home/daniel/Git/Global-Value-Factors-Explorer/Data/GVFD-Deriv/data/composite-data/csv/composite_value_factors.csv"
output_dir = "/home/daniel/Git/Global-Value-Factors-Explorer/Data/GVFD-Deriv/data/composite-data/other-formats"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_path)

# Convert to JSON and write to file
json_output_path = os.path.join(output_dir, "composite_value_factors.json")
df.to_json(json_output_path, orient="records", lines=True)  # 'lines=True' for JSON lines format

# Convert to Parquet and write to file
parquet_output_path = os.path.join(output_dir, "composite_value_factors.parquet")
df.to_parquet(parquet_output_path, index=False)  # 'index=False' to exclude the index from the Parquet file

print(f"Files have been successfully written to {output_dir}:")
print(f"JSON: {json_output_path}")
print(f"Parquet: {parquet_output_path}")
