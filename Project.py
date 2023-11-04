import csv
class BracPepol:
    
    serial=0
    departmentCodeDict = {'Archi': 1, 'CSE': 2, 'ESS': 3, 'EEE': 4, 'ENH': 5, 'MNS': 6, 'Pharma': 7, 'BBS': 8, 'Law': 9}
    students=[]

    def __init__(self, name, gender, location, birthdate, blood_group, phone, department, enrolled_year, completed_credits, current_cgpa):
        BracPepol.serial+=1
        self.name = name
        self.gender = gender
        self.location = location
        self.birthdate = birthdate
        self.blood_group = blood_group
        self.phone = phone
        self.department = department
        self.enrolled_year = enrolled_year
        self.completed_credits = completed_credits
        self.current_cgpa = current_cgpa
        self.unique_id = str(enrolled_year[-2:])+str(BracPepol.departmentCodeDict[department])+str(BracPepol.serial).zfill(4)
        BracPepol.students.append(self)
    
    @classmethod
    def male_femaleRatio(cls):
        male_count = 0
        female_count = 0
        for i in cls.students:
            if i.gender == 'Male':
                male_count += 1
            elif i.gender == 'Female':
                female_count += 1
        ratio = male_count/female_count
        print(f"Male & Female Students Ratio: {ratio}")
    
    @classmethod
    def siblingFromAnotherMother(cls, year, month=None):
        siblings = []
        for i in cls.students:
            x=i.birthdate.split(', ')
            birthYear = int(x[-1])
            birthMonth = x[1][:3]
            if birthYear == year and birthMonth == month:
                siblings.append(i.name)
            elif birthYear == year and month == None:
                siblings.append(i.name)
        if len(siblings) == 0:
            print("No siblings found.")
        else:
            print("Siblings found: ", siblings)
    
    @classmethod
    def availableBloodDonorByLocation(cls, blood_group, location, count=10):
        donors = []
        for i in cls.students:
            if i.blood_group == blood_group and i.location == location:
                donors.append((i.name, i.phone))
        if len(donors) == 0:
            print("No donors found.")
        else:
            if len(donors)<count:
                print(f"Only {len(donors)} donors available. Couldn't find {count} donors.")
                print("Available donors:")
                for i in range(len(donors)):
                    n, p = donors[i]
                    print(f"{1+i}. Name: {n}, Phone: {p}")
            else:
                print(f"Total {len(donors)} donors found.")
                print(f"Here are the first {count} available donors:")
                for i in range(count):
                    n, p = donors[i]
                    print(f"{1+i}. Name: {n}, Phone: {p}")
    
    @classmethod
    def availableBloodDonorByDept(cls, blood_group, dept=None, count=10):
        donors = []
        if dept != None:
            for i in cls.students:
                if i.blood_group == blood_group and i.department == dept:
                    donors.append((i.name, i.phone, i.location))
        else:
            for i in cls.students:
                if i.blood_group == blood_group:
                    donors.append((i.name, i.phone, i.location))
        if len(donors) == 0:
            print("No donors found.")
        else:
            if dept == None:
                if len(donors)<25:
                    print(f"Only {len(donors)} donors available.")
                    for i in range(len(donors)):
                        n, p, a = donors[i]
                        print(f"{1+i}. Name: {n}, Phone: {p}, Address: {a}")
                else:
                    print(f"Total {len(donors)} donors available. Here are first 25 donors.")
                    for i in range(25):
                        n, p, a = donors[i]
                        print(f"{1+i}. Name: {n}, Phone: {p}, Address: {a}")
            else:
                if len(donors)<count:
                    print(f"Only {len(donors)} donors available. Couldn't find {count} donors.")
                    print("Available donors:")
                    for i in range(len(donors)):
                        n, p, a = donors[i]
                        print(f"{1+i}. Name: {n}, Phone: {p}, Address: {a}")
                else:
                    print(f"Total {len(donors)} donors found.")
                    print(f"Here are the first {count} available donors:")
                    for i in range(count):
                        n, p, a = donors[i]
                        print(f"{1+i}. Name: {n}, Phone: {p}, Address: {a}")
    
    @classmethod
    def generateProbationStudentInfo(cls, dept="CSE"):
        print(f"Probation students in {dept} department:")
        for i in cls.students:
            if i.department == dept and float(i.current_cgpa) < 2.00:
                print(f"Name: {i.name}, ID: {i.unique_id}, Department: {i.department}, Phone: {i.phone}, CGPA: {i.current_cgpa}")
    
    @classmethod
    def findValedictorianCandidates(cls):
        candidates = [i for i in cls.students if int(i.completed_credits) >= 130]
        def sort_key(i):
            return (-float(i.current_cgpa), -int(i.completed_credits), int(i.enrolled_year.split(', ')[-1]))
        candidates.sort(key=sort_key)
        print("Valedictorian Candidates:")
        for i in range(5):
            x=candidates[i]
            print(f"Name: {x.name}, ID: {x.unique_id}, Department: {x.department}, CGPA: {x.current_cgpa}")
    
    @classmethod
    def findGoldMedalistCandidates(cls):
        departments = list(cls.departmentCodeDict.keys())
        candidates = []
        for i in departments:
            s = [j for j in cls.students if j.department == i and int(j.completed_credits) >= 130]
            def sort_key(j):
                return (-float(j.current_cgpa), -int(j.completed_credits), int(j.enrolled_year.split(', ')[-1]))
            s.sort(key=sort_key)
            candidates.append(s[0])
        print('Gold Medalist Candidates:')
        for i in candidates:
            print(f"Department: {i.department}, Name: {i.name}, ID: {i.unique_id}, CGPA: {i.current_cgpa}")

    @classmethod
    def findFemaleCoderChampionshipCandidates(cls):
        candidates = [i for i in cls.students if i.gender == "Female" and i.department == "CSE" and float(i.current_cgpa) >= 3.5 and int(i.completed_credits) >= 30]
        def sort_key(i):
            return (int(i.completed_credits))
        candidates.sort(key=sort_key)
        for i in range(10):
            x=candidates[i]
            print(f"Name: {x.name}, ID: {x.unique_id}")
    
    @classmethod
    def findSIM_users(cls, operatorName):
        operatorDigit = None
        if operatorName == "Grameenphone":
            operatorDigit = ["3", "7"]
        elif operatorName == "Banglalink":
            operatorDigit = ["4", "9"]
        elif operatorName == "TeleTalk":
            operatorDigit = ["5"]
        elif operatorName == "Robi":
            operatorDigit = ["6", "8"]
        else:
            print("Invalid operator name!")
        simUsers = []
        for i in cls.students:
            if i.phone[5] in operatorDigit:
                simUsers.append(i)
        if len(simUsers) == 0:
            print("No student found.")
        else:
            print(f"Students who are using {operatorName} operator:")
            for i in simUsers:
                print(f"Name: {i.name}, Location: {i.location}, Phone: {i.phone}")

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for i in reader:
        BracPepol(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9])

# BracPepol.male_femaleRatio()
# BracPepol.siblingFromAnotherMother()
# BracPepol.availableBloodDonorByLocation()
# BracPepol.availableBloodDonorByDept()
# BracPepol.generateProbationStudentInfo()
# BracPepol.findValedictorianCandidates()
# BracPepol.findGoldMedalistCandidates()
# BracPepol.findFemaleCoderChampionshipCandidates()
# BracPepol.findSIM_users()
