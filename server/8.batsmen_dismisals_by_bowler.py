import pandas as pd 

def main():
    deliveries_data=pd.read_csv("data/deliveries.csv")
    res=deliveries_data[(deliveries_data["dismissal_kind"]=="bowled") | (deliveries_data["dismissal_kind"]=="caught")].groupby(by=["bowler","batsman"]).size().reset_index(name="dismissal_count")
    print(res)

    with open("output/8.batsman_bowler_dismissals.txt", "w") as f:
        f.write("Dismissals (Bowled or Caught) per Bowler-Batsman Pair:\n\n")
        f.write(res.to_string(index=False))
if __name__=="__main__":
    main()

