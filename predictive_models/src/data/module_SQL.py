import sqlite3 as sql
import pathlib as pl
import pandas as pd

# --- Database and CSV Paths Setup ---

path_db = pl.Path('../../data/raw/data_base.db')

# If an old database exists, delete it to start fresh.
if (path_db.exists()):
    path_db.unlink()
    print('Old database deleted.')
    conn = sql.connect(path_db)
else:
    print('Database created.')
    conn = sql.connect(path_db)

cursor = conn.cursor()

# Define paths to the source CSV files.
path_Estudiantes_csv = pl.Path('../../data/raw/Estudiantes Info.csv')
path_Materias_Inscritas_csv = pl.Path('../../data/raw/Materias Inscritas.csv')
path_PGA_csv = pl.Path('../../data/raw/PGA.csv')
path_notas_finales_csv = pl.Path('../../data/raw/Notas Finales.csv')

# --- Load CSVs into Pandas DataFrames ---
df_estudiantes = pd.read_csv(path_Estudiantes_csv, encoding='latin-1', low_memory=False, sep=';')
df_materias_inscritas = pd.read_csv(path_Materias_Inscritas_csv, encoding='latin-1', low_memory=False, sep=',')
df_pga = pd.read_csv(path_PGA_csv, encoding='latin-1', low_memory=False, sep=';')
df_notas_finales = pd.read_csv(path_notas_finales_csv, encoding='latin-1', low_memory=False, sep=';')

# --- Write DataFrames to SQL Tables ---
df_estudiantes.to_sql('Estudiantes_Info', conn, if_exists='replace', index=False)
df_materias_inscritas.to_sql('Materias_Inscritas', conn, if_exists='replace', index=False)
df_pga.to_sql('PGA', conn, if_exists='replace', index=False)
df_notas_finales.to_sql('Notas_Finales', conn, if_exists='replace', index=False)

# --- Execute SQL Transformation Scripts ---
print("Executing SQL scripts...")
for i in range(1, 6):
    # Ensure we are using the SQL files
    sql_file = pl.Path(f'./module_{i}.sql')
    with sql_file.open(encoding='utf-8') as f:
        sql_script = f.read()
        cursor.executescript(sql_script)
    print(f'Executed: ./module_{i}.sql')

conn.commit()

# --- Fetch Transformed Data and Save to CSV ---
df = pd.read_sql_query('SELECT * FROM data', conn)

out_path = pl.Path('../../data/raw/data.csv')
df.to_csv(out_path, index=False)

conn.close()
print("Transformed data saved to data.csv")

path = pl.Path('../../data/raw/data.csv')
df = pd.read_csv(path)

# Convert grade columns from string with comma decimal to float.
cols_com = df.columns[8:28].to_list()
for col in cols_com:
    if col in df.columns:
        try:
            df[col] = df[col].str.replace(',', '.').astype(float)
        except AttributeError:
            # Skip columns that are already numeric.
            pass

# Ensure all semester grade columns are numeric floats.
cols_flt = df.columns[9:28].to_list()
for col in cols_flt:
	if col in df.columns:
		df[col] = pd.to_numeric(df[col], errors='coerce').astype(float)


cols_int = ['student_id', 'age', 'gender', 'stratum', 'residence', 'civil_status', 'start_period', 'total_repetitions', 'deserter']
for col in cols_int:
	if col in df.columns:
		df[col] = df[col].fillna(0).astype(int)


grades = df.drop(columns=cols_int).replace(0, pd.NA)


df["average"] = grades.mean(axis=1, skipna=True)

# Drop original semester columns and start_period as they are no longer needed.
columns_to_drop = ['start_period'] + [f'semester_{i}' for i in range(1, 21)]
df = df.drop(columns=columns_to_drop)

# --- Save the Final Processed Dataset ---
destiny = pl.Path('../../data/processed/data_set.csv')
df.to_csv(destiny, index=False)

print("Data processing complete. Final dataset saved to data_set.csv")