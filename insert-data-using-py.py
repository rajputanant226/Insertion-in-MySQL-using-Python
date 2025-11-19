import mysql.connector  
class Employee:     
    def __init__(self, data):         
        # data must be a tuple with 6 items
        (self.EmployeeID,self.Firstname,self.Email,self.PhoneNumber,self.Position,
         self.Department) = data  
def fetchEmployee(cursor):     
    cursor.execute("SELECT * FROM employees")      
    return list(cursor)  
def insertdata(cursor, emp):     
    q = """
        INSERT INTO employees
        (EmployeeID, Firstname, Email, PhoneNumber, Position, Department)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (
        emp.EmployeeID,emp.Firstname,emp.Email,emp.PhoneNumber,
        emp.Position,emp.Department
    )
    cursor.execute(q, values)  
def main():     
    try:         
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='anant',
            database='db1'
        )         
        if mydb.is_connected():
            print("Connected to MySQL..")
            cursor = mydb.cursor()
            # employeeList = fetchEmployee(cursor)
            # for x in employeeList:
            #     print(x)

            # TO INSERT THE DATA...
            emp = Employee((17, 'Anant', 'anant@gmail.com', 88997711, 'Manager', 'I.T'))
            insertdata(cursor, emp)
            mydb.commit()

            # print("Employee inserted successfully!")

            employeeList = fetchEmployee(cursor)
            for x in employeeList:
                print(x)
        else:             
            print("Connection Failed..")     

    except mysql.connector.Error as e:         
        print("Error:", e)     

    finally:         
        if mydb.is_connected():             
            cursor.close()             
            mydb.close()  


if __name__ == '__main__':     
    main()
