const express = require("express");
const axios = require("axios");
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
  const modelUrl = `${leagueId.toLowerCase()}model:${process.env.MODELPORT}`;

  axios
    .post(`http://${modelUrl}/predictproba`, matchStats)
    .then(response => {
      console.log(response.data);
      const { H, D, A } = response.data[0];
      res.send({ home: H, draw: D, away: A });
    })
    .catch(error => {
      console.log(error.response.data);
      res.status(500).send({ error: error.response.data });
    });
});

app.listen(process.env.PORT || 3000);
