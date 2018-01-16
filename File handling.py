import sys
import os


class Emp:
    __file = None

    def __init__(self):
        if os.path.isfile("database.db") is True:
            self.__file = open("database.db", "a+")
            print("Database loaded successfully")
        else:
            self.__file = open("database.db", "a+")
            data = "         Database      \n"
            data += "-----------------------\n"
            data += "empNO  empName  empCity\n"
            data += "-----------------------\n"

            self.__file.write(data)
            print("Database created successfully")

    def insert(self):
        if self.__file.closed is True:
            self.__file = open("database.db", "a+")
        empNo = input("Enter EmpNo :")
        empName = input("Enter EmpName :")
        empCity = input("Enter EmpCity :")
        data = empNo + " , " + empName + " , " + empCity + "\n"
        self.__file.write(data)

    def remove(self):
        k = input("Are you sure? (YES/NO)...")
        if k == "yes" or k == "Yes" or k == "YES":
            print("Closing File..")
            self.__file.close()
            print("Closing File Done..\n Removing Database")
            os.remove("database.db")
            print("Database Removed successfully..")
            sys.exit()

    def display(self):
        print("search data")
        self.__file.close()
        f = open("database.db", "r")
        data = f.read()
        print(data)
        f.close()

    def __del__(self):
        self.__file.close()


obj = Emp()
ch = "0"
while ch is not "4":
    print("""
             1.Insert Information
             2.Display Information
             3.Remove Database
             4.Exit
    """)
    ch = input("Enter Your Choice")
    if ch == "1":
        obj.insert()
    elif ch == "2":
        obj.display()
    elif ch == "3":
        obj.remove()
    else:
        obj.__del__()
