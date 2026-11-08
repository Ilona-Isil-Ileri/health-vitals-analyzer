from health_vitals.io_utils import load_vitals_csv
import numpy as np

records = load_vitals_csv("data/vitals_sample.csv")

def calculate_vitals(records):
    """
    Calculate average systolic, diastolic, and heart rate using NumPy arrays.
    
    Args:
        records (list of dict): List of vital records.
        
    Returns:
        tuple: avg_sys, avg_dia, avg_hr
    """

    # Convert list of values to NumPy arrays
    sys_array = np.array([row['sys'] for row in records])
    dia_array = np.array([row['dia'] for row in records])
    hr_array = np.array([row['hr'] for row in records])

    # Calculate averages using NumPy
    avg_sys = np.mean(sys_array)
    avg_dia = np.mean(dia_array)
    avg_hr = np.mean(hr_array)

    return avg_sys, avg_dia, avg_hr
