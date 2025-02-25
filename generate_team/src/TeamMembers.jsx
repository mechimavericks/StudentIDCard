import React, { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion"; // Import framer-motion
import students from "./students";

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
                      transition={{ delay: index * 0.3, duration: 0.5 }} // 0.3-second delay for each photo
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
                          transition={{ delay: index * 0.3, duration: 0.5 }} // 0.3-second delay for each name
                          className="mb-2"
                        >
                          {member.name} - {member.photo.split(".")[0]}
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
