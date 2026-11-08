from health_vitals.io_utils import load_vitals_csv
from health_vitals.analysis import calculate_vitals

from datetime import datetime

def add_patient_records(records):
    """Allow the user to manually enter new patient records with date/time validation."""
    n = int(input("How many patient records do you want to enter? "))
    
    for i in range(n):
        print(f"Entering record {i+1}:")

        # Validate Date
        while True:
            date = input("Date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:
                print("❌ Invalid date format. Please enter YYYY-MM-DD.")
                
        # Validate Time
        while True:
            time = input("Time (HH:MM): ")
            try:
                datetime.strptime(time, "%H:%m")
                break
            except ValueError:
                print("❌ Invalid time format. Please enter HH:MM.")

        # Systolic, diastolic, heart rate (basic int input)
        while True:
            try:
                sys = int(input("Systolic BP: "))
                dia = int(input("Diastolic BP: "))
                hr = int(input("Heart Rate: "))
                break
            except ValueError:
                print("❌ Please enter valid numbers for BP and heart rate.")

        # Append validated record
        records.append({"date": date, "time": time, "sys": sys, "dia": dia, "hr": hr})

        print(f"\n✅ {n} record(s) added successfully!")
        return records


def main():
    records = None  # initially no data loaded

    # Program disclosure
    print("\n" + "-"*40)
    print("   Welcome to Health Vitals Analyzer")
    print("-"*40)
    print("⚠️  For educational purposes only. Not a medical device.\n")

    while True:
        # Friendly menu
        print("\n--- Main Menu ---")
        print("1. Load data from file or enter new patient records")
        print("2. Show average vitals")
        print("3. Quit")
    
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            print("\nMenu 1: Data Input")
            print("a. Load data from CSV file")
            print("b. Enter new patient record(s)")
            
            sub_choice = input("Choose a or b: ").strip().lower()

            if sub_choice == "a":
                try:
                    records = load_vitals_csv("data/vitals_sample.csv")
                    print(f"\n✅ Data loaded successfully! You have {len(records)} records.")
                except FileNotFoundError:
                    print("\n❌ CSV file not found. Please check the file path and try again.")
            
            elif sub_choice == "b":
                    if records is None:
                        records = []
                    records = add_patient_records(records)
            else:
                print("\n❌ Invalid choice. Please enter 'a' or 'b'.")


        elif choice == "2":
            if records is None or len(records) == 0:
                print("\n⚠️ No data loaded yet! Redirecting you to load or enter data...")
                choice = "1"    # automatically redirect to menu 1 logic

            else:
                avg_sys, avg_dia, avg_hr = calculate_vitals(records)
                print("\n--- Average Vitals ---")
                print(f"Average systolic pressure: {avg_sys:.1f} mmHg")
                print(f"Average diastolic pressure: {avg_dia:.1f} mmHg")
                print(f"Average heart rate: {avg_hr:.1f} bpm")

        elif choice == "3":
            print("Thank you for using Health Vitals Analyzer!")
            print("Stay healthy and come back soon! 👋")
            break

        else:
            print("\n❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()