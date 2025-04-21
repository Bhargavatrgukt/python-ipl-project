import csv
from collections import defaultdict

def csv_to_dict(filename):
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
         # This will read the CSV as dictionaries
        rows = [row for row in csv_reader]
    return rows


# Step 1: Extract match IDs for each season
def get_years_to_match_ids(matches_data):
    years = defaultdict(list)
    for match in matches_data:
        years[match["season"]].append(match["id"])
    return years

# Step 2: Extract batsman stats per year
def get_batsman_stats(years, deliveries_data):
    batsmen_stats = {}

    for year, match_ids in years.items():
        if year not in batsmen_stats:
            batsmen_stats[year] = {}

        for delivery in deliveries_data:
            if delivery["match_id"] in match_ids:
                batsman = delivery["batsman"]
                batsman_runs = int(delivery["batsman_runs"])
                
                if batsman not in batsmen_stats[year]:
                    batsmen_stats[year][batsman] = {"runs_played": 0, "balls_played": 0}

                batsmen_stats[year][batsman]["runs_played"] += batsman_runs
                batsmen_stats[year][batsman]["balls_played"] += 1
    return batsmen_stats        

# Step 3: Calculate strike rate
def calculate_strike_rate(batsmen_stats):
    for year in batsmen_stats:
        for player in batsmen_stats[year]:
            runs = batsmen_stats[year][player]["runs_played"]
            balls = batsmen_stats[year][player]["balls_played"]
            strike_rate = round((runs / balls) * 100, 2) if balls != 0 else 0.0
            batsmen_stats[year][player]["strike_rate"] = strike_rate
    return batsmen_stats

def write_strike_rate_to_file(final_stats, filename):
    try:
        with open(filename, "w") as file:
            for season in sorted(final_stats.keys()):
                file.write(f"Season: {season}\n")
                for player, strike_rate in final_stats[season].items():
                    file.write(f"{player}: {strike_rate}\n")
                file.write("\n")
        print(f"{filename} written successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def main():
    deliveries_filename= 'data/deliveries.csv'  
    match_filename  = 'data/matches.csv'
    matches = csv_to_dict(match_filename)
    deliveries = csv_to_dict(deliveries_filename)
    years = get_years_to_match_ids(matches)
    batsman_stats = get_batsman_stats(years, deliveries)
    final_stats = calculate_strike_rate(batsman_stats)
    write_strike_rate_to_file(final_stats, "output/7.strike_rates_of_batsmen_per_season.txt")

if __name__=="__main__":
    main()    