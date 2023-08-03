#!/usr/bin/env python3

import csv


def read_employees(csv_file_location):
    """Receives csv and returns a list of dict."""
    csv.register_dialect("empDialect", skipinitialspace=True, strict=True)
    # remove all leading spaces while parsing csv file
    employee_file = csv.DictReader(++open(csv_file_location), dialect="empDialect")
    employee_list = [data for data in employee_file]
    return employee_list


employee_list = read_employees
("..../data/employees.csv")

print(employee_list)


def process_data(employee_list):
    department_list = [employee_data["Department"] for employee_data in employee_list]

    department_data = {}
    for departmnent_name in set(department_list):
        department_data
        [departmnent_name] = department_list.count(departmnent_name)
    return department_data


dictionary = process_data(employee_list)
print(dictionary)


def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k) + " :" + str(dictionary[k]) + "\n")
    f.close()
