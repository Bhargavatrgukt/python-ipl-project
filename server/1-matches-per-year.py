from collections import defaultdict
import sys
import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from utils.ipl_utils import matchData


def countMatchesPerSeasonApproach2(matches):
    seasons=defaultdict(int)
    for match in matches:
        season=match[1]
        seasons[season]+=1
    return dict(sorted(seasons.items(),key=lambda x: int(x[0])))
# this is one appraoch
def countMatchesPerSeason(matches):
    seasons = {}
    for match in matches:
        season = match[1]
        if season not in seasons:
            seasons[season] = 0
        seasons[season] += 1
    return seasons


def main():
    with open("data/matches.csv", "r") as file:
        lines = file.readlines()
    matches=[line.split(",") for line in lines[1:]]
    os.makedirs("output", exist_ok=True)    
    output=countMatchesPerSeasonApproach2(matches)

    with open("output/1.matches_per_season.txt", "w") as file:
        for season, count in output.items():
            file.write(f"{season}: {count}\n")
        

if __name__ == "__main__":
    main()