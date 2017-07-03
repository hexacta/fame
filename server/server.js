const express = require("express");
const app = express();

function getMatchStats(leagueId, homeTeam, awayTeam) {
  const stats = require(`./data/${leagueId}-stats.json`);
  const homeStats = stats.find(row => row["HomeTeam"] === homeTeam);
  const awayStats = stats.find(row => row["AwayTeam"] === awayTeam);

  const matchStats = {};
  Object.keys(homeStats).forEach(key => {
    matchStats[key] = key.startsWith("A_") ? awayStats[key] : homeStats[key];
  });
  delete matchStats["HomeTeam"];
  delete matchStats["AwayTeam"];
  delete matchStats["Referee"];

  return matchStats;
}

app.get("/api/:league/match", (req, res) => {
  const leagueId = req.params.league;
  const { home, away } = req.query;

  const matchStats = getMatchStats(leagueId, home, away);

  res.send({ home: 0.5, draw: 0.2, away: 0.3 });
});

app.listen(3000);
