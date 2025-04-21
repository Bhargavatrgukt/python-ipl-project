import pandas as pd 

def main():
    deliveries_data=pd.read_csv("data/deliveries.csv")
    res=deliveries_data[deliveries_data["is_super_over"]==1].groupby(by="bowler").agg( total_runs_conceded=("total_runs", "sum"),
    balls_bowled=("ball", "count"))
    res["economy"]=round(res["total_runs_conceded"]/(res["balls_bowled"]/6),2)
    print(res.sort_values(by="economy",ascending=True))
    
if __name__=="__main__":
    main()

