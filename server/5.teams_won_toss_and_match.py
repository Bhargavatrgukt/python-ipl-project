import csv
from collections import defaultdict

def csv_to_dict(filename):
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
         # This will read the CSV as dictionaries
        rows = [row for row in csv_reader]
    return rows

def count_toss_along_with_match_winning_team(matches):
    team=defaultdict(int)
    for match in matches:
        if match["toss_winner"]==match["winner"]:
            team[match["toss_winner"]] += 1
    return dict(sorted(team.items(), key=lambda x: x[1], reverse=True))

def main():
    match_filename  = 'data/matches.csv'
    matches = csv_to_dict(match_filename)
    teams=count_toss_along_with_match_winning_team(matches)

    
    try:
        with open("output/5.teams_won_both_toss_and_match.txt", "w") as file:
            for team, count in teams.items():
                file.write(f"{team}:{count}\n")
        print("output/5.teams_won_both_toss_and_match.txt")
    except Exception as e:
        print(f"Error writing to file: {e}")
        return


if __name__=="__main__":    
    main()