import application.salary as salary, application.people as people
from datetime import datetime

if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    date = datetime.now().date()
    print(date)