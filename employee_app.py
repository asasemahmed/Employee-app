# this program created by Asem abdallah


# employee system app by python
# the program have salary and id and name



#import modules
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox
import sys

#-----------------------------------------------------------------------------------

#connect and open data base
db = sqlite3.connect("amployee.db")
cr = db.cursor()
cr.execute("create table if not exists information (name text, salary integer, id integer)")

#----------------------------------------------------------------------------------

#creatpage from app
main_app = tk.Tk()
main_app.title("Employee app")
main_app.geometry("700x530")
main_app.resizable(width=False, height=False)

# this line of code for add icon in your app
## main_app.iconbitmap("Slack.ico")

#---------------------------------------------------

# the lines
tt = Canvas(main_app)
tt.pack()
tt.create_line(0, 25, 600, 25)
tt.place(x=0, y=120)
tt = Canvas(main_app)
tt.pack()
tt.create_line(0, 25, 600, 25)
tt.place(x=330, y=120)

tt = Canvas(main_app)
tt.pack()
tt.create_line(0, 25, 600, 25)
tt.place(x=0, y=310)
tt = Canvas(main_app)
tt.pack()
tt.create_line(0, 25, 600, 25)
tt.place(x=330, y=310)

#-------------------------------------------------------

# text label
the_text = Label(main_app, text="Show info of any employee", font=("Courier", 20, "italic"))
the_text.pack()
the_text.place(x=180, y=3)

the_text1 = Label(main_app, text="Enter employee id", font=("Arial", 14), justify="left")
the_text1.pack()
the_text1.place(x=0, y=40)

id = StringVar()
id.set("")

id_input = Entry(main_app, width=7, font=("Arial", 20), textvariable=id, justify="left")
id_input.pack()
id_input.place(x=25, y=70)

# fnction for geet employee information
def get_employee_info():

    the_id = id.get()


    try:
        cr.execute(f"select name, salary from information where id = {the_id}")
    except:
        if messagebox.askyesno("Eror", "wrong input \nplease check info and try again"):
            pass
        else:
            sys.exit()

    name_and_salary = cr.fetchone()

    try:
        t1 = Label(main_app, text= f"name : {name_and_salary[0]}\t\t\t\t", fg="red", bg="white smoke", font=("Microsoft JhengHei Light", 16))
        t1.pack
        t1.place(x=200, y=50)
        t1 = Label(main_app, text= f"salary : {name_and_salary[1]}\t\t\t\t\t", fg="red", bg="white smoke", font=("Microsoft JhengHei Light", 16))
        t1.pack
        t1.place(x=200, y=82)
    except:
        if messagebox.askyesno("Eror", "wrong input \nplease check info and try again"):
            pass
        else:
            sys.exit()



btn = Button(main_app, text="OK", width=15, bg="black", fg="white", borderwidth=0, command=get_employee_info)
btn.pack()
btn.place(x=25, y=110)


#----------------------------------------------------------------------------------


the_text2 = Label(main_app, text="insert a new employee", font=("Courier", 20, "italic"))
the_text2.pack()
the_text2.place(x=180, y=150)

#function for add new employee
def add_new_employee():
    the_name = name_of_emp.get()
    the_id = new_id.get()
    the_salary = new_salary.get()



    the_name.strip()

    try:
        the_id = int(the_id)
        the_salary = int(the_salary)
    except:
        if messagebox.askokcancel("Eror", "wrong input at id or salary\n please try again"):
            pass
        else:
            sys.exit()
    
    cr.execute("select id from information")

    all_id = cr.fetchall()

    for id in all_id:
        if the_id == id[0]:
            if messagebox.askyesno("Eror", "This ID already exists\n try agin please"):
                pass
            else:
                sys.exit()
        else:
            continue
    
    cr.execute(f"insert into information (name , id, salary) values ('{the_name}', {the_id}, {the_salary})")
    db.commit()



the_text3 = Label(main_app, text="Enter employee id", font=("Arial", 14), height=2, justify="left")
the_text3.pack()
the_text3.place(x=0, y=230)


new_id = StringVar()
new_id.set("")

input_new_id = Entry(main_app, width=20, font=("Arial", 12), textvariable=new_id, justify="left")
input_new_id.pack()
input_new_id.place(x=220, y=245)


btn1 = Button(main_app, text="OK", width=10, height=2, fg="white", bg="black", borderwidth=0, command=add_new_employee)
btn1.pack()
btn1.place(x=500, y=235)

#------------------------------------------------------------------------------------

the_text3 = Label(main_app, text="Enter employee name", font=("Arial", 14), height=2, justify="left")
the_text3.pack()
the_text3.place(x=0, y=190)

name_of_emp = StringVar()
name_of_emp.set("")

input_new_name = Entry(main_app, width=20, font=("Arial", 12), textvariable=name_of_emp, justify="left")
input_new_name.pack()
input_new_name.place(x=220, y=205)


#------------------------------------------------------------------------------------------------

the_text4 = Label(main_app, text="Enter employee salary", font=("Arial", 14), height=2, justify="left")
the_text4.pack()
the_text4.place(x=0, y=270)

new_salary = StringVar()
new_salary.set("")


input_salary = Entry(main_app, width=20, font=("Arial", 12), textvariable=new_salary, justify="left")
input_salary.pack()
input_salary.place(x=220, y=285)



#------------------------------------------------------------------------------------------------------


the_text2 = Label(main_app, text="Edit employee information", font=("Courier", 20, "italic"))
the_text2.pack()
the_text2.place(x=160, y=340)

#funtion for change infotmation of any employee
def change_info_employee():

    the_id3 = id_for_change_data.get()

    try:
            the_id3 = int(the_id3)
    except:
        if messagebox.askokcancel("Eror", "wrong id \n please try again"):
            pass
        else:
            sys.exit()

    the_text3 = Label(main_app, text="Enter new name ", font=("Arial", 14), height=2, justify="left")
    the_text3.pack()
    the_text3.place(x=250, y=400)

    new_name = StringVar()
    new_name.set("")

    input_new_name = Entry(main_app, width=20, font=("Arial", 12), textvariable=new_name, justify="left")
    input_new_name.pack()
    input_new_name.place(x=410, y=417)

    #function for change name
    def new_emp_name():
    
        the_name = new_name.get()

        the_id2 = the_id3

        try:
            cr.execute(f"update information set name = '{the_name}' where id = {the_id2}")
            db.commit()
        except:
            if messagebox.askokcancel("Eror", "try some thing eror\n please check the info and try again"):
                pass
            else:
                sys.exit()


    btn1 = Button(main_app, text="OK", width=4, fg="white", bg="black", borderwidth=0, command=new_emp_name)
    btn1.pack()
    btn1.place(x=600, y=417)

    #---------------------------------------------------------------------------------------------

    the_text3 = Label(main_app, text="Enter new salary ", font=("Arial", 14), height=2, justify="left")
    the_text3.pack()
    the_text3.place(x=250, y=450)

    new_salary2 = StringVar()
    new_salary2.set("")

    input_new_salary = Entry(main_app, width=20, font=("Arial", 12), textvariable=new_salary2, justify="left")
    input_new_salary.pack()
    input_new_salary.place(x=410, y=467)

    #fuction for change salary
    def new_emp_salary():
        the_salary = new_salary2.get()

        the_id2 = the_id3

        try:
            cr.execute(f"update information set salary = {the_salary} where id = {the_id2}")
            db.commit()
        except:
            if messagebox.askokcancel("Eror", "try some thing eror\n please check the info and try again"):
                pass
            else:
                sys.exit()


    btn1 = Button(main_app, text="OK", width=4, fg="white", bg="black", borderwidth=0, command=new_emp_salary)
    btn1.pack()
    btn1.place(x=600, y=467)


the_text4 = Label(main_app, text="Enter employee id", font=("Arial", 14))
the_text4.pack()
the_text4.place(x=0, y=380)


id_for_change_data = StringVar()
id_for_change_data.set("")

input_id_for_change_data = Entry(main_app, width=7, font=("Arial", 20), textvariable=id_for_change_data, justify="left")
input_id_for_change_data.pack()
input_id_for_change_data.place(x=20, y=410)


btn3 = Button(main_app, width=14, text="OK", bg="black", fg="white", command=change_info_employee)
btn3.pack()
btn3.place(x=20, y=450)

#####################################################################################

# loop running the programe
mainloop()
