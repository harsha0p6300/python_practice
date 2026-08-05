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