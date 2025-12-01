# Logging Lab – Custom Version  


This lab is my custom implementation of Lab Assignment 6 for Experiment Tracking & MLOps.  
It demonstrates how to build a complete Python logging pipeline using:

- Custom logger configuration  
- Console + file logging  
- Exception handling  
- Modular code structure (multi-file project)  
- Real dataset loading  
- Analytics with detailed debugging information  

This version uses a **real CSV dataset** and includes enhancements that are NOT part of the original lab.  
All code is original, modular, and organized professionally.

---

## 📁 Project Structure
```bash
python-logging-lab-custom-Meena/
│
├── app/
│   ├── logger_config.py       # Creates the logger, handlers, format, log file
│   ├── data_loader.py         # Safely loads CSV data with exception logging
│   └── analyzer.py            # Performs calculations with smart column detection
│
├── data/
│   └── sales_data.csv         # Real dataset with Height/Weight attributes
│
├── logs/
│   └── app.log                # Auto-created log file (generated at runtime)
│
├── venv/                      # Virtual environment (not included in repo)
│
└── main.py                    # Main application runner
```
---

## 🎯 Project Overview

This lab demonstrates **professional-grade logging** using Python’s built-in `logging` module.

### Key features:
- Logging to **both console and file** using handlers  
- **Custom logger names** for each module (data loader, analyzer, main app)  
- **Exception logging with full tracebacks**  
- Automatically creates a `logs/` directory  
- Loads a **real CSV dataset** (Height & Weight)  
- Performs analytics (mean, max, etc.) while logging every step  
- Smart column detection (handles columns like `Height(Inches)` or `"Weight(Pounds)"`)  
- Completely modular, clean, and reproducible  

---

## 🔧 Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd python-logging-lab-custom-Meena
```
2️⃣ Create a virtual environment
```bash
python3 -m venv venv
```
3️⃣ Activate the virtual environment (Mac/Linux)
```bash
source venv/bin/activate
```
4️⃣ Install required packages
```bash
pip install pandas
```
⸻

▶️ How to Run the Project

Run the main application:
```bash
python main.py
```
You will see log output in the terminal:
```bash
2025-11-30 20:51:36,155 - sales_app - DEBUG - Logger initialized successfully
2025-11-30 20:51:36,155 - sales_app.data_loader - INFO - Loading dataset...
2025-11-30 20:51:36,156 - sales_app.analyzer - INFO - Calculating average weight...
...
```
And a log file will be created automatically in:
```bash
logs/app.log

```
⸻

📊 Example Output (From This Project)
```bash
Average Weight: 127.22
Maximum Height: 73.9
```
Log file contains:
```bash
DEBUG - Dataset shape: (200, 3)
DEBUG - Average weight from column ' "Weight(Pounds)"'
DEBUG - Maximum height from column ' Height(Inches)"'
INFO  - Application finished successfully

```
⸻

🧠 What This Lab Demonstrates

This custom lab goes beyond basic examples and shows:
	•	How to structure Python projects like a real engineer
	•	How to configure multi-handler logging
	•	How to track data pipeline execution
	•	How to log errors with tracebacks for debugging
	•	How to make your logging pipeline reusable in large applications

⸻

🚀 Enhancements Added (Not in Original Lab)
	•	Smart column matching using regex
	•	Logging directory auto-creation
	•	Modular architecture with components
	•	Real-world dataset
	•	Exception safety for both loading and analytics
	•	Cleaner main application flow
	•	Professional project structure used in industry

⸻

📘 Dataset Used

Publicly available dataset:
	•	Height and Weight Dataset (200 samples)
	•	Source: https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv

This dataset has columns like:
	•	"Height(Inches)"
	•	"Weight(Pounds)"

The analyzer automatically detects these.

