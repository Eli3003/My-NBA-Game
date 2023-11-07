import pandas as pd
import re
from io import StringIO
def analyse_nba_game(play_by_play_moves):
    df = pd.read_csv(play_by_play_moves, header = None, sep = '|')
    
    df.columns = ["PERIOD", "REMAINING_SEC", "RELEVANT_TEAM", "AWAY_TEAM", "HOME_TEAM", "AWAY_SCORE", "HOME_SCORE", "DESCRIPTION"]
    return df
analyse = analyse_nba_game("https://storage.googleapis.com/qwasar-public/nba_game_warriors_thunder_20181016.txt")
def DESCRIPTION(analyse):
    all_information_about_names = []
    for i in analyse.get("DESCRIPTION").values:
        pattern = re.compile(r"(\w\. \w+)", re.I)
        some = pattern.search(i)
        if some != None:
            all_information_about_names.append(some.group(0))
    return all_information_about_names
find_desc = DESCRIPTION(analyse)
def find_team(find_desc, analyse):
    nba_game = []
    pt3_make = re.compile(r"(\w\. \w+) (makes 3-pt)", re.I)
    pt3_miss = re.compile(r"(\w\. \w+) (misses 3-pt)", re.I)
    pt2_make = re.compile(r"(\w\. \w+) (makes 2-pt)", re.I)
    pt2_miss = re.compile(r"(\w\. \w+) (misses 2-pt)", re.I)
    FTA = re.compile(r"(\w\. \w+) misses free throw", re.I)
    offensive = re.compile(r"Offensive rebound by (\w\. \w+)", re.I)
    foul_by = re.compile(r"foul by (\w\. \w+)", re.I)
    FT = re.compile(r"(\w\. \w+) makes free throw", re.I)
    FT2 = re.compile(r"(\w\. \w+) makes clear path free throw", re.I)
    DRB = re.compile(r"Defensive rebound by (\w\. \w+)", re.I)
    AST = re.compile(r"assist by (\w\. \w+)", re.I)
    STL = re.compile(r"steal by (\w\. \w+)", re.I)
    BLC = re.compile(r"block by (\w\. \w+)", re.I)
    TOV = re.compile(r"Turnover by (\w\. \w+)", re.I)

    for all in list(set(find_desc)):
        play_by_play = {"player_name": '', "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}
        play_by_play["player_name"] = all
        pt2 = 0
        for j in analyse["DESCRIPTION"].values:
            pt3_makes = pt3_make.search(j)
            if pt3_makes != None:
                if pt3_makes.group(1) == all:
                    play_by_play["3P"] += 1
                    play_by_play["3PA"] += 1
                    play_by_play["FG"] += 1
                    play_by_play["FGA"] += 1
            pt3_misses = pt3_miss.search(j)
            if pt3_misses != None:
                if pt3_misses.group(1) == all:
                    play_by_play["3PA"] += 1
                    play_by_play["FGA"] += 1
            pt2_makes = pt2_make.search(j)
            if pt2_makes != None:
                if pt2_makes.group(1) == all:
                    play_by_play["FG"] += 1
                    play_by_play["FGA"] += 1
                    pt2+=1
            pt2_misses = pt2_miss.search(j)
            if pt2_misses != None:
                if pt2_misses.group(1) == all:
                    play_by_play["FGA"] += 1
            FTA_pat = FTA.search(j)
            if FTA_pat != None:
                if FTA_pat.group(1) == all:
                    play_by_play["FTA"] += 1
            FT_pat = FT.search(j)
            if FT_pat != None:
                if FT_pat.group(1) == all:
                    play_by_play["FT"] += 1
                    play_by_play["FTA"] += 1
            FT2_pat = FT2.search(j)
            if FT2_pat != None:
                if FT2_pat.group(1) == all:
                    play_by_play["FT"] += 1
                    play_by_play["FTA"] += 1
            obr = offensive.search(j)
            if obr != None:
                if obr.group(1) == all:
                    play_by_play["ORB"] += 1
            fb = foul_by.search(j)
            if fb != None:
                if fb.group(1) == all:
                    play_by_play["PF"] += 1
            drb = DRB.search(j)
            if drb != None:
                if drb.group(1) == all:
                    play_by_play["DRB"] += 1
            ast = AST.search(j)
            if ast != None:
                if ast.group(1) == all:
                    play_by_play["AST"] += 1
            stl = STL.search(j)
            if stl != None:
                if stl.group(1) == all:
                    play_by_play["STL"] += 1
            blc = BLC.search(j)
            if blc != None:
                if blc.group(1) == all:
                    play_by_play["BLK"] += 1
            tov = TOV.search(j)
            if tov != None:
                if tov.group(1) == all:
                    play_by_play["TOV"] += 1

        if play_by_play["3PA"] != 0:
            play_by_play["3P%"] = round(play_by_play["3P"]/play_by_play["3PA"], 3)
        else:
            play_by_play['3P%'] = 0
        if play_by_play["FTA"] != 0:
            play_by_play["FT%"] = round(play_by_play["FT"]/play_by_play["FTA"], 3)
        else:
            play_by_play['FT%'] = 0
        if play_by_play["FGA"] != 0:
            play_by_play["FG%"] = round(play_by_play["FG"]/play_by_play["FGA"], 3)
        else:
            play_by_play['FG%'] = 0
        play_by_play["TRB"] = play_by_play["ORB"] + play_by_play["DRB"]
        play_by_play['PTS'] = (2 * pt2) + (3 * play_by_play['3P']) + play_by_play['FT']
        
        nba_game.append(play_by_play)
    home_team = []
    away_team = []
    for name in list(set(find_desc)):
        names = {name:0, "Team":""}
        names1 = {name:0, "Team1":""}
        thom = re.compile(f"{name}", re.I)
        for a in range(len(analyse["DESCRIPTION"])):
            thom1 = thom.search(analyse["DESCRIPTION"][a])
            if thom1 != None:
                if analyse.iloc[a].values[2] == "GOLDEN_STATE_WARRIORS":
                    names[name] += 1
                    names['Team'] = "GOLDEN_STATE_WARRIORS"
                elif analyse.iloc[a].values[2] == "OKLAHOMA_CITY_THUNDER":
                    names1[name] += 1
                    names1['Team1'] = "OKLAHOMA_CITY_THUNDER"
        num = max(names[name], names1[name])  
        if names[name] == num:
            home_team.append(name)
        elif names1[name] == num:
            away_team.append(name)
    All_home_team = [i for i in nba_game for j in home_team if i["player_name"] == j]
    All_away_team = [i for i in nba_game for j in away_team if i["player_name"] == j]
    
    for all_score in [All_home_team, All_away_team]:
        df = pd.DataFrame(all_score)
        columns = df.columns.values[1:]
        total = []
        for i in columns:
            total.append(round(df[i].sum(), 2))
        print(df.to_string(index = False))
        some = []
        for t in total:
            some.append(str(t))
        print("    Team Total  ", '   '.join(some), "\n")
find_team(find_desc, analyse)