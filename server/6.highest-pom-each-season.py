import pandas as pd
        
    
def main():
    matches=pd.read_csv("data/matches.csv")
    data=matches.groupby(by=["season","player_of_match"]).size().groupby(by="season").idxmax().apply(lambda x:x[1])
    print(data)

if __name__=="__main__":    
    main()