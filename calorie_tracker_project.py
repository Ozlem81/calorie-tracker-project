import csv
import sys

DAILY_TARGET = 2000

def read_calories_from_file(filename):
    total_calories = 0
    date = ""

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                print(row)

                try:
                    calories = int(row['Calories'])
                    total_calories += calories
                    date = row['Date']
                except ValueError:
                    print(f"Invalid calorie value: {row['Calories']} — Skipping.")

        return date, total_calories

    except FileNotFoundError:
        print("❌ Input file not found. Please check the file name.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error occurred while reading the file: {e}")
        sys.exit(1)

def write_report(date, total):
    try:
        with open("report.txt", mode='w', encoding='utf-8') as file:
            file.write(f"Date: {date}\n")
            file.write(f"Total Calories Consumed: {total} kcal\n")
            file.write(f"Daily Calorie Target: {DAILY_TARGET} kcal\n")

            difference = DAILY_TARGET - total

            if difference > 0:
                file.write(f"You consumed {difference} kcal less than your target. Well done!\n")
            elif difference < 0:
                file.write(f"You consumed {-difference} kcal more than your target. Consider adjusting your meals.\n")
            else:
                file.write("You met your calorie target exactly!\n")

        print("✅ Report written successfully to report.txt")

    except Exception as e:
        print(f"❌ Error occurred while writing the report: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python calorie_tracker_project.py input.csv")
        sys.exit(1)

    input_file = sys.argv[1]
    date, total_calories = read_calories_from_file(input_file)
    write_report(date, total_calories)

if __name__ == "__main__":
    main()
