import pandas as pd 

def main():
    deliveries_data=pd.read_csv("data/deliveries.csv")
    res=deliveries_data[deliveries_data["is_super_over"]==1].groupby(by="bowler").agg( total_runs_conceded=("total_runs", "sum"),
    balls_bowled=("ball", "count"))
    res["economy"]=round(res["total_runs_conceded"]/(res["balls_bowled"]/6),2)
    sorted_res=res.sort_values(by="economy",ascending=True)
    print(sorted_res)
    with open("output/9.lowest_economy_bowler_in_super_over.txt", "w") as f:
        f.write("Bowler Economy Rates in Super Overs:\n\n")
        f.write(sorted_res.to_string(index=False))
if __name__=="__main__":
    main()

