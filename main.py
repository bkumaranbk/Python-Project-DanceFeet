import sqlite3
from os import system, name  # os for clear function
from time import sleep
import getpass

# Connect to db
conn = sqlite3.connect('DanceFeet.db')

# Create cursor
c = conn.cursor()

# Create table
# Try except 
try:
    c.execute("""CREATE TABLE admin (
            username text,
            fullname text,
            email text,
            passwd text
        )
        """)
except:
    pass


#--------------------- instructor -------------------------------------
try:
    c.execute("""CREATE TABLE instructor (
            username text,
            passwd text
        )
        """)
except:
    pass

#---------------------- Instructors Table ------------------------
try:
    c.execute("""CREATE TABLE instructors (
            instructorsId text,
            name text,
            gender text,
            reg_status text,
            telephoneNo text,
            hourly_rate number,
            availability number,
            uId text
        )
        """)
except:
    pass

#---------------------- Students Table ------------------------
try:
    c.execute("""CREATE TABLE students (
            studentId text,
            name text,
            gender text,
            reg_status text,
            telephoneNo text,
            sId text
        )
        """)
except:
    pass

# Create another table for courses and section
try:
    c.execute("""CREATE TABLE courses (
            reg_id text,
            courses text,
            section text
        )
        """)
except:
    pass

class clear():
    # define our clear function
    def clear(self):
        # for windows
        if name == 'nt':
            _ = system('cls')
            # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
clear = clear()


#------------------------------------ Regiser Status Instructor --------------------------------
class reg_status_fn():
    def reg_status_fn(self):
        reg_input = int(
            input('\nRegistration Status: \n\t1. Completed  2. Partially Completed  3. Pending\nEnter 1, 2 or 3: '))

        if reg_input == 1:
            n = 'Completed'
        elif reg_input == 2:
            n = 'Partially Completed'
        else:
            n = 'Pending'

        return n
reg_status_fn = reg_status_fn()

#------------------------------------ Register Status Student --------------------------------
class reg_status_st():
    def reg_status_st(self):
        reg_input = int(
            input('\nRegistration Status: \n\t1. Completed  2. Partially Completed  3. Pending\nEnter 1, 2 or 3: '))

        if reg_input == 1:
            n = 'Completed'
        elif reg_input == 2:
            n = 'Partially Completed'
        else:
            n = 'Pending'

        return str(n)
reg_status_st = reg_status_st()

#------------------------------------ Search Instructor --------------------------------
class search_print():
    def search_print(self,id_input, uId):
        if id_input == 0:
            clear.clear()
            print('\n\t-----------Searching (by Instructors ID)-----------\n\n')
            id_input = input('ID Number: ')
            print('Searching ', flush=True, end="")
            sleep(0.5)
            print('.', flush=True, end="")
            sleep(0.5)
            print('.', flush=True, end="")
            sleep(0.3)
            print('.', flush=True, end="")

        c.execute("SELECT rowid, * FROM instructors WHERE instructorsId = ? AND uId = ?", (id_input, uId))
        # c.execute("SELECT rowid, * FROM instructors WHERE uId = ?",(uId))
        infos = c.fetchall()
        # print(infos)
        if len(infos) >= 1:
            c.execute("SELECT * FROM courses WHERE reg_id = ?", (str(infos[0][0]),))
            infos_course = c.fetchall()
            conn.commit()
            print('\nHere is the Instructors Information:\n')

            print(f'\tInstructors ID: {id_input}')
            print(f'\tName: {infos[0][2]}\n')
            print(f'\tGender: {infos[0][3]}\n')
            print('\tCourses     Section')
            for info in infos_course:
                print('\t', info[1], '\t\t', info[2])
            print(f'\n\tTelephone Number: {infos[0][5]}\n')
            print(f'\tHourly Rate: {infos[0][6]}\n')
            print(f'\tAvailability: {infos[0][7]}\n')
            print(f'\n\tRegistration Status: {infos[0][4]}')

        else:
            print('\n\nNot found!!!')

        input('\nPress any key to continue...')
search_print = search_print()

#------------------------------------ Search Student --------------------------------
class search_print_student():
    def search_print_student(self,id_input, sId):
        if id_input == 0:
            clear.clear()
            print('\n\t-----------Searching (by Student ID)-----------\n\n')
            id_input = input('ID Number: ')
            print('Searching ', flush=True, end="")
            sleep(0.5)
            print('.', flush=True, end="")
            sleep(0.5)
            print('.', flush=True, end="")
            sleep(0.3)
            print('.', flush=True, end="")

        c.execute("SELECT rowid, * FROM students WHERE studentId = ? AND sId = ?", (id_input, sId))
        # c.execute("SELECT rowid, * FROM students WHERE uId = ?",(uId))
        infos = c.fetchall()
        # print(infos)
        if len(infos) >= 1:
            # c.execute("SELECT * FROM courses WHERE reg_id = ?", (str(infos[0][0]),))
            # infos_course = c.fetchall()
            # conn.commit()
            print('\nHere is the Students Information:\n')

            print(f'\tStudent ID: {id_input}')
            print(f'\tName: {infos[0][2]}\n')
            print(f'\tGender: {infos[0][3]}\n')
            # print('\tCourses     Section')
            # for info in infos_course:
            #     print('\t', info[1], '\t\t', info[2])
            print(f'\n\tTelephone Number: {infos[0][5]}\n')
            print(f'\n\tRegistration Status: {infos[0][4]}')

        else:
            print('\n\nNot found!!!')

        input('\nPress any key to continue...')
search_print_student = search_print_student()


#------------------------------------ Update Instructor --------------------------------
class update_instructor():
    def update_instructor(self, uId):
        clear.clear()
        print('\n\t-----------Update Instructors Information-----------\n')
        id_input = input("ID Number: ")
        c.execute("SELECT rowid, * FROM instructors WHERE instructorsId = ? AND uId = ?", (id_input, uId))
        infos = c.fetchall()
        if len(infos) >= 1:
            print(f'\n\t-----------Update Information of ID: {id_input}------------\n\n')

            print(
                '\t\t1. Update Name\n\t\t2. Update Courses\n\t\t3. Update Telephone Number\n\t\t4. Update Gender Status\n\t\t5. Update Availability Status\n\t\t6. Update Hourly Rate\n\t\t7. Update Registration Status\n\t\t8. Show Updated Information\n\n')
            while True:
                n = input("Enter 1, 2, 3, 4, 5, 6, 7, or 8: ")
                if n == '1':
                    name = input("Enter Updated Name: ")
                    c.execute("UPDATE instructors SET name = ? WHERE instructorsId = ?", (name, id_input))
                    conn.commit()

                elif n == '2':
                    reg_id = str(infos[0][0])
                    c.executemany("DELETE FROM courses WHERE reg_id = ?", reg_id)
                    course_sec = [tuple(x.split(':')) for x in input('Dance and Type: Input Style "Dance:Samba" \nEnter all courses: \n').split()]
                    id_course_sec = [(reg_id,) + item for item in course_sec]
                    c.executemany("INSERT INTO courses VALUES (?,?,?)", id_course_sec)
                    conn.commit()

                elif n == '3':
                    tpNo = input("Enter Telephone Number: ")
                    c.execute("UPDATE instructors SET telephoneNo = ? WHERE instructorsId = ?", (tpNo, id_input))
                    conn.commit()

                elif n == '4':
                    gender = input("Enter Gender Status: ")
                    c.execute("UPDATE instructors SET gender = ? WHERE instructorsId = ?", (gender, id_input))
                    conn.commit()

                elif n == '5':
                    availability = input("Enter Availability: ")
                    c.execute("UPDATE instructors SET availability = ? WHERE instructorsId = ?", (availability, id_input))
                    conn.commit()

                elif n == '6':
                    hourly_rate = input("Enter Hourly Rate Status: ")
                    c.execute("UPDATE instructors SET hourly_rate = ? WHERE instructorsId = ?", (hourly_rate, id_input))
                    conn.commit()

                elif n == '7':
                    reg = reg_status_fn.reg_status_fn()
                    c.execute("UPDATE instructors SET reg_status = ? WHERE instructorsId = ?", (reg, id_input))
                    conn.commit()


                elif n == '8':
                    search_print.search_print(id_input, uId)
                    return
        else:
            print("\nNot Found!!!")

        input('\nPress any key to continue...')
update_instructor = update_instructor()

#------------------------------------ Delete Instructor --------------------------------
class delete_instructor():
    def delete_instructor(self, uId):
        clear.clear()
        print('\n\t-----------Deleting (by Instructors ID)-----------\n')
        id_input = input('ID Number: ')
        c.execute("SELECT rowid, * FROM instructors WHERE instructorsId = ? AND uId = ?", (id_input, uId))
        infos = c.fetchall()
        if len(infos) >= 1:
            c.execute("DELETE FROM instructors WHERE instructorsId = ?", (id_input,))
            c.executemany("DELETE FROM courses WHERE reg_id = ?", (str(infos[0][0]),))
            conn.commit()
            print('Deleting ', flush=True, end="")
            sleep(0.3)
            print('.', flush=True, end="")
            sleep(0.3)
            print('.', flush=True, end="")
            sleep(0.2)
            print('.', flush=True, end="")
            print('\nDeleted!!!')
            # print('\nRegistration Deleted successfully of ID',id_input)
        else:
            print("Not Found!!!")

        input('\nPress any key to continue...')
delete_instructor = delete_instructor()

#------------------------------------ Add Instructor --------------------------------
class add_instructor():
    def add_instructor(self, uId):
        clear.clear()
        # Inputing data
        print('\n\t-----------Add Instructors (Enter these information Properly)-----------\n')
        id_input = input('ID number: ')
        name = input('Name: ')
        gender = input('Gender: ')
        # print('Courses and Section: Input Style "CSE231:C" \nEnter all courses: ')
        print()
        course_sec = [tuple(x.split(':')) for x in input('Dance and Type: Input Style "Dance:Samba" \nEnter all courses: \n\n').split()]
        tpNo = input('Telephone Number: ')
        hourlyRate = int(input('Hourly Rate: '))
        availability = int(input('Availability (Days of the week): '))

        reg = reg_status_fn.reg_status_fn()

        c.execute("INSERT INTO instructors VALUES (?,?,?,?,?,?,?,?)", (id_input, name, gender, reg, tpNo, hourlyRate, availability, uId))
        reg_id = c.lastrowid
        id_course_sec = [(reg_id,) + item for item in course_sec]
        c.executemany("INSERT INTO courses VALUES (?,?,?)", id_course_sec)

        conn.commit()

        print('\n- Registration Recorded of ID - ',id_input)
        search_print.search_print(id_input, uId)
add_instructor = add_instructor()


#------------------------------------ Add students --------------------------------
class add_students():
    def add_students(self, sId):
        clear.clear()
        # Inputing data
        print('\n\t-----------Add students (Enter these information Properly)-----------\n')
        id_input = input('ID number: ')
        name = input('Name: ')
        gender = input('Gender: ')
        # print('Courses and Section: Input Style "Dance:Samba" \nEnter all courses: ')
        print()
        # course_sec = [tuple(x.split(':')) for x in input('Dance and Type: Input Style "Dance:Samba Dance:Barath" \nEnter all courses: \n\n').split()]
        tpNo = input('Telephone Number: ')

        reg = reg_status_fn.reg_status_fn()

        c.execute("INSERT INTO students VALUES (?,?,?,?,?,?)", (id_input, name, gender, reg, tpNo, sId))

        # reg_id = c.lastrowid
        # id_course_sec = [(reg_id,) + item for item in course_sec]
        # c.executemany("INSERT INTO courses VALUES (?,?,?)", id_course_sec)

        conn.commit()

        print('\n- Registration Recorded of ID - ',id_input)
        search_print_student.search_print_student(id_input, sId)
add_students = add_students()



# --------------------------------- Admin Menu -----------------------------------------------
class admin_menu():
    def admin_menu(self, uId):
        while True:
            clear.clear()
            print('\n\t---------------- Dance_Feet System (Admin) ----------------\n\t\t\t\t\t By CT/2017/033\n')
            print(
                '\t\t\t1. Add a New Instructors\n\t\t\t2. Search by Instructors ID\n\t\t\t3. Update Instructors Information\n\t\t\t4. Delete Registration Record\n\n')
            n = input("Enter 1, 2, 3, 4 and 'e' for exit: ")
            if n == '1':
                add_instructor.add_instructor(uId)
            elif n == '2':
                search_print.search_print(0, uId)
            elif n == '3':
                update_instructor.update_instructor(uId)
            elif n == '4':
                delete_instructor.delete_instructor(uId)
            elif n == 'e':
                exit()
admin_menu = admin_menu()

# --------------------------------- Instructor Menu -----------------------------------------------
class instructor_menu():
    def instructor_menu(self, sId):
        while True:
            clear.clear()
            print('\n\t---------------- Dance_Feet System (instructor) ----------------\n\t\t\t\t\t By CT/2017/033\n')
            print(
                '\t\t\t1. Add a New Student\n\t\t\t2. Search by Student ID\n\n')
            n = input("Enter 1, 2, and 'e' for exit: ")
            if n == '1':
                add_students.add_students(sId)
            elif n == '2':
                search_print_student.search_print_student(0, sId)
            elif n == 'e':
                exit()
instructor_menu = instructor_menu()

#---------------------------- Admin Register --------------------------------------
class Admin_login():
    def Admin_login(self):
        print('\n\t\t--------------Admin Login--------------\n')
        login_uname = input('\tUsername: ')
        login_pass = input('\tPassword: ')
        c.execute("SELECT rowid, * FROM admin WHERE username = ? AND passwd = ?", (login_uname, login_pass))
        info = c.fetchall()
        # print(info)
        # pi = info[0][1]
        # print(pi)
        if len(info) >= 1:
            admin_menu.admin_menu(str(info[0][0]))
        else:
            print('\n\nAdmin Your Username or Password are incorrect! Please Try again!')
            n = input("\n\tPress 1. Admin Register or 2. Admin Login: ")
            if n == '1':
                register_Admin.register_Admin()
            else:
                Admin_login.Admin_login()
Admin_login = Admin_login()


class register_Admin():
    def register_Admin(self):
        print('\n\n\t\t--------------Create an Admin Account--------------\n\n')
        reg_uname = input('\tUsername: ')
        reg_name = input('\tFull Name: ')
        reg_email = input('\tEmail: ')
        reg_pass = input('\tPassword: ')
        reg_conf_pass = input('\tConfirm Password: ')

        # c.execute("SELECT * FROM admin")
        # info = c.fetchall()
        #
        # print(info)
        # pi = info[0][0]
        # print(pi)

        # if(reg_name == pi):
        #     print("\nUsername Already Taken ;-(\n\n")
        #     input("Press any key for try again! ")
        #     register_Admin.register_Admin()
        if reg_pass == reg_conf_pass:
            c.execute("INSERT INTO admin VALUES (?,?,?,?)", (reg_uname, reg_name, reg_email, reg_pass))
            conn.commit()
            print("\nSuccessfully Registered!!! Now Login! ;-)\n\n")
            Admin_login.Admin_login()
        else:
            print("Password does not match! Try again!")
            input("Press any key for try again! ")
            register_Admin.register_Admin()
register_Admin = register_Admin()



#---------------------------- Instructor Register --------------------------------------
class Instructor_login():
    def Instructor_login(self):
        print('\n\t\t--------------Instructor Login--------------\n')
        login_uname = input('\tUsername: ')
        login_pass = input('\tPassword: ')
        c.execute("SELECT rowid, * FROM instructor WHERE username = ? AND passwd = ?", (login_uname, login_pass))
        info = c.fetchall()
        if len(info) >= 1:
            instructor_menu.instructor_menu(str(info[0][0]))
        else:
            print('\n\nInstructor Your Username or Password are incorrect! Please Try again!')
            n = input("\n\tPress 1. Instructor Register or 2. Instructor Login: ")
            if n == '1':
                register_instructor.register_instructor()
            else:
                Instructor_login.Instructor_login()
Instructor_login = Instructor_login()

class register_instructor():
    def register_instructor(self):
        print('\n\n\t\t--------------Create an Instructor Account--------------\n\n')
        reg_uname = input('\tUsername: ')

        reg_pass = input('\tPassword: ')
        reg_conf_pass = input('\tConfirm Password: ')
        if reg_pass == reg_conf_pass:
            c.execute("INSERT INTO instructor VALUES (?,?)", (reg_uname, reg_pass))
            conn.commit()
            print("\nSuccessfully Registered!!! Now Login! ;-)\n\n")
            Instructor_login.Instructor_login()
        else:
            print("Password does not match! Try again!")
            input("Press any key for try again! ")
            register_instructor.register_instructor()
register_instructor = register_instructor()

# Login Screen
clear.clear()
print('\n\t----------------Dance_Feet System----------------\n\t\t\t\t\t By CT/2017/033\n')
print('\t\t\t1. Admin     2. Instructor\n')
choose = input('Enter 1 or 2: ')
if choose == '1':
    print('\t\t\t1. Admin_Login     2. Admin_Register\n')
    choose1 = input('Enter 1 or 2: ')
    if choose1 == '1':
        Admin_login.Admin_login()
    elif choose1 == '2':
        register_Admin.register_Admin()
    else:
        exit()
elif choose == '2':
    print('\t\t\t1. Instructor_Login     2. Instructor_Register\n')
    choose2 = input('Enter 1 or 2: ')
    if choose2 == '1':
        Instructor_login.Instructor_login()
    elif choose2 == '2':
        register_instructor.register_instructor()
    else:
        exit()
else:
    exit()