## Department Salary Summary
# In Python, given a list of dicts like [{"employee": "A", "department": "Sales", "salary": 42000}, ...], return a dict mapping each department to its average salary. Round averages to 2 decimal places. Think aloud about how you would write the SQL equivalent.

employees = [
    {"employee": "A", "department": "Sales", "salary": 42000},
    {"employee": "B", "department": "Sales", "salary": 38000},
    {"employee": "C", "department": "HR", "salary": 50000},
    {"employee": "D", "department": "HR", "salary": 45000},
    {"employee": "E", "department": "IT", "salary": 60000}
]
#empty list department
departments={}

for emp in employees:
    dept=emp["department"]
    salary=emp['salary']

    if dept not in departments:
        departments[dept]=[]

    departments[dept].append(salary)
result={}
for dept,salaries in departments.items():
    average=round(sum(salaries)/len(salaries),2)
    result[dept]=average

print(result)

#or another solution using function

def department_salary_summary(dicts):
    totals = {}
    counts = {}

    for record in dicts:
        dept = record["department"]
        salary = record["salary"]

        if dept in totals:
            totals[dept] += salary
            counts[dept] += 1
        else:
            totals[dept] = salary
            counts[dept] = 1

    result = {}
    for dept in totals:
        result[dept] = round(totals[dept] / counts[dept], 2)

    return result