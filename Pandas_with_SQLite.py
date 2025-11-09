import sqlite3
import pandas as pd

# Connect to SQLite (creates database file)
conn = sqlite3.connect('college.db')
cursor = conn.cursor()

#Create 'students' table

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS students (
#     student_id INTEGER PRIMARY KEY,
#     name TEXT,
#     department TEXT,
#     marks INTEGER,
#     gender TEXT,
#     city TEXT
# )
# ''')

# # Insert sample data
#cursor.executemany('''INSERT INTO students (student_id, name, department, marks, gender, city) VALUES (?, ?, ?, ?, ?, ?)''', 
 # [
    # (1, 'Alice', 'CSE', 85, 'F', 'Chennai'),
    #(2, 'Bob', 'IT', 90, 'M', 'Coimbatore'),
    #(3, 'Charlie', 'AI', 75, 'M', 'Salem'),
     #(4, 'Diana', 'CSE', 95, 'F', 'Erode'),
     #(5, 'Ethan', 'AI', 60, 'M', 'Madurai'),
     #(6, 'Fiona', 'IT', 88, 'F', 'Trichy'),
     #(7, 'George', 'CSE', 70, 'M', 'Tirunelveli'),
     #(8, 'Hema', 'AI', 92, 'F', 'Chennai'),
     #(9, 'Ian', 'CSE', 78, 'M', 'Coimbatore'),
     #(10, 'Jenny', 'IT', 83, 'F', 'Salem'),
     #(11, 'Kiran', 'AI', 55, 'M', 'Erode'),
     #(12, 'Latha', 'CSE', 97, 'F', 'Madurai'),
     #(13, 'Manoj', 'IT', 66, 'M', 'Trichy'),
     #(14, 'Nisha', 'AI', 89, 'F', 'Chennai'),
     #(15, 'Om', 'CSE', 81, 'M', 'Tirunelveli')

  #])

#conn.commit()

df = pd.read_sql("SELECT * FROM students", conn)
#print(df)
#print(df.head())  # Show first 5 rows
#print(df.head(10))
#print(df.tail())
#print(df.tail(10))

#print(df.shape)         # (rows, columns)
#print(df.columns)       # Column names
#print(df.info())        # Data summary
#print(df.describe())    # Statistics

#print("Average Marks:", df['marks'].mean())

#print(df.groupby('department')['marks'].mean())
#print(df.groupby('gender')['marks'].mean())

#print(df['gender'].value_counts())

print(df[df['marks'] > 80])

#print(df['name'])               # Single column
#print(df[['name', 'marks']])    # Multiple columns
#print(df.iloc[0])               # First row


#df.to_csv("sqldata_new.csv", index=True)
