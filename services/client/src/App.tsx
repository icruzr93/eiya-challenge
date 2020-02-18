import React, { useState } from "react";
import Header from "./components/Header/Header";
import List from "./components/List/List";
import "./App.css";
import Record from "./types/Record";
import axios from "axios";

const API_URL = process.env.REACT_APP_API_URL;

const App = () => {
  const [loading, setLoading] = useState<boolean>(false);
  const [records, setRecords] = useState<Record[]>([]);
  const [isError, setIsError] = useState<boolean>(false);

  const fetchData = async () => {
    setLoading(true);
    try {
      const { data } = await axios(`${API_URL}/records/`);
      setRecords(data);
    } catch (error) {
      setIsError(true);
    }

    setLoading(false);
  };

  return (
    <div>
      <Header fetchData={fetchData} />
      <List
        fetchData={fetchData}
        loading={loading}
        isError={isError}
        records={records}
      />
    </div>
  );
};

export default App;
