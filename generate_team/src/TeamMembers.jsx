import React, { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion"; // Import framer-motion

const students = [
  { name: "Aaditya Rajbanshi", photo: "1.jpg" },
  { name: "Aashish Hasda", photo: "2.jpg" },
  { name: "Alisha Dawadi", photo: "3.jpg" },
  { name: "Anish Shrestha", photo: "4.jpg" },
  { name: "Ankita Baral", photo: "5.jpg" },
  { name: "Anu Rajbanshi", photo: "6.jpg" },
  { name: "Arjun Dhungel", photo: "7.jpg" },
  { name: "Ashim Lamsal", photo: "8.jpg" },
  { name: "Asmin Acharya", photo: "9.jpg" },
  { name: "Av Rajbanshi", photo: "10.jpg" },
  { name: "Avinash Shah", photo: "11.jpg" },
  { name: "Aviyan Budhathoki", photo: "12.jpg" },
  { name: "Basanta Adhikari", photo: "13.jpg" },
  { name: "BIMAL GHORSAI", photo: "14.jpg" },
  { name: "BINAYAK KATTEL", photo: "15.jpg" },
  { name: "Bishop Poudel", photo: "16.jpg" },
  { name: "Deepika Acharya", photo: "17.jpg" },
  { name: "Devendra Raj Gautam", photo: "18.jpg" },
  { name: "Dipesh Timsina", photo: "19.jpg" },
  { name: "Dipswari Acharya", photo: "20.jpg" },
  { name: "Gayatra Baskota", photo: "21.jpg" },
  { name: "Joshna Khadka", photo: "22.jpg" },
  { name: "Kailash Prasai", photo: "23.jpg" },
  { name: "Karan Rajbanshi", photo: "24.jpg" },
  { name: "Karuna Kumari Rajbanshi", photo: "25.jpg" },
  { name: "Madhav Bhattarai", photo: "26.jpg" },
  { name: "Manish Ghimire", photo: "27.jpg" },
  { name: "Neharika Neupane", photo: "28.jpg" },
  { name: "Nemika Thapa", photo: "29.jpg" },
  { name: "Nimisha Rimal", photo: "30.jpg" },
  { name: "Nirdesh Chauhan", photo: "31.jpg" },
  { name: "Nirjala Gahatraj", photo: "32.jpg" },
  { name: "Nishal Niraula", photo: "33.jpg" },
  { name: "Nishma Khatiwada", photo: "34.jpg" },
  { name: "Noel Pradhan", photo: "35.jpg" },
  { name: "Oseen Niroula", photo: "36.jpg" },
  { name: "Pragyan Gautam", photo: "38.jpg" },
  { name: "Prajit Bhattarai", photo: "39.jpg" },
  { name: "Prakhyati Budhathoki", photo: "40.jpg" },
  { name: "Prakriti Paudel", photo: "41.jpg" },
  { name: "Pranisha Shrestha", photo: "42.jpg" },
  { name: "Pranjal Khanal", photo: "43.jpg" },
  { name: "Raju Neupane Khatri", photo: "45.jpg" },
  { name: "Raymon Chapagai", photo: "46.jpg" },
  { name: "Rikesh Giri", photo: "47.jpg" },
  { name: "Roshan Newar", photo: "49.jpg" },
  { name: "SADHANA DAHAL", photo: "50.jpg" },
  { name: "Sagona Gautam", photo: "51.jpg" },
  { name: "Sajina Banjara", photo: "52.jpg" },
  { name: "Samarpan Rai", photo: "53.jpg" },
  { name: "Sanju Shah", photo: "54.jpg" },
  { name: "Sarika Khatiwada", photo: "55.jpg" },
  { name: "Sarika Rai", photo: "56.jpg" },
  { name: "Saujan Khanal", photo: "57.jpg" },
  { name: "Saurav Mishra", photo: "58.jpg" },
  { name: "SONY SARU", photo: "59.jpg" },
  { name: "Sulabh Dahal", photo: "61.jpg" },
  { name: "Susmita Bista", photo: "62.jpg" },
  { name: "Suvam Bista", photo: "63.jpg" },
  { name: "Tekendra Rai", photo: "64.jpg" },
  { name: "Urmila Acharya", photo: "65.jpg" },
  { name: "Yuddha Bikram Sapkota", photo: "66.jpg" },
  { name: "Aditya Dhungana", photo: "68.jpg" },
  { name: "Rohan Shah", photo: "69.jpg" },
  { name: "Kabin Bhetwal", photo: "70.jpg" },
];

function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}

function generateTeams(students, teamSize) {
  const shuffledStudents = shuffleArray([...students]);
  const teams = [];
  for (let i = 0; i < shuffledStudents.length; i += teamSize) {
    teams.push(shuffledStudents.slice(i, i + teamSize));
  }
  return teams;
}

const TeamMembers = () => {
  const [teams, setTeams] = useState([]);
  const [currentTeamIndex, setCurrentTeamIndex] = useState(0);
  const [allTeamsViewed, setAllTeamsViewed] = useState(false);
  const [direction, setDirection] = useState("next"); // Track animation direction

  useEffect(() => {
    const generatedTeams = generateTeams(students, 5);
    setTeams(generatedTeams);
  }, []);

  const handleNext = () => {
    setDirection("next");
    if (currentTeamIndex < teams.length - 1) {
      setCurrentTeamIndex(currentTeamIndex + 1);
    } else {
      setAllTeamsViewed(true);
    }
  };

  const handleBack = () => {
    setDirection("previous");
    if (currentTeamIndex > 0) {
      setCurrentTeamIndex(currentTeamIndex - 1);
    }
  };

  const handleSelectTeam = (index) => {
    setCurrentTeamIndex(index);
    setAllTeamsViewed(false);
  };

  const handleShowMenu = () => {
    setAllTeamsViewed(true);
  };

  const currentTeam = teams[currentTeamIndex] || [];

  return (
    <div className="h-full py-4 px-12">
      {allTeamsViewed ? (
        <div className="">
          <h2 className="text-5xl text-center text-white font-bold">
            Select a Team
          </h2>
          <div className="grid grid-cols-3 gap-5 mt-10 h-full">
            {teams.map((team, index) => (
              <button
                key={index}
                onClick={() => handleSelectTeam(index)}
                className="bg-white text-black text-3xl hover:bg-gray-200 py-2 px-3 rounded-full font-bold cursor-pointer"
              >
                Team {index + 1}
              </button>
            ))}
          </div>
        </div>
      ) : (
        <>
          <div className="flex justify-between">
            <button className="bg-white text-black py-2 px-4 rounded-full text-5xl font-bold">
              Team {currentTeamIndex + 1}
            </button>
            <button
              onClick={handleShowMenu}
              className="bg-white text-black hover:bg-gray-200 rounded-full py-2 px-4 text-2xl font-bold cursor-pointer"
            >
              All teams
            </button>
          </div>

          <div className="mt-10">
            <AnimatePresence mode="wait">
              <motion.div
                key={currentTeamIndex}
                initial={{ x: direction === "next" ? 100 : -100, opacity: 0 }}
                animate={{ x: 0, opacity: 1 }}
                exit={{ x: direction === "next" ? -100 : 100, opacity: 0 }}
                transition={{ duration: 0.3 }}
                className="flex justify-between"
              >
                {/* Image container */}
                <div className="flex w-[60%] flex-wrap justify-center gap-5 bg-black/50 backdrop-blur-sm px-4 py-4 rounded-3xl">
                  {currentTeam.map((member, index) => (
                    <motion.div
                      key={index}
                      initial={{ scale: 0.8, opacity: 0 }}
                      animate={{ scale: 1, opacity: 1 }}
                      transition={{ delay: index * 0.1 }}
                      className="flex justify-center"
                    >
                      <img
                        src={`/${member.photo}`}
                        alt={`Profile ${index + 1}`}
                        className="rounded-full border-2 border-primary w-40 h-40 object-cover"
                      />
                    </motion.div>
                  ))}
                </div>

                {/* Team names */}
                <div className="w-[30%]">
                  <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="bg-black/50 backdrop-blur-sm rounded-3xl px-4 py-4"
                  >
                    <h2 className="text-2xl text-white font-bold">
                      Team members
                    </h2>
                    <ol className="mt-5 list-decimal list-inside text-white font-bold text-xl">
                      {currentTeam.map((member, index) => (
                        <motion.li
                          key={index}
                          initial={{ opacity: 0, x: 20 }}
                          animate={{ opacity: 1, x: 0 }}
                          transition={{ delay: index * 0.1 }}
                          className="mb-2"
                        >
                          {member.name}
                        </motion.li>
                      ))}
                    </ol>
                  </motion.div>
                  <div className="flex mt-6 justify-around">
                    {currentTeamIndex > 0 && (
                      <button
                        onClick={handleBack}
                        className="bg-white text-black hover:bg-gray-200 py-1 px-3 rounded-full text-2xl font-bold cursor-pointer"
                      >
                        PREVIOUS
                      </button>
                    )}
                    <button
                      onClick={handleNext}
                      className="bg-white text-black hover:bg-gray-200 py-1 px-3 rounded-full text-2xl font-bold cursor-pointer"
                    >
                      NEXT
                    </button>
                  </div>
                </div>
              </motion.div>
            </AnimatePresence>
          </div>
        </>
      )}
    </div>
  );
};

export default TeamMembers;
