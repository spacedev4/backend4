# import sqlite3
#
# conn = sqlite3.connect("sample-database.db")
#
# cur = conn.cursor()
#
# cur.execute("SELECT * FROM employees LIMIT 3")
#
# ans = cur.fetchall()
# for i in ans:
#     print(i)
#
# cur.close()
# conn.close()


import sqlite3
from contextlib import closing


# CRUD
def get_connection(database_path):
    return closing(sqlite3.connect(database_path))

def create_employee(database_path,employee_id,first_name, last_name,email,phone_number,hire_date,job_id,salary,manager_id,department_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO employees (employee_id,first_name, last_name,email,phone_number,hire_date,job_id,salary,manager_id,department_id) VALUES (?, ?,?,?, ?,?,?, ?,?,?)", (employee_id,first_name, last_name,email,phone_number,hire_date,job_id,salary,manager_id,department_id))
        connection.commit()
        return cursor.lastrowid


def get_employee(database_path, employee_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees WHERE employee_id=?", (employee_id,))
        return cursor.fetchone()


def update_employee(database_path, employee_id, first_name=None, last_name=None):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        if first_name:
            cursor.execute("UPDATE employees SET first_name=? WHERE employee_id=?", (first_name, employee_id))
        if last_name:
            cursor.execute("UPDATE employees SET last_name=? WHERE employee_id=?", (last_name.strip(), employee_id))
        connection.commit()


def delete_employee(database_path, employee_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM employees WHERE employee_id=?", (employee_id,))
        connection.commit()

database_path = "sample-database.db"

employee_update = update_employee
update_employee(database_path, 207, "Anvar", "Valiyev")

employee_get = get_employee(database_path,207)
print(employee_get)

# employee_create = create_employee(database_path,207,"Ali","Valiyev","ali@gmail.com","+998931234567","08-08-2018", 5,1500,3,10)
# print(employee_create)