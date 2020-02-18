import React from "react";
import "./Loading.css";

interface LoadingProps {
  width: string;
  height: string;
}

const Loading = (props: LoadingProps) => {
  const { width, height } = props;
  return <div className="Loading" style={{ width, height }} />;
};

Loading.defaultProps = {
  width: "28px",
  height: "28px"
};

export default Loading;
