import pandas as pd


def pd_series_to_dict(data):
    output = {}
    for (season, team), count in data.items():
        if season not in output:
            output[season] = {}
        output[season][team] = count
    return output    


def main():
    match_data = pd.read_csv("data/matches.csv")
    filtered_data=match_data=match_data[["season", "winner"]].groupby(["season", "winner"]).size()
    output=pd_series_to_dict(filtered_data)
    print(output)
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
    return

if __name__ == "__main__":
    main()
