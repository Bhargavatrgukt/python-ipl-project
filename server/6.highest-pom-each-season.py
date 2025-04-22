import pandas as pd
        
    
def main():
    matches=pd.read_csv("data/matches.csv")
    data=matches.groupby(by=["season","player_of_match"]).size().groupby(by="season").idxmax().apply(lambda x:x[1])
    print(data)

    with open("output/6.most_mom_per_season.txt", "w") as f:
        f.write("Top Player of the Match per Season:\n\n")
        f.write(data.to_string())
    

if __name__=="__main__":    
    main()