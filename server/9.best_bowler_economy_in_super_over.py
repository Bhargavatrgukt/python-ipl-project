import csv
# from ..utils.ipl_utils import csv_to_dict
from utils.ipl_utils import csv_to_dict

# def csv_to_dict(filename):
#     with open(filename, mode='r') as file:
#         csv_reader = csv.DictReader(file)
#          # This will read the CSV as dictionaries
#         rows = [row for row in csv_reader]
#     return rows


def find_lowest_economy_bowler_in_super_over(deliveries):
    bowler_stat = {}

    for delivery in deliveries:
        if delivery["is_super_over"] == "1":
            bowler = delivery["bowler"]
            runs = int(delivery["total_runs"])

            if bowler not in bowler_stat:
                bowler_stat[bowler] = {"no_of_balls": 1, "runs_given": runs}
            else:
                bowler_stat[bowler]["no_of_balls"] += 1
                bowler_stat[bowler]["runs_given"] += runs

    lowest_economy_bowler = ""
    lowest_economy = float("inf")

    for bowler, stats in bowler_stat.items():
        overs = stats["no_of_balls"] / 6
        economy = round(stats["runs_given"] / overs, 2) if overs != 0 else float("inf")
        bowler_stat[bowler]["economy"] = economy

        if economy < lowest_economy:
            lowest_economy = economy
            lowest_economy_bowler = bowler

    result = {
        "lowest_economy_bowler": lowest_economy_bowler,
        "stats": bowler_stat[lowest_economy_bowler]
    }

    return result

def main():
    deliveries_filename = 'data/deliveries.csv'
    deliveries = csv_to_dict(deliveries_filename)
    result = find_lowest_economy_bowler_in_super_over(deliveries)

    try:
        with open("output/9.lowest_economy_bowler_in_super_over.txt", "w") as file:
            file.write(f"Bowler: {result['lowest_economy_bowler']}\n")
            file.write(f"Stats: {result['stats']}\n")
        print("output/9.lowest_economy_bowler_in_super_over.txt")
    except Exception as e:
        print(f"Error writing to file: {e}")
        return
    return

if __name__ == "__main__":
    main()
