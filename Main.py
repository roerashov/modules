from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date



if __name__ == '__main__':
    print(date.today(),calculate_salary())
    print(date.today(),get_employees())