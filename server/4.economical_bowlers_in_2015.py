import pandas as pd



def main():
    deliveries=pd.read_csv("data/deliveries.csv")
    matches=pd.read_csv("data/matches.csv")
    matches_played_in_2015 = set(matches[matches["season"]==2015]["id"].tolist())
    economical_bowlers=deliveries[deliveries["match_id"].isin(matches_played_in_2015)].groupby(["bowler"]).agg(total_runs=("total_runs", "sum"), balls_faced=("ball", "count"))
    economical_bowlers["economy_rate"]=round(economical_bowlers["total_runs"]/economical_bowlers["balls_faced"]*6,2)
    result=economical_bowlers.sort_values(by="economy_rate",ascending=True)
    print(result)

if __name__=="__main__":    
    main()