import pandas as pd 


def main():
    match_data=pd.read_csv("data/matches.csv")
    deliveries_data=pd.read_csv("data/deliveries.csv")
    match_season_df = match_data[['id', 'season']]
    
    merged_df = deliveries_data.merge(match_season_df, how='left', left_on='match_id', right_on='id')
    result=merged_df.groupby(['season', 'batsman']).agg(total_runs=('total_runs', 'sum'), balls_faced=('ball', 'count'))
    result["strike_rate"]=round((result['total_runs']/result["balls_faced"])*100,2) 
    print(result)
    
    with open("output/7.strike_rates_of_batsmen_per_season.txt", "w") as f:
        f.write("Batsman Strike Rates per Season:\n\n")
        f.write(result.to_string())

    
if __name__=="__main__":
    main()