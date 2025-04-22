
import pandas as pd

def count_extra_runs_per_team_in_year_2016(deliveries, match_ids):
    result=deliveries[deliveries["match_id"].isin(match_ids)].groupby(["bowling_team"]).agg(total_extra_runs=("extra_runs", "sum"))
    return result
    
    


def get_match_ids_for_season(matches, season):
    match_ids=matches[matches["season"]==2016]["id"].tolist()
    return set(match_ids)



def main():
    matches=pd.read_csv("data/matches.csv")
    deliveries=pd.read_csv("data/deliveries.csv")
    matches_played_in_2016 = get_match_ids_for_season(matches, '2016')
    output=count_extra_runs_per_team_in_year_2016(deliveries, matches_played_in_2016)
    print(output)
    
    with open("output/3.extra_runs_per_team_in_2016.txt", "w") as f:
        f.write("Extra Runs Conceded per Team in 2016:\n")
        for team, runs in output.items():
            f.write(f"{team}: {runs}\n")
        



if __name__=="__main__":
    main()