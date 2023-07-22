from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import csv
import mysql.connector
from fastapi import HTTPException 
import os
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

# Configure CORS to allow requests from specified origins
origins = [
    "http://localhost:3000",
    "http://localhost:3002",
    "http://localhost:3003"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Configuration for MySQL database connection
db_config = {
    "host": "localhost",
    "user": os.getenv("MYSQL_USER","root"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "database": os.getenv("DATABASE_NAME"),
    "auth_plugin": 'mysql_native_password'
}


def create_table():
    # Create the table if it doesn't exist
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tickerdata1 (
            datetime VARCHAR(30) PRIMARY KEY,
            close FLOAT,
            high FLOAT,
            low FLOAT,
            open FLOAT,
            volume INT,
            instrument VARCHAR(20)
        )
        """
    )
    cursor.close()
    connection.close()


def insert_data(data):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    query = "INSERT INTO tickerdata1(datetime, close, high, low, open, volume, instrument) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(query, data)
    connection.commit()
    cursor.close()
    connection.close()


@app.post("/")
async def upload_csv(file: UploadFile = File(...)):
    # Receive POST request to upload csv file
    contents = await file.read()
    decoded_data = contents.decode("utf-8")
    csv_data = csv.reader(decoded_data.splitlines())
    
    next(csv_data)  # Skip header row if it exists
    data_to_insert = []

    # Call create_table() to create the table if it doesn't exist
    create_table()

    # Loop through csv_data and extract individual values, converting them to appropriate data types
    for row in csv_data:
        date = row[0]
        close = float(row[1])
        high = float(row[2])
        low = float(row[3])
        open_val = float(row[4])
        volume = int(row[5])
        instrument = row[6]

        # Append the converted values to data_to_insert as a tuple
        data_to_insert.append((date, close, high, low, open_val, volume, instrument))

    # Call insert_data() to insert the data into the MySQL database
    insert_data(data_to_insert)

    return JSONResponse(content={"message": "CSV data imported successfully"})


@app.get("/get-data")
async def get_data():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM tickerdata1")
        data = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        result = []
        for row in data:
            result.append(dict(zip(column_names, row)))
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        connection.close()



