import employee_info

print("Test_employee_info")

def test_get_employees_by_age_range():
    result = []
    input_upper_age_limit = 26
    input_lower_age_limit = 24
    result = employee_info.get_employees_by_age_range(input_lower_age_limit, input_upper_age_limit)
    test = [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000}]

    assert (test == result)

def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    test = 60166.666666666664
    
    assert (test == result)

def test_get_employees_by_dept():
    result = []
    input_department = "Marketing"
    result = employee_info.get_employees_by_dept(input_department)
    test = [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]

    assert (test == result)