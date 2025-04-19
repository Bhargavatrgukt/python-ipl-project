import csv

def csv_to_dict(filename):
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
         # This will read the CSV as dictionaries
        rows = [row for row in csv_reader]
    return rows

def count_economical_bowlers_in_2015(deliveries):
    bowlers={}
    for delivery in deliveries:
        bowler=delivery["bowler"]
        runs=int(delivery["total_runs"])
        if bowler not in bowlers:
            bowlers[bowler]=[runs,1]  # [total_runs, number_of_deliveries]
        else:
            bowlers[bowler][0]+=runs
            bowlers[bowler][1]+=1 
    bowlers_economy = {
            bowler: round(runs / (deliveries / 6), 2)
            for bowler, (runs, deliveries) in bowlers.items() if deliveries > 0
        }
    return bowlers_economy

def main():
    deliveries_filename= 'data/deliveries.csv'  
    match_filename  = 'data/matches.csv'
    matches = csv_to_dict(match_filename)
    deliveries = csv_to_dict(deliveries_filename)
    matches_played_in_2015={match["id"] for match in matches if match["season"]=="2015"}
    filtered_deliveries=[delivery for  delivery in deliveries if delivery["match_id"] in matches_played_in_2015]
    bowlers_economy=count_economical_bowlers_in_2015(filtered_deliveries)
    top_10_economical_bowlers=sorted(bowlers_economy.items(), key=lambda x: x[1])[:10]
    try:
        with open("output/4.economical_bowlers_in_2015.txt", "w") as file:
            for bowler, economy in top_10_economical_bowlers:
                file.write(f"{bowler}:{economy}\n")
        print("Output written to output/4.economical_bowlers_in_2015.txt")
    except Exception as e:
        print(f"Error writing to file: {e}")
        return


if __name__=="__main__":    
    main()