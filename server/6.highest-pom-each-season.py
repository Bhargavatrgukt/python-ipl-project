import csv

def csv_to_dict(filename):
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        rows = [row for row in csv_reader]
    return rows

def most_mom_for_each_season(matches):
    season_mom = {}
    for match in matches:
        season=match["season"]
        if season  in season_mom:
            season_mom[season].append(match["player_of_match"])
        else:
            season_mom[season] = [match["player_of_match"]]
    return dict(sorted(
    {key: max(value,key=value.count) for key, value in season_mom.items()}.items(),
    key=lambda x: int(x[0])
))
        
    
def main():
    match_filename  = 'data/matches.csv'
    matches = csv_to_dict(match_filename)
    output=most_mom_for_each_season(matches)
    try:
        with open("output/6.most_mom_per_season.txt", "w") as file:
            for season, player in output.items():
                file.write(f"{season}:{player}\n")
        print("output/5.teams_won_both_toss_and_match.txt")
    except Exception as e:
        print(f"Error writing to file: {e}")
        return


if __name__=="__main__":    
    main()