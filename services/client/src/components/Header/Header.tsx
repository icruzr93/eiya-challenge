import React from "react";
import Search from "../Search/Search";
import "./Header.css";

interface HeaderProps {
  fetchData: () => void;
}

const Header = ({ fetchData }: HeaderProps) => (
  <div className="Header">
    <Search fetchData={fetchData} />
  </div>
);

export default Header;
