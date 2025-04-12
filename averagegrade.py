import pandas as pd

# Function to convert GPA to grade (out of 4)
def gpa_to_grade(gpa):
    # Assuming the GPA scale is out of 4 and converting to percentage out of 100
    if gpa == 4.0:
        return 90  # GPA 4.0 corresponds to grade 90+
    elif gpa >= 3.0:
        return 80  # GPA 3.0 corresponds to grade between 80-89
    elif gpa >= 2.0:
        return 70  # GPA 2.0 corresponds to grade between 70-79
    elif gpa >= 1.0:
        return 60  # GPA 1.0 corresponds to grade between 60-69
    else:
        return 50  # GPA less than 1.0 corresponds to grade less than 60

# Function to analyze and convert GPA to grades for each student
def analyze_and_convert_gpa(file_path):
    # Read the CSV file using pandas
    df = pd.read_csv(file_path)

    # Print the columns to verify data
    print("Columns in the CSV file:", df.columns)

    # Remove unnecessary columns
    columns_to_drop = ["StudentID", "Email", "Department", "GraduationYear"]
    df = df.drop(columns=columns_to_drop, errors='ignore')  # Drop columns if they exist

    # Apply the GPA to grade conversion function
    df['Grade'] = df['GPA'].apply(gpa_to_grade)

    # Print the students with corresponding grades
    print("\nStudents with corresponding grades:")
    print(df[['Name', 'Grade']])

# Input the CSV file path
file_path = input("Enter the CSV file path: ")

# Analyze the GPA and convert it to grades
analyze_and_convert_gpa(file_path)
