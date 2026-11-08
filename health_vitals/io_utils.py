import csv
from pathlib import Path

def load_vitals_csv(path: str) -> list[dict]:
    """
    Load the vitals CSV file and return the list of records.
    Each record is a dictionary with keys:
    'date', 'time', 'sys', 'dia', 'hr'
    """

    records = []
    file_path = Path(path)

    with file_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numeric fields to integers
            record = {
                "date": row["date"],
                "time": row["time"],
                "sys": int(row["sys"]),
                "dia": int(row["dia"]),
                "hr": int(row["hr"]),
            }
            records.append(record)

    return records