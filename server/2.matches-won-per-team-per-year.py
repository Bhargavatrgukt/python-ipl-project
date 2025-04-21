import csv
from collections import defaultdict

def csv_to_dict(filename):
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        return [row for row in csv_reader]

def countMatchesWonPerTeamPerYear(matches):
    winsPerTeamPerYear = defaultdict(lambda: defaultdict(int))
    for match in matches:
        season = match['season']
        winner = match['winner']
        if winner:
            winsPerTeamPerYear[season][winner] += 1
    return winsPerTeamPerYear

def main():
    matches = csv_to_dict("data/matches.csv")
    output = countMatchesWonPerTeamPerYear(matches)

    try:
        with open("output/2.matches_won_per_team_per_year.txt", "w") as file:
            for season, teams in sorted(output.items(), key=lambda x: int(x[0])):
                file.write(f"{season}:\n")
                for team, count in sorted(teams.items()):
                    file.write(f"  {team}: {count}\n")
                file.write("\n")
    except Exception as e:
        print(f"Error writing to file: {e}")
        return

    print("Output written to output/2.matches_won_per_team_per_year.txt")

if __name__ == "__main__":
    main()
