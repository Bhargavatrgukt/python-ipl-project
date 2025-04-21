import pandas as pd



# def countMatchesPerSeason(matches):
#     seasons = defaultdict(int)
#     for match in matches:
#         season = match['season'] 
#         seasons[season] += 1
#     return dict(sorted(seasons.items(), key=lambda x: int(x[0])))

def main():
    match_data = pd.read_csv("data/matches.csv")
    output=match_data.groupby('season').size()
    print(output)
    try:
        with open("output/1.matches_per_season.txt", "w") as file:
            for season, count in output.items():
                file.write(f"{season}: {count}\n")
    except Exception as e:
        print(f"Error writing to file: {e}")
        return
    print("Output written to output/1.matches_per_season.txt")   
    return         

if __name__ == "__main__":
    main()
