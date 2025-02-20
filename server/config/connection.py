# import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("DB_HOST_NAME")
USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# mydb = mysql.connector.connect(
#     host=HOST,
#     user=USER,
#     password=DB_PASSWORD
# )

# if mydb.is_connected():
#     print("CONNECTED TO MYSQL")
#     mydb.close()
# else:
#     print("failed to connect to DB")