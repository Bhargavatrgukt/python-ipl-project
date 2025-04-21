import csv

def csv_to_dict(filename):
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
         # This will read the CSV as dictionaries
        rows = [row for row in csv_reader]
    return rows

def get_batsman_bowler_dismissals(deliveries):
    result = {}

    for delivery in deliveries:
        if (
            delivery["batsman"] == delivery["player_dismissed"]
            and delivery["dismissal_kind"].lower() != "run out"
        ):
            batsman = delivery["batsman"]
            bowler = delivery["bowler"]
            pair = f"{batsman}--vs--{bowler}"

            if pair not in result:
                result[pair] = 1
            else:
                result[pair] += 1

    return dict(sorted(result.items(), key=lambda x: x[1], reverse=True))

def main():
    deliveries_filename= 'data/deliveries.csv'  
    deliveries = csv_to_dict(deliveries_filename)
    output=get_batsman_bowler_dismissals(deliveries)
    try:
        with open("output/8.batsman_bowler_dismissals.txt", "w") as file:
            for pair, count in output.items():
                file.write(f"{pair}:{count}\n")
        print("output/8.batsman_bowler_dismissals.txt")
    except Exception as e:
        print(f"Error writing to file: {e}")
        return
    return

if __name__=="__main__":
    main()