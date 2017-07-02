import numpy as np
import pandas as pd
import itertools
import xgboost as xgb
import sys


def load_input(seasons, league="E0"):
    inputs = []
    for year in seasons:
        df = pd.read_csv('input/{0}-{1}.csv'.format(league, year))
        df = df[pd.notnull(df.FTR)]
        # df["Season"] = year
        # df["Fixture"] = np.repeat(np.arange(1,39), 10)
        inputs.append(df)

    return pd.concat(inputs, ignore_index=True)


def process(full):
    # FTR dummies
    full["FTR_H"] = full["FTR"] == "H"
    full["FTR_D"] = full["FTR"] == "D"
    full["FTR_A"] = full["FTR"] == "A"
    full["HTR_H"] = full["HTR"] == "H"
    full["HTR_D"] = full["HTR"] == "D"
    full["HTR_A"] = full["HTR"] == "A"

    stats_cols = ["FTHG", "FTAG", "HTHG", "HTAG", "HS", "AS", "HST", "AST", "HC", "AC", "HF",
                  "AF", "HY", "AY", "HR", "AR", "FTR_H", "FTR_D", "FTR_A", "HTR_H", "HTR_D", "HTR_A"]
    target_cols = ["FTR"]
    match_cols = ["HomeTeam", "AwayTeam", "Referee"]
    match_cols = [col for col in match_cols if col in full.columns]

    # Create copy without stats cols
    train = full[match_cols + target_cols].copy()

    # Add team and referee dummies
    train = pd.concat([train, pd.get_dummies(
        train.HomeTeam, prefix="H")], axis=1)
    train = pd.concat([train, pd.get_dummies(
        train.AwayTeam, prefix="A")], axis=1)

    if ("Referee" in train):
        train = pd.concat([train, pd.get_dummies(train.Referee)], axis=1)

    # Amount of matches (H or A) to go back
    history = [1, 2, 3]

    # Create empty (filled with -1) stats aggregate columns
    for team, back, prev_match, stats in itertools.product(["H", "A"], history, ["H", "A"], stats_cols):
        name = "{0}_L{1}{2}_{3}".format(team, back, prev_match, stats)
        train[name] = -1
    for team, back, stats in itertools.product(["H", "A"], history, stats_cols):
        name = "{0}_L{1}X_{2}".format(team, back * 2, stats)
        train[name] = -1

    # Calculate stats aggregates
    for i in range(len(full)):
        prev = full.head(i)

        home_team = full.iloc[i]["HomeTeam"]
        away_team = full.iloc[i]["AwayTeam"]

        for back_match in history:
            last_home_team_home_match = prev[prev["HomeTeam"] == home_team].tail(
                back_match)
            last_home_team_away_match = prev[prev["AwayTeam"] == home_team].tail(
                back_match)
            last_away_team_home_match = prev[prev["HomeTeam"] == away_team].tail(
                back_match)
            last_away_team_away_match = prev[prev["AwayTeam"] == away_team].tail(
                back_match)

            for stats_col in stats_cols:
                train.iloc[i, train.columns.get_loc("H_L{0}H_{1}".format(
                    back_match, stats_col))] = last_home_team_home_match[stats_col].sum()
                train.iloc[i, train.columns.get_loc("H_L{0}A_{1}".format(
                    back_match, stats_col))] = last_home_team_away_match[stats_col].sum()
                train.iloc[i, train.columns.get_loc("A_L{0}H_{1}".format(
                    back_match, stats_col))] = last_away_team_home_match[stats_col].sum()
                train.iloc[i, train.columns.get_loc("A_L{0}A_{1}".format(
                    back_match, stats_col))] = last_away_team_away_match[stats_col].sum()
                train.iloc[i, train.columns.get_loc("H_L{0}X_{1}".format(back_match * 2, stats_col))] = train.iloc[i]["H_L{0}H_{1}".format(
                    back_match, stats_col)] + train.iloc[i]["H_L{0}A_{1}".format(back_match, stats_col)]
                train.iloc[i, train.columns.get_loc("A_L{0}X_{1}".format(back_match * 2, stats_col))] = train.iloc[i]["A_L{0}H_{1}".format(
                    back_match, stats_col)] + train.iloc[i]["A_L{0}A_{1}".format(back_match, stats_col)]
    return train


def get_teams(df):
    return df.HomeTeam.unique()

# league = "E0"
league = sys.argv[1]


input = load_input(["2016", "2017"], league=league)
# input = load_input(["2017"], league=league)
input = input[pd.notnull(input.FTR)]

teams = get_teams(input)
extra_rows = [{"HomeTeam": team, "AwayTeam": team} for team in teams]
input = input.append(extra_rows, ignore_index=True)

data = process(input)

teams_stats = data.tail(len(teams)).drop("FTR", axis=1)
teams_stats.to_json("output/{0}-stats.json".format(league), orient="records")
pd.Series(teams).to_json(
    "output/{0}-teams.json".format(league), orient="records")

data = data.head(len(data) - len(teams))

X = data.drop(["FTR", "HomeTeam", "AwayTeam", "Referee", "Date"],
              axis=1, errors="ignore")
y = data.FTR


model = xgb.XGBClassifier(n_estimators=80, max_depth=6,
                          learning_rate=0.1, random_state=100)
model.fit(X, y)

from sklearn.externals import joblib
joblib.dump(model, 'output/{0}-model.pkl'.format(league))
