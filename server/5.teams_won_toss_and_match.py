import pandas as pd

def main():
    matches_data=pd.read_csv("data/matches.csv")
    data=matches_data[matches_data["winner"]==matches_data["toss_winner"]].groupby(by="winner").agg('size')
    print(data)
    with open("output/5.teams_won_both_toss_and_match.txt", "w") as f:
        f.write("Matches Won by Teams Who Also Won the Toss:\n\n")
        f.write(data.to_string())


if __name__=="__main__":    
    main()