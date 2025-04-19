import csv

def csv_to_dict(filename):
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
         # This will read the CSV as dictionaries
        rows = [row for row in csv_reader]
    return rows

def count_extra_runs_per_team_in_year_2016(matches):
    team_and_their_extra_runs = {}
    for match in  matches:
        if match["bowling_team"] not in team_and_their_extra_runs:
            team_and_their_extra_runs[match["bowling_team"]]=int(match["extra_runs"])
        else:    
            team_and_their_extra_runs[match["bowling_team"]]+=int(match["extra_runs"])
    return team_and_their_extra_runs        


def get_match_ids_for_season(matches, season):
    return {match['id'] for match in matches if match['season'] == season}

def  get_deliveries_for_match_ids(deliveries, match_ids):
    return [delivery for delivery in deliveries if delivery['match_id'] in match_ids]


def main():
    deliveries_filename= 'data/deliveries.csv'  
    match_filename  = 'data/matches.csv'
    matches = csv_to_dict(match_filename)
    deliveries = csv_to_dict(deliveries_filename)
    matches_played_in_2016 = get_match_ids_for_season(matches, '2016')
    filtered_deliveries = get_deliveries_for_match_ids(deliveries, matches_played_in_2016)
    output=count_extra_runs_per_team_in_year_2016(filtered_deliveries)
    
    try:
        with open("output/3.extra_runs_per_team_in_2016.txt", "w") as file:
            for team, extra_runs in output.items():
                file.write(f"{team}:{extra_runs}\n")
    except Exception as e:
        print(f"Error writing to file: {e}")
        return
    print("Output written to output/3.extra_runs_per_team_in_2016.txt")
        



if __name__=="__main__":
    main()