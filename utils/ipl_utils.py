import pandas as pd
import csv

def matchData():
    with open("data/matches.csv", "r") as file:
        lines = file.readlines()
        matches=[line.split(",") for line in lines[1:]]
    return matches    

def matchDataPandas():
    df=pd.read_csv("data/matches.csv")
    return df

def csv_to_dict(filename):
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)  # This will read the CSV as dictionaries
        rows = [row for row in csv_reader]
    return rows

if __name__=="__main__":
    print(matchDataPandas())