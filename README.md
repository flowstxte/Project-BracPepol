# BracPepol

OOP Based Project

# BracPepol - BRAC University Student Management System

A comprehensive Python-based student management system for BRAC University that provides various analytical and information retrieval functionalities.

## Overview
BracPepol is a student management system designed to handle and analyze student data from BRAC University. The system reads student information from a CSV file and provides multiple functionalities for data analysis, student identification, and information retrieval based on various criteria.

## Features
### Student Data Management
- Reads and processes student data from a CSV file
- Generates unique student IDs based on enrollment year, department, and serial number
- Stores comprehensive student information including personal details, academic progress, and contact information

### Statistical Analysis
- **Gender Ratio Analysis**: Calculate and display the male-to-female student ratio
- **Birth Date Analysis**: Find students sharing the same birth year or month

### Blood Donation Management
- **Location-based Donor Search**: Find blood donors based on blood group and location
- **Department-based Donor Search**: Find blood donors based on blood group and department

### Academic Performance Analysis
- **Probation Student Identification**: Generate reports of students on academic probation (CGPA < 2.00)
- **Valedictorian Candidate Selection**: Identify top 5 students with highest CGPA who have completed at least 130 credits
- **Gold Medalist Candidate Selection**: Identify the highest CGPA holder from each department who has completed at least 130 credits
- **Female Coder Championship Candidates**: Identify female CSE students with CGPA > 3.5 who have completed at least 30 credits

### Telecommunication Analysis
- **SIM User Identification**: Find students using specific mobile operators based on their phone numbers

## Usage Examples
```python
# Calculate male to female ratio
BracPepol.male_femaleRatio()

# Find students born in June 2000
BracPepol.siblingFromAnotherMother(2000, 'Jun')

# Find O+ blood donors in Uttara area (up to 20 donors)
BracPepol.availableBloodDonorByLocation('O+', 'Uttara', 20)

# Find B+ blood donors in CSE department (up to 100 donors)
BracPepol.availableBloodDonorByDept('B+', 'CSE', 100)

# Generate list of CSE students on probation
BracPepol.generateProbationStudentInfo()

# Find top 5 valedictorian candidates
BracPepol.findValedictorianCandidates()

# Find gold medalist candidates from each department
BracPepol.findGoldMedalistCandidates()

# Find female coder championship candidates
BracPepol.findFemaleCoderChampionshipCandidates()

# Find students using TeleTalk SIM cards
BracPepol.findSIM_users('TeleTalk')
```

## Installation
### Clone the repository:
```bash
git clone https://github.com/flowstxte/Project-BracPepol.git
```

### Navigate to the project directory:
```bash
cd Project-BracPepol
```

### Ensure you have the data.csv file in the correct location or update the file path in the code:
```python
with open('path/to/data.csv', 'r') as file:
```

### Run the program:
```bash
python main.py
```

## Data Structure
The system expects a CSV file with the following columns:
- Name
- Gender
- Location
- Birthdate
- Blood Group
- Phone
- Department
- Enrolled Year
- Completed Credits
- Current CGPA

## Requirements
- Python 3.6 or higher
- CSV module (included in Python standard library)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
