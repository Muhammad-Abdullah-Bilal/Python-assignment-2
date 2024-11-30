def calculate_average_salary(salaries):  
    total_salary = sum(salaries)
    num_salaries = len(salaries)
    average_salary = total_salary / num_salaries
    return average_salary

salaries = [int(salary.strip()) for salary in input("Enter salaries separated by commas: ").split(',')]
average = calculate_average_salary(salaries)
print("Average Salary:", average)
