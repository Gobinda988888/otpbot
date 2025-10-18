import sqlite3
from dbase import *

def main():
    adminid = 5755448879
    check = check_admin(adminid)
    if check == True:
        print("Admin already exists")
    else:
        try:
            create_admin(adminid)
            create_user_lifetime(adminid)
        except:
            print('something went wrong')
        else:
            print('Admin created...')
    james = fetch_UserData_table()
    print(james)
if __name__ == '__main__':
    main()