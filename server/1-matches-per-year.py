import csv
from collections import defaultdict

def csv_to_dict(filename):
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        rows = [row for row in csv_reader]
    return rows

def countMatchesPerSeason(matches):
    seasons = defaultdict(int)
    for match in matches:
        season = match['season'] 
        seasons[season] += 1
    return dict(sorted(seasons.items(), key=lambda x: int(x[0])))

def main():
    matches = csv_to_dict("data/matches.csv")
    output = countMatchesPerSeason(matches)
    with open("output/1.matches_per_season.txt", "w") as file:
        for season, count in output.items():
            file.write(f"{season}: {count}\n")

if __name__ == "__main__":
    main()
