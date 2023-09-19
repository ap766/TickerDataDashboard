# TickerDataDashboard
## About
1. Data is listed below for one ticker symbol. Create a table in a database (Postgres or MySQL). Use Python to insert data into the database.
2. Build a simple app with React frontend and FastAPI backend. The user has two options:

a. Upload Data: By clicking this button, the user should upload the CSV data and with the help of Rest APIs, the FastAPI backend should insert the data in the DB.
b. Get data: On clicking this button, the API should fetch data from the DB and display it on the React frontend as a table.

## OUTPUTS 
### 1)The Output
![t1 - Copy (3)](https://github.com/ap766/TickerDataDashboard/assets/79255079/0981e7ea-9c91-4a3b-a712-962762ad1d5b)

### 2)Selecting and Uploading File
![t2](https://github.com/ap766/TickerDataDashboard/assets/79255079/efbb489c-328f-4812-afe7-c7e51bb77070)

### 3)Uploaded File
![t3 - Copy (2)](https://github.com/ap766/TickerDataDashboard/assets/79255079/eeb1cbee-68ae-4d84-ad89-4abb31102541)

### 4)Clicking _Upload Data_
![t4 - Copy (2)](https://github.com/ap766/TickerDataDashboard/assets/79255079/9fa6330a-a6f7-4d10-9f18-2642a4619b20)

### 5)MySQL Table Created and Data Inserted
![t5](https://github.com/ap766/TickerDataDashboard/assets/79255079/e85d5087-be11-4254-94b5-7e66ee5e6676)

### 6)Clicking _Get Data_
![t6 - Copy (2)](https://github.com/ap766/TickerDataDashboard/assets/79255079/90fe3cdf-63c2-499d-ba8a-db95f9e05786)

## HOW TO RUN IT?
### 1)env file
`Make a .env file in api folder of backend and fill DATABASE_NAME,MYSQL_USER,MYSQL_PASSWORD`

### 2)Backend 
```

cd backend
pipenv install fastapi dotenv mysql.connector 
pipenv shell
cd api
uvicorn main:app --reload
```
**Backend would be up and running!**

### 3)Frontend
```
cd frontend
npm i
npm run start
```
**Frontend would be up and running!**

`File uploaded here is HINDALCO_1D which is a csv file which you need to download and upload by choosing select file`




   


