import React from "react";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div className="h-full flex items-center flex-col justify-around">
      <div>
        <h1 className="text-white text-4xl font-bold text-center">
          BCA ASSOSCIATION - MMC & MECHI MAVRICKS
        </h1>
        <p className="text-white text-5xl font-bold text-center">Presents</p>
      </div>

      <h2 className="text-6xl text-white font-bold text-center ">
        TREASURE HUNT 2.0
      </h2>
      <Link to="/team">
        <button className=" bg-white text-black hover:bg-gray-200 py-4 px-10 rounded-full text-5xl  font-bold cursor-pointer">
          CHOOSE TEAM
        </button>
      </Link>
    </div>
  );
};

export default Home;
