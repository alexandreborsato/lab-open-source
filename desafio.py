''' Python Script to calculate the salary after taxes '''

def taxes(salary):
    tax = 0.00
    if salary >= 0 and salary <= 1100:
        tax = 0.05
    elif salary >= 1100.01 and salary <= 2500:
        tax = 0.10
    else:
        tax = 0.15
    return tax * salary

name = str(input("Enter your name: "))
salary = float(input("Enter your salary: "))
benefits = float(input("Enter your benefits: "))
tax_value = taxes(salary)
final_salary = salary + benefits - tax_value
print(f"Hello, {name}! Your final salary is: {final_salary:.2f}")
