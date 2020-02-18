import React, { useState } from "react";
import "./Search.css";
import Loading from "../Loading/Loading";
import axios from "axios";

const API_URL = process.env.REACT_APP_API_URL;

interface SearchProps {
  fetchData: () => void;
}

const Search = ({ fetchData }: SearchProps) => {
  const [query, setQuery] = useState();
  const [loading, setLoading] = useState();

  const handleEnter = async () => {
    if (!query) return "";
    setLoading(true);

    await axios.post(`${API_URL}/records/`, {
      number: query
    });
    setLoading(false);
    fetchData();
  };

  return (
    <div className="Search">
      <span className="Search-icon" />
      <input
        className="Search-input"
        type="number"
        placeholder="Enter a number and click enter"
        onChange={e => setQuery(e.target.value)}
        onKeyDown={e => {
          if (e.key === "Enter") handleEnter();
        }}
        name="query"
        value={query}
      />

      {loading && (
        <div className="Search-loading">
          <Loading width={"12px"} height={"12px"} />
        </div>
      )}
    </div>
  );
};

export default Search;
