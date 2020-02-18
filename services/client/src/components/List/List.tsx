import React, { useEffect } from "react";
import moment from "moment";

import Record from "../../types/Record.d";
import Loading from "../Loading/Loading";
import "./List.css";

interface ListProps {
  fetchData: () => void;
  loading: boolean;
  isError: boolean;
  records: Record[];
}

const List = ({ fetchData, loading, isError, records }: ListProps) => {
  useEffect(() => {
    fetchData();
    const timer = setInterval(() => fetchData(), 10000);
    return () => clearTimeout(timer);
  }, []);

  if (loading)
    return (
      <div className="loading-container">
        <Loading />
      </div>
    );

  if (isError) return <div className="error">Something went wrong ...</div>;

  return (
    <div>
      <div className="Table-container">
        <table className="Table">
          <thead className="Table-head">
            <tr>
              <th>Number</th>
              <th>Created At</th>
              <th>Result</th>
              <th>State</th>
              <th>Analyzed At</th>
            </tr>
          </thead>
          <tbody className="Table-body">
            {records.map((record: Record) => (
              <tr key={record.id}>
                <td>
                  <span className="Table-number">{record.number}</span>
                </td>
                <td>{moment(record.created_at).format("YYYY-MM-DD HH:SS")}</td>
                <td>
                  {record.result ? (
                    <span className="ready">{record.result}</span>
                  ) : (
                    <span className="not-ready">NOT READY </span>
                  )}
                </td>
                <td>
                  {record.state === "PENDING" ? (
                    <span className="not-ready">{record.state}</span>
                  ) : (
                    <span className="ready">{record.state}</span>
                  )}
                </td>
                <td>
                  {record.analyzed_at ? (
                    <span className="ready">
                      {moment(record.analyzed_at).format("YYYY-MM-DD HH:SS")}
                    </span>
                  ) : (
                    <span className="not-ready">NOT READY </span>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default List;
