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
#--------------------- admin ---------------------
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


#--------------------- instructor ---------------------
try:
    c.execute("""CREATE TABLE instructor (
            username text,
            passwd text
        )
        """)
except:
    pass

#--------------------- Instructors Table ---------------------
try:
    c.execute("""CREATE TABLE instructors (
            instructorsId text,
            name text,
            gender text,
            reg_status text,
            telephoneNo text,
            availability number,
            Dance_style text,
            hourly_rate number,
            uId text
        )
        """)
except:
    pass

#---------------------- Students Table ------------------------
try:
    c.execute("""CREATE TABLE students (
            studentId text,
            fname text,
            sname text,
            email text,
            gender text,
            dob text,
            telephoneNo text,
            instructorsId text,
            reg_status text,
            sId text
        )
        """)
except:
    pass

# Create another table for courses and section
try:
    c.execute("""CREATE TABLE dance (
            instructorsId text,
            Dance_style text,
            hourly_rate number,
            uId text
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


#---------------------------- Admin Register --------------------------------------
class Admin:
    def Admin_login(self):
        print('\n\t\t--------------Admin Login--------------\n')
        login_uname = input('\tUsername: ')
        login_pass = input('\tPassword: ')

        if(login_uname == "" and login_pass == ""):
            print("\nPlease Enter The Username And Password Details to login...\n")
            self.Admin_login()

        c.execute("SELECT rowid, * FROM admin WHERE username = ? AND passwd = ?", (login_uname, login_pass))
        info = c.fetchall()
        # print(info)
        # pi = info[0][1]
        # print(pi)


        if len(info) >= 1:
            print('\n\t\t-------------- Student | Instructor --------------\n')
            print('\t\t\t1. Go with Instructors Section\n\t\t\t2. Go with Student Section\n\t\t\t3. Exit\n')
            n = input("Enter 1, 2, and 'e' for exit: ")
            if n == '1':
                self.admin_menu(str(info[0][0]))
            elif n == '2':
                c.execute("SELECT rowid, * from instructors")
                result = c.fetchall()
                # print(result)
                if(len(result) >= 1):
                    self.student_menu(str(info[0][0]))
                else:
                    print("\nPlease Kindly Go with Instructor First Becouse there is no instuctos to take lesson for a student...")
                    input("press any key to coninue...")
                    print('\n\t\t-------------- Student | Instructor --------------\n')
                    print('\t\t\t1. Go with Instructors Section\n\t\t\t2. Go with Student Section\n\t\t\t3. Exit\n')
                    n = input("Enter 1, 2, and 'e' for exit: ")
                    if n == '1':
                        self.admin_menu(str(info[0][0]))
                    elif n == '2':
                        self.student_menu(str(info[0][0]))
                    elif n == 'e':
                        exit()
            elif n == 'e':
                exit()
        else:
            print('\n\noops!!.. Admin Your Username or Password are incorrect! Please Try again!')
            n = input("\n\tPress 1. Admin Register or 2. Admin Login: ")
            if n == '1':
                self.register_Admin()
            else:
                self.Admin_login()


    def register_Admin(self):
        print('\n\n\t\t--------------Create an Admin Account--------------\n\n')
        reg_uname = input('\tUsername: ')
        reg_name = input('\tFull Name: ')
        reg_email = input('\tEmail: ')
        reg_pass = input('\tPassword: ')
        reg_conf_pass = input('\tConfirm Password: ')

        #reg_conf_pass = input('\tConfirm Password: ')
        c.execute("SELECT rowid, * FROM admin WHERE username = username ")
        infos = c.fetchall()
        # print(infos)

        for i in infos:
            for s in i:
                if(s==reg_uname):
                    print("Username already Taken... \n")
                    input("Press any key for try again! ")
                    self.register_Admin()

        # c.execute("select count(*) from admin")
        c.execute("SELECT rowid, * FROM admin")

        result = c.fetchall()
        # print(len(result))

        if reg_pass == reg_conf_pass:
            if len(result) < 1:
                c.execute("INSERT INTO admin VALUES (?,?,?,?)", (reg_uname, reg_name, reg_email, reg_pass))
                conn.commit()
                print("\nSuccessfully Registered!!! Now Login! ;-)\n\n")
                self.Admin_login()
            else:
                print("\n Sorry.... ! Only one admin can control this system.. further more details contact danceFeet.")
                exit(0)
        else:
            print("Password does not match! Try again!")
            input("Press any key for try again! ")
            self.register_Admin()

    # --------------------------------- Admin Menu -----------------------------------------------
    def admin_menu(self, uId):
        while True:
            clear.clear()
            print('\n\t---------------- Dance_Feet System (Instructor) ----------------\n\t\t\t\t\t By CT/2017/033\n')
            print(
                '\t\t\t1. Add a New Instructors\n\t\t\t2. Search by Instructors ID\n\t\t\t3. Search All Instructors\n\t\t\t4. Update Instructors Information\n\t\t\t5. Delete Registration Record\n\t\t\t6. Go with Student Section\n\n')
            n = input("Enter 1, 2, 3, 4, 5 and 'e' for exit: ")
            if n == '1':
                self.add_instructor(uId)
            elif n == '2':
                self.search_print(0, uId)
            elif n == '3':
                self.search_all_instructors()
                # self.search_all_instructors_dance()
            elif n == '4':
                self.update_instructor(uId)
            elif n == '5':
                self.delete_instructor(uId)
            elif n == '6':
                c.execute("SELECT rowid, * from instructors")
                result = c.fetchall()
                # print(result)
                if (len(result) >= 1):
                    self.student_menu(uId)
                else:
                    print(
                        "\nPlease Kindly Go with Instructor First Becouse there is no instuctos to take lesson for a student...")
                    input("press any key to coninue...")
                    print(
                        '\n\t---------------- Dance_Feet System (Instructor) ----------------\n\t\t\t\t\t By CT/2017/033\n')
                    print(
                        '\t\t\t1. Add a New Instructors\n\t\t\t2. Search by Instructors ID\n\t\t\t3. Search All Instructors\n\t\t\t4. Update Instructors Information\n\t\t\t5. Delete Registration Record\n\t\t\t6. Go with Student Section\n\n')
                    n = input("Enter 1, 2, 3, 4, 5 and 'e' for exit: ")
                    if n == '1':
                        self.add_instructor(uId)
                    elif n == '2':
                        self.search_print(0, uId)
                    elif n == '3':
                        self.search_all_instructors()
                        # self.search_all_instructors_dance()
                    elif n == '4':
                        self.update_instructor(uId)
                    elif n == '5':
                        self.delete_instructor(uId)
                    elif n == '6':
                        self.student_menu(uId)
                    elif n == 'e':
                        exit()

            elif n == 'e':
                exit()

    # ------------------------------------ Search Instructor --------------------------------
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
            print('\nHere is the Instructors Information:\n')

            print(f'\t* Instructors ID: {id_input}\n')
            print(f'\t* Name: {infos[0][2]}\n')
            print(f'\t* Gender: {infos[0][3]}\n')
            print(f'\t* Telephone Number: {infos[0][5]}\n')
            print(f'\t* Availability: {infos[0][6]}\n')
            print(f'\t* Dance Style: {infos[0][7]}\n')
            print(f'\t* Hourly Rate: {infos[0][8]}\n')
            print(f'\t* Registration Status: {infos[0][4]}\n')

        else:
            print('\n\nNot found!!!')

        c.execute("SELECT rowid, * FROM dance WHERE instructorsId = ? AND uId = ?", (id_input, uId))
        infos_dance = c.fetchall()
        conn.commit()
        if len(infos_dance) >= 1 :
            print(f'\t* Dance Style: {infos_dance[0][2]}\n')
            print(f'\t* Hourly Rate: {infos_dance[0][3]}\n')

        input('\nPress any key to continue...')

    # ------------------------------------ Search All instructors --------------------------
    def search_all_instructors(self):
        print("\n\t\t\t-------------- All Instructors Details. ------------------\n")
        sqlite_select_query = """SELECT * from instructors"""
        c.execute(sqlite_select_query)
        conn.commit()
        results = c.fetchall()

        widths = []
        columns = []
        tavnit = '|'
        separator = '+'

        for cd in c.description:
            # max_col_length = max(list(map(lambda x: len(str(x[1])), results)))
            max_col_length = 25
            widths.append(max(max_col_length, len(cd[0])))
            columns.append(cd[0])

        for w in widths:
            tavnit += " %-" + "%ss |" % (w,)
            # tavnit += " %-" + "%s.%ss |" % (w, w)
            separator += '-' * w + '--+'

        print(separator)
        print(tavnit % tuple(columns))
        print(separator)
        for row in results:
            print(tavnit % row)
        print(separator)

    # ------------------------------------ Search All instructors --------------------------
    def search_all_instructors_dance(self):
        print("\n\t\t\t-------------- All Ilstructors Dance Details and Hourly Rate Details.. ------------------\n")
        sqlite_select_query = """SELECT * from dance"""
        c.execute(sqlite_select_query)
        conn.commit()
        results = c.fetchall()

        widths = []
        columns = []
        tavnit = '|'
        separator = '+'

        for cd in c.description:
            # max_col_length = max(list(map(lambda x: len(str(x[1])), results)))
            max_col_length = 10
            widths.append(max(max_col_length, len(cd[0])))
            columns.append(cd[0])

        for w in widths:
            tavnit += " %-" + "%ss |" % (w,)
            # tavnit += " %-" + "%s.%ss |" % (w, w)
            separator += '-' * w + '--+'

        print(separator)
        print(tavnit % tuple(columns))
        print(separator)
        for row in results:
            print(tavnit % row)
        print(separator)


    # ------------------------------------ Search All students --------------------------
    def search_all_students(self):
        print("\n\t\t\t-------------- All Students Details. ------------------\n")
        sqlite_select_query = """SELECT * from students"""
        c.execute(sqlite_select_query)
        conn.commit()
        results = c.fetchall()

        widths = []
        columns = []
        tavnit = '|'
        separator = '+'

        for cd in c.description:
            # max_col_length = max(list(map(lambda x: len(str(x[1])), results)))
            max_col_length = 25
            widths.append(max(max_col_length, len(cd[0])))
            columns.append(cd[0])

        for w in widths:
            tavnit += " %-" + "%ss |" % (w,)
            # tavnit += " %-" + "%s.%ss |" % (w, w)
            separator += '-' * w + '--+'

        print(separator)
        print(tavnit % tuple(columns))
        print(separator)
        for row in results:
            print(tavnit % row)
        print(separator)


    # ------------------------------------ Add Instructor --------------------------------
    def add_instructor(self, uId):
        clear.clear()
        # Inputing data
        print('\n\t-----------Add Instructors (Enter these information Properly)-----------\n')
        id_input = input('ID number: ')
        c.execute("SELECT rowid, * FROM instructors WHERE instructorsId = instructorsId ")
        infos = c.fetchall()
        # print(infos)

        for i in infos:
            for s in i:
                if (s == id_input):
                    print("Instructor ID  already Taken... \n")
                    input("Press any key for try again! ")
                    self.admin_menu(uId)
        name = input('Name: ')
        gender = input('Gender: ')
        # print('Courses and Section: Input Style "Dance:Type" \nEnter all courses: ')
        # course_sec = [tuple(x.split(':')) for x in input('Dance and Type: Input Style "Dance:Samba Dance:Barat" You Can Enter MULTIPLE dance type using space \nEnter all courses: \n\n').split()]
        dance_style = input('Input Dance Style: ')
        tpNo = input('Telephone Number: ')
        hourlyRate = (input('Hourly Rate: '))
        availability = (input('Availability (Days of the week): '))

        reg = self.reg_status_fn()

        if(id_input != "" and dance_style != "" and hourlyRate != "" and name != "" and gender != "" and reg != "" and availability != ""):
            c.execute("INSERT INTO dance VALUES (?,?,?,?)", (id_input, dance_style, hourlyRate, uId))
            c.execute("INSERT INTO instructors VALUES (?,?,?,?,?,?,?,?,?)", (id_input, name, gender, reg, tpNo, availability, dance_style,hourlyRate, uId))
        else:
            print("Please required Feild to continue...")
            self.add_instructor(uId)

        conn.commit()


        print('\n- Registration Recorded of ID - ',id_input)
        self.search_print(id_input, uId)

    # ------------------------------------ Update Instructor --------------------------------
    def update_instructor(self, uId):
        clear.clear()
        print('\n\t-----------Update Instructors Information-----------\n')
        id_input = input("ID Number: ")
        c.execute("SELECT rowid, * FROM instructors WHERE instructorsId = ? AND uId = ?", (id_input, uId))
        infos = c.fetchall()
        if len(infos) >= 1:
            print(f'\n\t-----------Update Information of ID: {id_input}------------\n\n')

            print(
                '\t\t1. Update Name\n\t\t2. Update Telephone Number\n\t\t3. Update Gender Status\n\t\t4. Update Availability Status\n\t\t5. Update Dance Style\n\t\t6. Update Hourly Rate\n\t\t7. Update Registration Status\n\t\t8. Show Updated Information\n\n')
            while True:
                n = input("Enter 1, 2, 3, 4, 5, 6, 7 or 8: ")
                if n == '1':
                    name = input("Enter Updated Name: ")
                    c.execute("UPDATE instructors SET name = ? WHERE instructorsId = ?", (name, id_input))
                    conn.commit()

                # elif n == '2':
                #     # reg_id = str(infos[0][0])
                #     # c.executemany("DELETE FROM courses WHERE reg_id = ?", reg_id)
                #     # course_sec = [tuple(x.split(':')) for x in input('Dance and Type: Input Style "Dance:Samba Dance:Barat" You can enter multpile dance type using space \nEnter all courses: \n').split()]
                #     # id_course_sec = [(reg_id,) + item for item in course_sec]
                #     # c.executemany("INSERT INTO courses VALUES (?,?,?)", id_course_sec)
                #     # conn.commit()
                #     dance_style = input("Enter Dance style: ")
                #     c.execute("UPDATE instructors SET dance_style = ? WHERE instructorsId = ?", (dance_style, id_input))
                #     conn.commit()

                elif n == '2':
                    tpNo = input("Enter Telephone Number: ")
                    c.execute("UPDATE instructors SET telephoneNo = ? WHERE instructorsId = ?", (tpNo, id_input))
                    conn.commit()

                elif n == '3':
                    gender = input("Enter Gender Status: ")
                    c.execute("UPDATE instructors SET gender = ? WHERE instructorsId = ?", (gender, id_input))
                    conn.commit()

                elif n == '4':
                    availability = input("Enter Availability: ")
                    c.execute("UPDATE instructors SET availability = ? WHERE instructorsId = ?", (availability, id_input))
                    conn.commit()
                #
                # elif n == '6':
                #     hourly_rate = input("Enter Hourly Rate Status: ")
                #     c.execute("UPDATE instructors SET hourly_rate = ? WHERE instructorsId = ?", (hourly_rate, id_input))
                #     conn.commit()



                elif n == '5':
                    Dance_style = input("Enter Dance Style: ")
                    c.execute("UPDATE instructors SET Dance_style = ? WHERE instructorsId = ?", (Dance_style, id_input))
                    c.execute("UPDATE dance SET Dance_style = ? WHERE instructorsId = ?", (Dance_style, id_input))
                    conn.commit()

                elif n == '6':
                    hourly_rate = input("Enter Hourly Rate: ")
                    c.execute("UPDATE instructors SET hourly_rate = ? WHERE instructorsId = ?", (hourly_rate, id_input))
                    c.execute("UPDATE dance SET Dance_style = ? WHERE instructorsId = ?", (hourly_rate, id_input))
                    conn.commit()

                elif n == '7':
                    reg = self.reg_status_fn()
                    c.execute("UPDATE instructors SET reg_status = ? WHERE instructorsId = ?", (reg, id_input))
                    conn.commit()


                elif n == '8':
                    self.search_print(id_input, uId)
                    return
        else:
            print("\nNot Found!!!")

        input('\nPress any key to continue...')

    # ------------------------------------ Update Instructor --------------------------------
    def update_student(self, sId):
        clear.clear()
        print('\n\t-----------Update Students Information-----------\n')
        id_input = input("ID Number: ")
        c.execute("SELECT rowid, * FROM students WHERE studentId = ? AND sId = ?", (id_input, sId))
        infos = c.fetchall()
        if len(infos) >= 1:
            print(f'\n\t-----------Update Information of ID: {id_input}------------\n\n')

            print(
                '\t\t1. Update First Name\n\t\t2. Update Surname\n\t\t3. Update Email\n\t\t4. Update Gender\n\t\t5. Update Date Of Birth\n\t\t6. Update Telephone Number\n\t\t7. Update Instructor\n\t\t8. Update Regstration Status\n\t\t9. Show all Updated inforamtion \n\n')
            while True:
                n = input("Enter 1, 2, 3, 4, 5, 6, 7, 8, or 9: ")
                if n == '1':
                    fname = input("Enter Updated First Name: ")
                    c.execute("UPDATE students SET fname = ? WHERE studentId = ?", (fname, id_input))
                    conn.commit()

                elif n == '2':
                    sname = input("Enter Surname: ")
                    c.execute("UPDATE students SET sname = ? WHERE studentId = ?", (sname, id_input))
                    conn.commit()

                elif n == '3':
                    email = input("Enter Email: ")
                    c.execute("UPDATE students SET email = ? WHERE studentId = ?", (email, id_input))
                    conn.commit()

                elif n == '4':
                    gender = input("Enter Gender Status: ")
                    c.execute("UPDATE students SET gender = ? WHERE studentId = ?", (gender, id_input))
                    conn.commit()

                elif n == '5':
                    dob = input("Enter Date of Birth: ")
                    c.execute("UPDATE students SET dob = ? WHERE studentId = ?", (dob, id_input))
                    conn.commit()

                elif n == '6':
                    telephoneNo = input("Enter Telephone Number: ")
                    c.execute("UPDATE students SET telephoneNo = ? WHERE studentId = ?", (telephoneNo, id_input))
                    conn.commit()

                elif n == '7':
                    print("\n\t\t--- Avilable Instructor... ---")
                    self.search_all_instructors_dance()

                    dance_ins = input("Enter Dance Instructor ID to take lesson for this student: ")

                    for name in (" "):
                        c.execute("SELECT rowid FROM dance WHERE instructorsId = ?", (dance_ins,))
                        data = c.fetchall()
                        if len(data) == 0:
                            print('\n Sorry... There is no Instructor ID .. Please check it... And Your Current Student update details are updated.. thankyou.')
                            self.student_menu(sId)
                        else:
                            c.execute("UPDATE students SET instructorsId = ? WHERE studentId = ?", (dance_ins, id_input))
                            conn.commit()

                elif n == '8':
                    reg = self.reg_status_fn()
                    c.execute("UPDATE students SET reg_status = ? WHERE studentId = ?", (reg, id_input))
                    conn.commit()

                elif n == '9':
                    self.search_print_student(id_input, sId)
                    return
        else:
            print("\nNot Found!!!")

        input('\nPress any key to continue...')


    # ------------------------------------ Delete Instructor --------------------------------
    def delete_instructor(self, uId):
        clear.clear()
        print('\n\t-----------Deleting (by Instructors ID)-----------\n')
        id_input = input('ID Number: ')
        c.execute("SELECT rowid, * FROM dance WHERE instructorsId = ? AND uId = ?", (id_input, uId))
        info = c.fetchall()
        if len(info) >= 1:
            c.execute("DELETE FROM dance WHERE instructorsId = ?", (id_input,))
            conn.commit()
        else:
            print("Not Found!!!")

        c.execute("SELECT rowid, * FROM instructors WHERE instructorsId = ? AND uId = ?", (id_input, uId))
        infos = c.fetchall()
        if len(infos) >= 1:
            c.execute("DELETE FROM instructors WHERE instructorsId = ?", (id_input,))
            # c.executemany("DELETE FROM dance WHERE instructorsId = ?", (id_input))
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



        input('\nPress any key to continue...')

    # ------------------------------------ Register Status Instructor --------------------------------
    def reg_status_fn(self):
        reg_input = (
            input('\nRegistration Status: \n\t1. Completed  2. Partially Completed  3. Pending\nEnter 1, 2 or 3: '))

        if reg_input == "1":
            n = 'Completed'
        elif reg_input == "2":
            n = 'Partially Completed'
        else:
            n = 'Pending'

        return n



    def student_menu(self, sId):
        while True:
            clear.clear()
            print('\n\t---------------- Dance_Feet System (Students) ----------------\n\t\t\t\t\t By CT/2017/033\n')
            print(
                '\t\t\t1. Add a New Student\n\t\t\t2. Search by Student ID\n\t\t\t3. Search all Students\n\t\t\t4. Update Students Details\n\t\t\t5. Delete Students Details\n\t\t\t6. Go with Instructors Section\n ')
            n = input("Enter 1, 2, 3, 4 and 'e' for exit: ")
            if n == '1':
                self.add_students(sId)
            elif n == '2':
                self.search_print_student(0, sId)
            elif n == '3':
                self.search_all_students()
            elif n == '4':
                self.update_student(sId)
            elif n == '5':
                self.delete_student(sId)
            elif n == '6':
                self.admin_menu(self)
            elif n == 'e':
                exit()

    # ------------------------------------ Add students --------------------------------
    def add_students(self, sId):
        clear.clear()
        # Inputing data
        print('\n\t-----------Add students (Enter these information Properly)-----------\n')
        id_input = input('ID number: ')
        c.execute("SELECT rowid, * FROM students WHERE studentId = studentId ")
        infos = c.fetchall()
        # print(infos)

        for i in infos:
            for s in i:
                if (s == id_input):
                    print("Student ID  already Taken... \n")
                    input("Press any key for try again! ")
                    self.student_menu(sId)
        fname = input('Firstname: ')
        sname = input('Surname: ')
        email = input('Email: ')
        gender = input('Gender: ')
        DOB = input('Date of Birth: ')
        tpNo = input('Telephone Number: ')

        print("\n\t\t--- Avilable Instructor... ---")
        self.search_all_instructors_dance()

        dance_ins = input("Enter Dance Instructor ID to take lesson for this student: ")

        for name in (" "):
            c.execute("SELECT rowid FROM dance WHERE instructorsId = ?", (dance_ins,))
            data = c.fetchall()
            if len(data) == 0:
                print('\n Sorry... There is no Instructor ID .. Please check it...')
                self.add_students(sId)
            else:
                reg = self.reg_status_st()

                if (
                        id_input != "" and fname != "" and sname != "" and email != "" and gender != "" and DOB != "" and reg != "" and tpNo != "" and dance_ins != ""):
                    c.execute("INSERT INTO students VALUES (?,?,?,?,?,?,?,?,?,?)",
                              (id_input, fname, sname, email, gender, DOB, tpNo, dance_ins, reg, sId))
                else:
                    print("Please required Feild to continue...")
                    self.add_students(sId)

                    conn.commit()

        print('\n- Registration Recorded of ID - ',id_input)
        self.search_print_student(id_input, sId)



    # ---------------------------- delete_student ----------------------------------------
    def delete_student(self, sId):
        clear.clear()
        print('\n\t-----------Deleting (by Student ID)-----------\n')
        id_input = input('ID Number: ')

        c.execute("SELECT rowid, * FROM students WHERE studentId = ? AND sId = ?", (id_input, sId))
        infos = c.fetchall()
        if len(infos) >= 1:
            c.execute("DELETE FROM students WHERE studentId = ?", (id_input,))
            # c.executemany("DELETE FROM dance WHERE instructorsId = ?", (id_input))
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
            print("Not found....")
            self.student_menu(sId)


        input('\nPress any key to continue...')



    # ------------------------------------ Search Student --------------------------------
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

            print(f'\t* Student ID: {id_input}\n')
            print(f'\t* First Name: {infos[0][2]}\n')
            print(f'\t* SurName: {infos[0][3]}\n')
            print(f'\t* Email Address: {infos[0][4]}\n')
            print(f'\t* Gender: {infos[0][5]}\n')
            print(f'\t* Date Of Birth: {infos[0][6]}\n')
            # print('\tCourses     Section')
            # for info in infos_course:
            #     print('\t', info[1], '\t\t', info[2])
            print(f'\t* Instructor ID: {infos[0][8]}\n')
            print(f'\t* Telephone Number: {infos[0][7]}\n')
            print(f'\t* Registration Status: {infos[0][9]}')

        else:
            print('\n\nNot found!!!')

        input('\nPress any key to continue...')

    # ------------------------------------ Register Status Student --------------------------------
    def reg_status_st(self):
        reg_input =(input('\nRegistration Status: \n\t1. Completed  2. Partially Completed  3. Pending\nEnter 1, 2 or 3: '))

        if reg_input == "1":
            n = 'Completed'
        elif reg_input == "2":
            n = 'Partially Completed'
        else:
            n = 'Pending'

        return str(n)

Admin = Admin()






#---------------------------- Instructor Register --------------------------------------
class Instructor():
    def Instructor_login(self):
        print('\n\t\t--------------Instructor Login--------------\n')
        self.login_uname = input('\tInstructor ID: ')
        login_pass = input('\tPassword: ')

        c.execute("SELECT rowid, * FROM instructor WHERE username = ? AND passwd = ?", (self.login_uname, login_pass))
        info = c.fetchall()
        if len(info) >= 1:
            print("\n You are sucessfully log in...")
            self.student_menu(str(info[0][0]))
        else:
            print('\n\nInstructor Your Registration ID or Password are incorrect! Please Try again!')
            n = input("\n\tPress 1. Instructor Register or 2. Instructor Login: ")
            if n == '1':
                self.register_instructor()
            else:
                self.Instructor_login()



    def register_instructor(self):
        print('\n\n\t\t--------------Create an Instructor Account--------------\n\n')
        reg_uname = input('\tPlease Input Instructor Registration ID: ')

        # reg_conf_pass = input('\tConfirm Password: ')
        c.execute("SELECT rowid, * FROM instructor WHERE username = username ")
        infos = c.fetchall()
        # print(infos)

        for i in infos:
            for s in i:
                if (s == reg_uname):
                    print("Username already Taken... \n")
                    input("Press any key for try again! ")
                    self.register_instructor()


        c.execute("SELECT 1 FROM instructors WHERE instructorsId= ?", (reg_uname,))
        info = c.fetchall()
        # print(info)
        if len(info) >= 1:
            reg_pass = input('\tPassword: ')
            reg_conf_pass = input('\tConfirm Password: ')

            if reg_pass == reg_conf_pass:
                c.execute("INSERT INTO instructor VALUES (?,?)", (reg_uname, reg_pass))
                conn.commit()
                print("\nSuccessfully Registered!!! Now Login! ;-)\n\n")
                self.Instructor_login()
            else:
                print("Password does not match! Try again!")
                input("Press any key for try again! ")
                self.register_instructor()

        else:
            print("\nInstructor Registration ID Doesn't exists Please contact Your Dancefeet Admin... Or Enter Correct Registration ID..")
            self.register_instructor()


    # --------------------------------- Instructor Menu -----------------------------------------------
    def student_menu(self, sId):
        while True:
            clear.clear()
            print('\n\t---------------- Dance_Feet System (instructor) ----------------\n\t\t\t\t\t By CT/2017/033\n')
            print(
                '\t\t\t1. Book Student Lesson\n\t\t\t2. Search by Student ID\n\n')
            n = input("Enter 1, 2, and 'e' for exit: ")
            if n == '1':
                self.book_student(sId)

            elif n == '2':
                self.search_print_student(0, sId)
            elif n == 'e':
                exit()

    # ------------------------------------ Add students --------------------------------
    def book_student(self, sId):
        clear.clear()
        # Inputing data

        print('\n\t----------- Search Student By ID to Book student for a lesson -----------\n')

        id = self.login_uname
        print(id)
        id_input = input('ID number: ')

        c.execute("SELECT rowid, * FROM students WHERE studentId = studentId and instructorsId = ? ", (id,))

        res = c.fetchall()
        # print(res)

        if len(res) >= 1:
            print('\n- Registration Recorded of ID - ', id_input)

            self.search_print_student(id_input, sId)
            print('\n\t-----------Book student for a lesson (Enter these information Properly)-----------\n')


            hourly_rate = input('Input Hourly Rate: ')
            dance_style = input('Enter Dance Style: ')
            reg = self.reg_status_st()

        # reg_id = c.lastrowid
        # id_course_sec = [(id_input,) + item for item in course_sec]
        # c.executemany("INSERT INTO courses VALUES (?,?,?)", id_course_sec)

            input('\nPress any key to continue...')
            self.search_print_student(id_input,sId)

            conn.commit()
        else:
            print("\nYou are Not book this student because this student under another instructor...")




    # ------------------------------------ Search Student --------------------------------
    def search_print_student(self, id_input, sId):
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

            print(f'\t* Student ID: {id_input}\n')
            print(f'\t* First Name: {infos[0][2]}\n')
            print(f'\t* SurName: {infos[0][3]}\n')
            print(f'\t* Email Address: {infos[0][4]}\n')
            print(f'\t* Gender: {infos[0][5]}\n')
            print(f'\t* Date Of Birth: {infos[0][6]}\n')
            # print('\tCourses     Section')
            # for info in infos_course:
            #     print('\t', info[1], '\t\t', info[2])
            print(f'\t* Telephone Number: {infos[0][8]}\n')
            print(f'\t* Registration Status: {infos[0][7]}')

        else:
            print('\n\nNot found!!!')
            self.student_menu(sId)

        input('\nPress any key to continue...')

    # ------------------------------------ Register Status Student --------------------------------
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
Instructor = Instructor()



if __name__ == '__main__':
    # Login Screen
    clear.clear()
    print('\n\t----------------Dance_Feet System----------------\n\t\t\t\t\t By CT/2017/033\n')
    print('\t\t\t1. Admin     2. Instructor     3. Exit\n')
    choose = input('Enter 1 or 2: ')
    if choose == '1':
        print('\t\t\t1. Admin_Login     2. Admin_Register     3. Exit\n')
        choose1 = input("Enter 1, 2, and 'e' for exit: ")
        if choose1 == '1':
            Admin.Admin_login()
        elif choose1 == '2':
            Admin.register_Admin()
        else:
            exit()
    elif choose == '2':
        print('\t\t\t1. Instructor_Login     2. Instructor_Register     3. Exit\n')
        choose2 = input("Enter 1, 2, and 'e' for exit: ")
        if choose2 == '1':
            Instructor.Instructor_login()
        elif choose2 == '2':
            Instructor.register_instructor()
        else:
            exit()
    else:
        exit()