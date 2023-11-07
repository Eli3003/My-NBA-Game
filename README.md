# Welcome to My Nba Game Analysis
***

## Task
TODO - What is the problem? And where is the challenge?

## Description
We have caught all the play_by_play happening during a NBA game so we have a flow of data and we want to create a nice array of hash which will sum everything.

Part I
Create a function analyse_nba_game(play_by_play_moves) which receives an array of play and will return a dictionary summary of the game.

Each play follow this format:

PERIOD|REMAINING_SEC|RELEVANT_TEAM|AWAY_TEAM|HOME_TEAM|AWAY_SCORE|HOME_SCORE|DESCRIPTION
They are ordered by time.

The return dictionary (hash) will have this format:

{"home_team": {"name": TEAM_NAME, "players_data": DATA}, "away_team": {"name": TEAM_NAME, "players_data": DATA}}
DATA will be an array of hashes with this format:
{"player_name": XXX, "FG": XXX, "FGA": XXX, "FG%": XXX, "3P": XXX, "3PA": XXX, "3P%": XXX, "FT": XXX, "FTA": XXX, "FT%": XXX, "ORB": XXX, "DRB": XXX, "TRB": XXX, "AST": XXX, "STL": XXX, "BLK": XXX, "TOV": XXX, "PF": XXX, "PTS": XXX}
Percent are on 100.
Player is a string everything else are integers.

Part II
Create a print_nba_game_stats(team_dict) function which will a dictionary with name and players_data will print it with the following format (each column is separated by a tabulation (' ')):

HEADER
FOR PLAYER IN PLAYERS
PLAYER
TOTAL

## Installation
wget https://storage.googleapis.com/qwasar-public/nba_game_warriors_thunder_20181016.txt
wget https://storage.googleapis.com/qwasar-public/nba_game_blazers_lakers_20181018.txt

## Usage
python 	my_nba_game_analysis.py
```
  player_name  FG  FGA    FG%  3P  3PA    3P%  FT  FTA  FT%  ORB  DRB  TRB  AST  STL  BLK  TOV  PF  PTS
     K. Looney   5   11  0.455   0    0  0.000   0    0  0.0    8    2   10    2    1    2    1   4   10
    J. Jerebko   0    0  0.000   0    0  0.000   0    0  0.0    0    3    3    0    0    0    1   2    0
   K. Thompson   5   20  0.250   1    8  0.125   3    3  1.0    1    3    4    0    0    0    2   3   14
   A. McKinnie   0    1  0.000   0    1  0.000   0    0  0.0    0    0    0    0    0    0    0   0    0
 S. Livingston   3    5  0.600   0    0  0.000   0    0  0.0    2    1    3    1    1    0    1   2    6
      D. Jones   6    7  0.857   0    0  0.000   0    0  0.0    2    1    3    2    0    3    2   4   12
       J. Bell   0    0  0.000   0    0  0.000   0    0  0.0    1    1    2    0    0    1    0   1    0
   A. Iguodala   1    2  0.500   0    1  0.000   0    0  0.0    0    2    2    2    0    0    0   0    2
       Q. Cook   1    2  0.500   1    1  1.000   0    0  0.0    1    1    2    1    0    0    2   2    3
      S. Curry  11   20  0.550   5    9  0.556   5    5  1.0    0    8    8    9    1    0    3   4   32
      D. Green   1    6  0.167   0    1  0.000   0    0  0.0    1   12   13    5    3    0    6   3    2
     K. Durant   9   21  0.429   0    5  0.000   9   10  0.9    1    7    8    6    1    1    3   4   27
    Team Total   42   95   4.31   7   26   1.68   17   18   2.9   17   41   58   28   7   7   21   29   108 

  player_name  FG  FGA    FG%  3P  3PA    3P%  FT  FTA    FT%  ORB  DRB  TRB  AST  STL  BLK  TOV  PF  PTS
    R. Felton   1    5  0.200   0    3  0.000   4    5  0.800    0    3    3    1    0    0    2   0    6
 P. Patterson   2    9  0.222   1    4  0.250   2    3  0.667    3    2    5    0    1    1    1   0    7
  T. Ferguson   0    2  0.000   0    2  0.000   0    0  0.000    2    2    4    1    0    0    1   3    0
     J. Grant   2    7  0.286   1    4  0.250   2    4  0.500    2    0    2    2    0    3    0   1    7
    P. George   9   23  0.391   4   12  0.333   5    8  0.625    0    2    2    5    4    0    5   3   27
      N. Noel   1    2  0.500   0    0  0.000   1    2  0.500    3    4    7    1    1    1    0   3    3
   Á. Abrines   3    8  0.375   2    6  0.333   0    0  0.000    0    2    2    0    0    0    0   2    8
     S. Adams   6   12  0.500   0    0  0.000   5    8  0.625    4    7   11    4    2    0    2   3   17
    H. Diallo   2    4  0.500   0    0  0.000   0    1  0.000    0    1    1    1    1    0    0   2    4
  D. Schröder   7   19  0.368   2    6  0.333   5    6  0.833    2    6    8    6    3    1    3   4   21
    Team Total   33   91   3.34   10   37   1.5   24   37   4.55   16   29   45   21   12   6   14   21   100 
