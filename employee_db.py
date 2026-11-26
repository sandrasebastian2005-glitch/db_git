import mysql.connector

def get_db_connection():
    try:
        conn=mysql.connector.connect(host="localhost",user="root",password="sandra",database="company_db")
        return conn
    except Exception:
        print("connection failed")
        return None

def create_department(deptname):
    conn=get_db_connection()
    if conn is None:
        return
    try:
        cursor=conn.cursor()
        query="insert into department (deptname) values(%s)"
        cursor.execute(query,(deptname,))
        conn.commit()
        print("the department made successfully")

    except Exception:
        print("creation failed")

    finally:
        cursor.close()
        conn.close()

def create_emp(name,age,salary,dept_id):
    conn=get_db_connection()
    if conn is None:
        return
    try:
        cursor=conn.cursor()
        query="insert into employee (name,age,salary,dept_id) values(%s,%s,%s,%s)"
        data=(name,age,salary,dept_id)
        cursor.execute(query,data)
        conn.commit()
        print("employee created successfully ")
    
    except Exception:
        print("creation failed")

    finally:
        cursor.close()
        conn.close()

def read_all_emp():
    conn=get_db_connection()
    if conn is None:
        return
    try:
        cursor=conn.cursor()
        query="select employee.emp_id,employee.name,employee.age,employee.salary,department.deptname from employee inner join department on employee.dept_id=department.dept_id"
        cursor.execute(query)
        records=cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("no records found")

    except Exception:
        print("reading all records failed")

    finally:
        cursor.close()
        conn.close()

def retreive_emp(emp_id):
    conn=get_db_connection()
    if conn is None:
        return
    try:
        cursor=conn.cursor()
        query="select * from employee where emp_id=%s"
        cursor.execute(query,(emp_id,))
        record=cursor.fetchone() 
        if record:
            print(record)
        else:
            print("no records exist")

    except Exception:
        print("retreiving records failed")

    finally:
        cursor.close()
        conn.close()

def update_emp(emp_id,name,dept_id):
    conn=get_db_connection()
    if conn is None:
        return
    try:
        cursor=conn.cursor()
        query="update employee set name=%s,dept_id=%s where emp_id=%s"
        data=(name,dept_id,emp_id)
        cursor.execute(query,data)
        conn.commit()
        if cursor.rowcount > 0:
            print("updated successfully")
        else:
            print("such emp id does not exist")

    except Exception:
        print("Updation failed")

    finally:
        cursor.close()
        conn.close()

def delete(emp_id):
    conn=get_db_connection()
    if conn is None:
        return
    try:
        cursor=conn.cursor()
        query="delete from employee where emp_id=%s"
        cursor.execute(query,(emp_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("deleted successfully")
        else:
            print("no empid exists")

    except Exception:
        print("deletion failed")

    finally:
        cursor.close()
        conn.close()

def distinct():
    conn=get_db_connection()
    if conn is None:
        return
    try:
        cursor=conn.cursor()
        query="select distinct dept_id from employee"
        cursor.execute(query)
        records=cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("no records found")

    except Exception:
        print("finding distinct failed")

    finally:
        cursor.close()
        conn.close()

def group_by():
    conn=get_db_connection()
    if conn is None:
        return
    try:
        cursor=conn.cursor()
        query="select dept_id ,count(*) from employee group by dept_id"
        cursor.execute(query)
        records=cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("no records found")

    except Exception:
        print("group by failed")

    finally:
        cursor.close()
        conn.close()

def having():
    conn=get_db_connection()
    if conn is None:
        return
    try:
        cursor=conn.cursor()
        query="select dept_id ,count(*) from employee group by dept_id having count(*)>1"
        cursor.execute(query)
        records=cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("no records found")

    except Exception:
        print("having failed")

    finally:
        cursor.close()
        conn.close()

def limit_offset(limit,offset):
    conn=get_db_connection()
    if conn is None:
        return
    try:
        cursor=conn.cursor()
        query="select * from employee limit %s offset %s"
        cursor.execute(query,(limit,offset,))
        records=cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("no records found")

    except Exception:
        print("limit offset failed")

    finally:
        cursor.close()
        conn.close()

while True:
    print("\nEMPLOYEE MANAGEMENT SYSTEM")
    print("1. Create Department")
    print("2. Create Employee")
    print("3. Read All Employees")
    print("4. Retrieve Employee")
    print("5. Update Employee")
    print("6. Delete Employee")
    print("7. Display Unique Departments")
    print("8. Group By Department")
    print("9. Having")
    print("10. Limit and Offset")
    print("11. Exit")

    ch = int(input("enter your choice:"))
    if ch == 1:
        dept_name = input("Enter department name:")
        create_department(dept_name)

    elif ch == 2:
        name = input("Enter employee name:")
        age = int(input("Enter age:"))
        salary = float(input("Enter salary:"))
        dept_id = int(input("Enter department ID:"))
        create_emp(name,age,salary,dept_id)

    elif ch == 3:
        read_all_emp()

    elif ch == 4:
        emp_id = int(input("Enter employee ID:"))
        retreive_emp(emp_id)  

    elif ch == 5:
        emp_id = int(input("Enter employee ID:"))
        name = input("Enter new name:")
        dept_id = int(input("Enter department ID:"))

        update_emp(emp_id,name,dept_id)

    elif ch == 6:
        emp_id = int(input("Enter employee ID:"))
        delete(emp_id)

    elif ch == 7:
        distinct()

    elif ch == 8:
        group_by()

    elif ch == 9:
        having()

    elif ch == 10 :
        limit = int(input("Enter number of records:"))
        offset = int(input("Enter number of records to skip:"))

        limit_offset(limit,offset)

    else:
        exit()

        