import pandas as pd 


def main():
    match_data=pd.read_csv("data/matches.csv")
    deliveries_data=pd.read_csv("data/deliveries.csv")
    match_season_df = match_data[['id', 'season']]
    
    merged_df = deliveries_data.merge(match_season_df, how='left', left_on='match_id', right_on='id')
    result=merged_df.groupby(['season', 'batsman']).agg(total_runs=('total_runs', 'sum'), balls_faced=('ball', 'count'))
    result["strike_rate"]=round((result['total_runs']/result["balls_faced"])*100,2) 
    print(result)


    
if __name__=="__main__":
    main()