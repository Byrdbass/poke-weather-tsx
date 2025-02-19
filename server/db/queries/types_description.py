import pandas as pd
from sqlalchemy import create_engine

DB_URL = "mysql+pymysql://user:password@localhost/db_name"
engine = create_engine(DB_URL)

query = "SELECT * FROM pokemon_weather_match"
df = pd.read_sql(query, engine)

# Convert categorical values (types, descriptions) into numerical form
df = pd.get_dummies(df, columns=['pokemon_type', 'weather_description'])

# Save processed data
df.to_csv("pokemon_weather_dataset.csv", index=False)

print("Data prepared for ML training!")
