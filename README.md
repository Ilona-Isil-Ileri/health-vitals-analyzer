# Health Vitals Analyzer (Python) 🩺📊

A beginner-friendly Python project built to explore and practice reading, organizing, and analyzing basic health vital-sign records (blood pressure and heart rate) using modular files and NumPy.

---

## 🎯 Strategic Purpose & Vision

As a medical doctor transitioning into health tech, my goal with this project wasn't just to write lines of code, but to understand how a basic health application comes together: how data is loaded from a CSV file, processed, analyzed using NumPy, and presented through a simple user interface. 

While the current implementation is kept at a foundational, beginner level for learning, the project structure is designed with future extensions in mind (such as more thorough input validation, saving new records in a CSV file, or adding visualizations).

---

## 📌 Project Overview

Instead of putting everything in a single script, I split the application into logical modules:

1. **Data Loading (`io_utils.py`):** Reads vital-sign records from a CSV file, parses rows as dictionaries, and converts text data into usable numbers.
2. **Data Analysis (`analysis.py`):** Uses NumPy arrays to calculate basic averages (`np.mean`) for systolic blood pressure, diastolic blood pressure, and heart rate.
3. **Interactive Menu (`main.py`):** Acts as the user interface, bringing the modules together through a command-line menu allowing users to load data, manually enter records, and view calculated averages.

---

## 🗂️ Project Structure

```text
health_vitals_analyzer/
│
├── data/
│   └── vitals_sample.csv  (Sample / synthetic test data)
│
├── health_vitals/
│   ├── io_utils.py
│   └── analysis.py
│
├── main.py
└── README.md
```

- **main.py:** Runs the main application loop and user menu.
- **health_vitals/io_utils.py:** Handles CSV file reading and data formatting (load_vitals_csv).
- **health_vitals/analysis.py:** Handles numerical calculations using NumPy (calculate_vitals).
- **data/vitals_sample.csv:** Contains sample vital records for testing.

---

## 💡 Key Learnings & Concepts Practiced

Building this project helped me understand the foundational mechanics behind writing structured code:

- **Dividing into Files:** Instead of writing everything in a single script, separating code into different files (modules) and importing functions between them.
- **Data Transformation:** Learning that CSV inputs are read as text and must be converted to numbers before doing mathematical calculations.
- **Data Structures:** Working with lists of dictionaries to organize records in table format.
- **Basic Numerical Analysis:** Using NumPy for basic array-based calculations and handling multiple return values (tuples).
- **User Flow & Error Handling:** Managing user input loops and checking for empty data states before running calculations.

---

## 🚀 Current Status & Future Ideas

Current Implementation: Successfully set up: 

- Modular file structure
- CSV data loading
- NumPy-based average calculations
- Initial interactive menu

Future Improvement Ideas: If expanded further, the project could include:

- Advanced input validation for manual user entries.
- Saving newly entered manual records back to CSV files.
- Basic data visualization using libraries like Matplotlib to show trends over time

---

## 🤖 AI Assistance Note

This project was developed with the guidance of ChatGPT. While AI helped with syntax, debugging, and file organization best practices, the core workflow design and step-by-step learning path were driven by my own exploration of programming fundamentals.

---

## 🚀 How to Run

1. Clone or download this repository:
   git clone [https://github.com/Ilona-Isil-Ileri/health-vitals-analyzer.git](https://github.com/Ilona-Isil-Ileri/health-vitals-analyzer.git)
2. Ensure you have NumPy installed:
   pip install numpy
3. Run the main application from your terminal:
   python main.py

---

(Note: This project is created strictly for educational purposes and programming practice. It is not a medical device.)
