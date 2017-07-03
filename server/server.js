const express = require("express");
const app = express();

app.get("/api/:league/match", (req, res) => {
  res.send({ home: 0.5, draw: 0.2, away: 0.3 });
});

app.listen(3000);
