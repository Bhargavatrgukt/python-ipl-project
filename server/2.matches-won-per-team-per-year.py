import sys
import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from utils.ipl_utils import matchData

def countMatchesWonPerTeamPerYear(matches):
    winsPerTeamPerYear={}
    for match in matches:
        season=match[1]
        if season in winsPerTeamPerYear:
            if match[10] in winsPerTeamPerYear[season]:
                winsPerTeamPerYear[season][match[10]]+=1
            else:
                winsPerTeamPerYear[season][match[10]]=1
        else:
            winsPerTeamPerYear[season]={}
            winsPerTeamPerYear[season][match[10]]=1
    return winsPerTeamPerYear




def main():
    with open("data/matches.csv", "r") as file:
        lines = file.readlines()
        matches = [line.split(",") for line in lines[1:]]  # Skip header line

    # Ensure output directory exists
    os.makedirs("output", exist_ok=True)    

    output=countMatchesWonPerTeamPerYear(matches)
    try:
        with open("output/2.matches_won_per_team_per_year.txt", "w") as file:
            for season, teams in output.items():
                file.write(f"{season}:\n")
                for team, count in teams.items():
                    file.write(f"  {team}: {count}\n")
                file.write("\n")
    except Exception as e:
        print(f"Error writing to file: {e}")
        return
                
    print("Output written to output/2.matches_won_per_team_per_year.txt")




if __name__=="__main__":
    main()