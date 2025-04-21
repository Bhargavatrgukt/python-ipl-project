import pandas as pd

def main():
    matches_data=pd.read_csv("data/matches.csv")
    data=matches_data[matches_data["winner"]==matches_data["toss_winner"]].groupby(by="winner").agg('size')
    print(data)


if __name__=="__main__":    
    main()