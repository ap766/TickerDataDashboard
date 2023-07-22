import React, { useState, useEffect } from "react";
import ReactDOM from "react-dom";
import "./index.css";

function App() {

  //the functions used to upload csv data to the database are handleOnChange, handleOnSubmit.
  //the function used to get data from the database is handleGetData.

  const [file, setFile] = useState();
  const [data, setData] = useState([]);

  const handleOnChange = (e) => {
    setFile(e.target.files[0]);
  };

  // This function is called when the user clicks the "Import CSV" button.
  const handleOnSubmit = async (e) => {
    e.preventDefault();

    if (file) {
      const formData = new FormData();
      formData.append("file", file);

      // Send the CSV file data to the backend API. The API will parse the CSV file and import the data into the database.
      const response = await fetch("http://localhost:8000/", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        console.log("CSV data has been uploaded successfully");
      } else {
        console.error("Error importing CSV data");
      }
    }
  };

  // This function is called when the user clicks the "Get Data" button.
  const handleGetData = async () => {
    try {
      const response = await fetch("http://localhost:8000/get-data");
      if (!response.ok) {
        console.log("!ok");
        throw new Error("Failed to fetch data");
      }
      const jsonData = await response.json();
      console.log("Data fetched from Table successfully")
      setData(jsonData);

    } catch (error) {
      console.error("Error fetching data:", error);
      console.log("Please Upload the data first!");
    }
  };


  return (
    <div style={{ textAlign: "center" }}>
      <h1>Assignment</h1>
      <div>
      <form onSubmit={handleOnSubmit}>
        <input 
          type={"file"}
          id={"csvFileInput"}
          accept={".csv"}
          onChange={handleOnChange}
        />
        <button  class="import bt" type="submit">Import Csv</button>
      </form>
      
      <button class="data bt" onClick={handleGetData}>Get Data</button>
      </div>

     
      <table>
        <thead>
          <tr>
            <th>DateTime</th>
            <th>Close</th>
            <th>High</th>
            <th>Low</th>
            <th>Open</th>
            <th>Volume</th>
            <th>Instrument</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item) => (
            <tr key={item.datetime}>
              <td>{item.datetime}</td>
              <td>{item.close}</td>
              <td>{item.high}</td>
              <td>{item.low}</td>
              <td>{item.open}</td>
              <td>{item.volume}</td>
              <td>{item.instrument}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
