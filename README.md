
📘 SQLite + Pandas Data Analysis (College Database)

🧩 Overview

This project demonstrates how to use SQLite and Pandas in Python to store, query, and analyze student data.
It covers:

Creating a local SQLite database

Inserting sample data

Reading the data using Pandas

Performing basic data analysis and exporting to CSV

⚙️ Requirements

Install the required library:
```
pip install pandas
```

💡 sqlite3 is included by default with Python.

🗃️ Database Setup

The script connects to a database file named college.db and creates a table students with the following structure:
```
Column Name	Type	Description
student_id	INTEGER	Primary Key (unique ID)
name	TEXT	Student’s name
department	TEXT	Department name (CSE, IT, AI)
marks	INTEGER	Total marks
gender	TEXT	M / F
city	TEXT	Hometown
```
💻 How to Run

Uncomment the table creation and data insertion code in the script.

Run once to create and populate the table.

Comment them back (to avoid duplicates).

Run again to explore and analyze the data.

📊 Example Operations
🔹 Load Data
```
df = pd.read_sql("SELECT * FROM students", conn)
```
🔹 Explore Data
```
print(df.head())       # First 5 rows
print(df.info())       # Data summary
print(df.describe())   # Statistics
```
🔹 Analyze Data
```
print(df[df['marks'] > 80])                           # Filter high scorers
print(df.groupby('department')['marks'].mean())       # Avg marks by dept
print(df.groupby('gender')['marks'].mean())           # Avg marks by gender
print(df['gender'].value_counts())                    # Gender count
```
📂 Export to CSV
```
df.to_csv("sqldata_new.csv", index=True)
```

Exports all student records to sqldata_new.csv.

🧠 Learnings

How to integrate SQLite and Pandas

Run SQL queries inside Python

Perform statistical summaries

Export data to CSV for reporting

📁 Project Structure
college_project/
│
├── college.db          # SQLite database file
├── college_script.py   # Python script
├── sqldata_new.csv     # Exported CSV file
└── README.md           # Documentation

👩‍💻 Author

Jyothi Madesh

jyothimadesh00@gmail.com
