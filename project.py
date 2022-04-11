import tkinter as tk
from tkinter import ttk
from tkinter import *
from ctypes import windll
from tkinter.messagebox import askyesno
import mysql.connector
from tkinter.font import Font
from tkinter.messagebox import showinfo

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="companyx"
)
myCursor = mydb.cursor()

windll.shcore.SetProcessDpiAwareness(1)


class RegistrationWindow(tk.Toplevel):

    def newEmployeePersonalInfo(self):
        ttk.Label(self, text="DATA HAS BEEN INSERTED", foreground='red').pack()
        fname = self.text1.get()
        lname = self.text2.get()
        area = self.text3.get()
        pincode = self.text4.get()
        state = self.text5.get()
        phoneNo = self.text6.get()

        sql = "insert into employee (fname,lname,area,pincode,state,phoneNo) values (%s,%s,%s,%s,%s,%s)"
        myCursor.execute(sql, (fname, lname, area, pincode, state, phoneNo))
        mydb.commit()

        sql = "update storage set val = val+1"
        myCursor.execute(sql)
        mydb.commit()

    def newEmployeeWorkProfile(self):
        sql = "select val from storage"
        myCursor.execute(sql)

        current_empId = 0

        for i in myCursor.fetchall():
            current_empId = int(i[0])

        print("current empid:", type(current_empId))

        jobType = self.text7.get()
        print(jobType)
        if jobType == "Engineer":
            sql = "insert into engg (empid,salary,pos) values (%s,%s,%s)"
            myCursor.execute(sql, (current_empId, self.text9.get(), self.text8.get()))
            mydb.commit()
        elif jobType == "Salesperson":
            sql = "insert into salesperson(empid,salary,pskill) values (%s,%s,%s)"
            myCursor.execute(sql, (current_empId, self.text9.get(), self.text8.get()))
            mydb.commit()
        else:
            sql = "insert into freelancer (empid,salary,work_type) values (%s,%s,%s)"
            myCursor.execute(sql, (current_empId, self.text9.get(), self.text8.get()))
            mydb.commit()

        showinfo(title="Information", message="Record has been saved successfully")

    def confirm(self):
        answer = askyesno(title='confirmation',
                          message='Are you sure that you want to enter this record?')
        if not answer:
            self.destroy()
        else:
            self.newEmployeePersonalInfo()

    def __init__(self, parent):
        super().__init__(parent)

        self.title("Company X Registration page")

        self.geometry("1200x800")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True)

        frame1 = ttk.Frame(self.notebook, width=480, height=280)
        frame2 = ttk.Frame(self.notebook, width=400, height=280)
        frame1.pack(fill="both", expand=True)
        frame2.pack(fill="both", expand=True)

        self.notebook.add(frame1, text="Personal Information")
        self.notebook.add(frame2, text="work profile")

        photo = tk.PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\registration from 800x 800.png")

        image_label = ttk.Label(frame1, text="image", image=photo, padding=5)
        image_label.image = photo
        image_label.grid(column=1, row=1, sticky=tk.E, rowspan=800, columnspan=980)

        photo = tk.PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\registration from 800x 800.png")

        image_label = ttk.Label(frame2, text="image", image=photo, padding=5)
        image_label.image = photo
        image_label.grid(column=1, row=1, sticky=tk.E, rowspan=800, columnspan=980)

        regFont = Font(family="Arial",
                       weight="bold",
                       size=10)

        label1 = ttk.Label(frame1, text="First Name:", font=regFont)
        label1.grid(column=1000, row=450, padx=10, pady=10, sticky=tk.W)

        self.text1 = tk.StringVar()
        widget1 = ttk.Entry(frame1, textvariable=self.text1)
        widget1.focus()
        widget1.grid(column=1001, row=450, padx=10, pady=10)

        label2 = ttk.Label(frame1, text="Last Name:", font=regFont)
        label2.grid(column=1000, row=451, padx=10, pady=10, sticky=tk.W)

        self.text2 = tk.StringVar()
        widget2 = ttk.Entry(frame1, textvariable=self.text2)
        widget2.grid(column=1001, row=451, padx=10, pady=10)

        label3 = ttk.Label(frame1, text="Area:", font=regFont)
        label3.grid(column=1000, row=452, padx=10, pady=10, sticky=tk.W)

        self.text3 = tk.StringVar()
        widget3 = ttk.Entry(frame1, textvariable=self.text3)
        widget3.grid(column=1001, row=452, padx=10, pady=10)

        label4 = ttk.Label(frame1, text="Pincode:", font=regFont)
        label4.grid(column=1000, row=453, padx=10, pady=10, sticky=tk.W)

        self.text4 = tk.StringVar()
        widget4 = ttk.Entry(frame1, textvariable=self.text4)
        widget4.grid(column=1001, row=453, padx=10, pady=10)

        label5 = ttk.Label(frame1, text="State:", font=regFont)
        label5.grid(column=1000, row=454, padx=10, pady=10, sticky=tk.W)

        self.text5 = tk.StringVar()
        widget5 = ttk.Entry(frame1, textvariable=self.text5)
        widget5.grid(column=1001, row=454, padx=10, pady=10)

        label6 = ttk.Label(frame1, text="Phone No:", font=regFont)
        label6.grid(column=1000, row=455, padx=10, pady=10, sticky=tk.W)

        self.text6 = tk.StringVar()
        widget6 = ttk.Entry(frame1, textvariable=self.text6)
        widget6.grid(column=1001, row=455, padx=10, pady=10)

        label7 = ttk.Label(frame2, text="Field of work:", font=regFont)
        label7.grid(column=1000, row=456, padx=10, pady=10, sticky=tk.W)

        self.text7 = tk.StringVar()
        widget7 = ttk.Combobox(frame2, textvariable=self.text7)
        widget7["values"] = ["Engineer", "Salesperson", "Freelancer"]
        widget7["state"] = "readonly"
        widget7.grid(column=1001, row=456, padx=10, pady=10)

        label8 = ttk.Label(frame2, text="Position:", font=regFont)
        label8.grid(column=1000, row=457, padx=10, pady=10, sticky=tk.W)

        self.text8 = tk.StringVar()
        widget8 = ttk.Entry(frame2, textvariable=self.text8)
        widget8.grid(column=1001, row=457, padx=10, pady=10)

        label9 = ttk.Label(frame2, text="Salary/cost per hour:", font=regFont)
        label9.grid(column=1000, row=458, padx=1, pady=10, sticky=tk.W)

        self.text9 = tk.StringVar()
        widget9 = ttk.Entry(frame2, textvariable=self.text9)
        widget9.grid(column=1001, row=458, padx=10, pady=10)

        save1 = ttk.Button(frame1, text='Save', command=self.confirm)
        save1.grid(column=1000, row=480, padx=10, pady=10, sticky=tk.E)
        save2 = ttk.Button(frame2, text='Save', command=self.newEmployeeWorkProfile)
        save2.grid(column=1000, row=480, padx=10, pady=10, sticky=tk.E)


class GeneratePaySlip(tk.Toplevel):
    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(str(record)))

    def PaySlip(self):
        print("1")
        employeeId = int(self.text1.get())
        sql = "select amount from canteen where canteen.empid = %s"
        myCursor.execute(sql, (employeeId,))
        myResult = myCursor.fetchall()

        canteen_dues = 0
        empSal = 0

        for i in myResult:
            print(i)
            canteen_dues = int(i[0])

        if self.text2.get() == "Engineer":
            sql = "select salary from employee as e inner join engg as eng on e.empid = eng.empid "
            myCursor.execute(sql)
            myResult = myCursor.fetchall()
            empSal = int(myResult[0][0])

            sql = "select e.empid,fname,lname,salary,phoneNo from employee as e inner join engg as eng on e.empid = eng.empid "
            myCursor.execute(sql)
        else:
            sql = "select salary from employee as e inner join salesperson as s on e.empid = s.empid "
            myCursor.execute(sql)
            myResult = myCursor.fetchall()
            empSal = int(myResult[0][0])

            sql = "select e.empid,fname,lname,salary,phoneNo from employee as e inner join salesperson as s on e.empid = s.empid "
            myCursor.execute(sql)

        myResult = myCursor.fetchall()
        # y = []
        # for i in myResult:
        #     y = list(i)
        #     y.append(str(empSal-canteen_dues))

        sql = "delete from canteen where empid = (%s)"
        myCursor.execute(sql, (employeeId,))
        mydb.commit()

        columns = ('e.empid', 'fname', 'lname', 'salary', 'phoneNo', 'updated_salary')

        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.column("#0", width=0, minwidth=200, stretch=True)
        self.tree.column("#1", width=0, minwidth=200, stretch=True)
        self.tree.column("#2", width=0, minwidth=200, stretch=True)
        self.tree.column("#3", width=0, minwidth=200, stretch=True)
        self.tree.column("#4", width=0, minwidth=200, stretch=True)
        self.tree.column("#5", width=0, minwidth=200, stretch=True)

        # define headings
        # tree.heading('first_name', text='First Name')
        # tree.heading('last_name', text='Last Name')
        # tree.heading('email', text='Email')

        self.tree.heading('e.empid', text='EMPID')
        self.tree.heading('fname', text='FIRST NAME')
        self.tree.heading('lname', text='LAST NAME')
        self.tree.heading('salary', text='BASE SALARY')
        self.tree.heading('phoneNo', text="PHONE NUMBER")
        self.tree.heading('updated_salary', text="Updated SALARY")

        # generate sample data
        # contacts = []
        # for n in range(1, 100):
        #     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

        # add data to the treeview
        for row in myResult:
            self.tree.insert('', tk.END, values=row)

        self.tree.bind('<<TreeviewSelect>>', self.item_selected)

        self.tree.grid(row=230, column=1000, sticky='nsew', rowspan=400, columnspan=100)

        # add a scrollbar
        # scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        # tree.configure(yscroll=scrollbar.set)
        # scrollbar.grid(row=0, column=1, sticky='ns')
        ttk.Label(self, text="", background="white").grid(row=240, column=1000)
        ttk.Label(self, text="", background="white").grid(row=241, column=1000)

        scrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscroll=scrollbar.set)
        scrollbar.grid(row=250, column=1000, sticky='we')

    def __init__(self, parent):
        super().__init__(parent)

        self.title("Company X Registration page")

        # To specify size of a window
        self.geometry("1200x800")

        photo = tk.PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\registration from 800x 800.png")

        image_label = ttk.Label(self, text="image", image=photo, padding=5)
        image_label.image = photo
        image_label.grid(column=1, row=1, sticky=tk.E, rowspan=800, columnspan=980)

        label1 = ttk.Label(self, text="Enter the empId:", font=("Arial", 12))
        label1.grid(column=1000, row=100, padx=10)

        self.text1 = tk.StringVar()
        textbox = ttk.Entry(self, textvariable=self.text1)
        textbox.grid(column=1001, row=100, padx=10)

        label2 = ttk.Label(self, text="Select Job-type:", font=("Arial", 12))
        label2.grid(column=1000, row=101, padx=10)

        self.text2 = tk.StringVar()
        widget7 = ttk.Combobox(self, textvariable=self.text2)
        widget7["values"] = ["Engineer", "Salesperson"]
        widget7["state"] = "readonly"
        widget7.grid(column=1001, row=101, padx=10, pady=10)

        ttk.Button(self, text="Generate Pay Slip", command=self.PaySlip).grid(column=1001, row=102, padx=10,
                                                                              sticky=tk.E)


class companyx_canteen(tk.Toplevel):
    def placeOrder(self):
        employeeId = int (self.text.get ())
        sql = "select amount from canteen where empid = %s"
        myCursor.execute(sql,(employeeId,))
        myResult = myCursor.fetchall()
        print ("size :", len (myResult))

        if len(myResult) == 0:
            sql = "insert into canteen values (%s,%s)"
            myCursor.execute(sql, (employeeId, self.total))
            mydb.commit()

        else:
            self.total += (myResult[0][0])
            sql = "update canteen set amount = (%s) where empid = %s"
            myCursor.execute(sql, (self.total,employeeId))
            mydb.commit()


        showinfo(title="Information",
                 message="Your order has been placed\nTotal bill is {}".format (self.total))

    def calculate(self):
        head_font = Font(
            family="times",
            size=15,
            weight="bold"
        )
        price = [30,5,150,50,70]
        order = [self.text1.get (),
                 self.text2.get (),
                 self.text3.get (),
                 self.text4.get (),
                 self.text5.get ()]

        self.total = 0

        for i in range(len(order)):
            if (order[i] != ""):
                self.total += int (order[i])*price[i]

        lable14 = Label(self, text="Your Total Bill is - " + str(self.total), font=head_font,foreground="red", background="black")

        lable14.grid(column = 1000, row = 500)
        # lable14.after(1000, lable14.destroy)
        # tk.after (1000, self.calculate)

        ttk.Button (self,text = "Place Order", command = self.placeOrder).grid(
            column = 1001, row = 500
        )


    def __init__(self, parent):
        super().__init__(parent)

        print("in canteen")
        self.title("CompanyX canteen")
        self.geometry("1600x800")

        photo = tk.PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\canteen 800x800.png")
        image_label = ttk.Label(self, text="image", image=photo, padding=5)
        image_label.image = photo
        image_label.grid(column=1, row=1, sticky=tk.E, rowspan=800, columnspan=980)

        # lable7 = Label(self, text="MENU", font="times 28 bold")
        # lable7.place(x=350, y=20, anchor="center")

        canteen_font = Font (
            family = "Arial",
            size = 12
        )

        head_font = Font (
            family = "times",
            size = 15,
            weight = "bold"
        )
        label = ttk.Label(self, text="Enter your EMPLOYEE ID", font=canteen_font)
        label.grid(column=1000, row=180, padx=20, pady=50)
        self.text = tk.StringVar()
        e1 = ttk.Entry(self, textvariable=self.text)
        e1.grid(column=1001, row=180, padx=20, pady=50, sticky=tk.W)

        label = ttk.Label(self,text = "FOOD ITEMS", font = head_font)
        label.grid (column= 1000, row = 280, padx = 20, pady = 20,sticky=tk.W)

        label = ttk.Label(self, text="PRICE",font= head_font)
        label.grid(column=1001, row=280, padx = 20, pady = 20,sticky=tk.W)

        label = ttk.Label(self, text="PLACE ORDER", font=head_font, foreground="red")
        label.grid(column=1002, row=280, padx=80, pady=20)

        lable1 = Label(self, text="Coke", font=canteen_font)
        lable1.grid (column = 1000, row = 300,padx = 20, pady =5,sticky=tk.W)

        lable1 = Label(self, text="Rs. 30", font=canteen_font)
        lable1.grid(column=1001, row=300, padx =20, pady = 5,sticky=tk.W)

        lable2 = Label(self, text="Samosa", font=canteen_font)
        lable2.grid (column = 1000, row = 301,padx = 20,pady = 5,sticky=tk.W)

        lable2 = Label(self, text="Rs 5", font=canteen_font)
        lable2.grid(column=1001, row=301, padx=20, pady=5,sticky=tk.W)

        lable3 = Label(self, text="Pizza", font=canteen_font)
        lable3.grid (column = 1000, row = 302,padx = 20, pady = 5,sticky=tk.W)

        lable3 = Label(self, text="Rs 150", font=canteen_font)
        lable3.grid(column=1001, row=302, padx=20, pady=5,sticky=tk.W)

        lable4 = Label(self, text="Chilli Potato", font=canteen_font)
        lable4.grid (column = 1000, row = 303, padx = 20, pady = 5,sticky=tk.W)

        lable4 = Label(self, text="Rs 50", font=canteen_font)
        lable4.grid(column=1001, row=303, padx=20, pady=5,sticky=tk.W)

        lable5 = Label(self, text="Chowmein", font=canteen_font)
        lable5.grid (column = 1000, row = 304, padx = 20, pady = 5,sticky=tk.W)

        lable5 = Label(self, text="Rs 70", font=canteen_font)
        lable5.grid(column=1001, row=304, padx=20, pady=5,sticky=tk.W)

        self.text1 = tk.StringVar()
        e1 = ttk.Entry (self, textvariable=self.text1)
        e1.grid (column = 1002, row = 300,padx = 80, pady =5,sticky=tk.W)

        self.text2 = tk.StringVar()
        e1 = ttk.Entry(self, textvariable=self.text2)
        e1.grid(column=1002, row=301, padx=80, pady=5, sticky=tk.W)

        self.text3 = tk.StringVar()
        e1 = ttk.Entry(self, textvariable=self.text3)
        e1.grid(column=1002, row=302, padx=80, pady=5, sticky=tk.W)

        self.text4 = tk.StringVar()
        e1 = ttk.Entry(self, textvariable=self.text4)
        e1.grid(column=1002, row=303, padx=80, pady=5, sticky=tk.W)

        self.text5 = tk.StringVar()
        e1 = ttk.Entry(self, textvariable=self.text5)
        e1.grid(column=1002, row=304, padx=80, pady=5, sticky=tk.W)

        button = ttk.Button(self,text = "Generate bill",command = self.calculate)
        button.grid (column=1002, row = 305, padx = 130)
        #
        # self.text1 = StringVar()
        # self.e1 = Entry(self, textvariable=self.text1)
        # self.e1.place(x=20, y=150)
        #
        # lable9 = Label(self, text="Samosa", font="times 18")
        # lable9.place(x=20, y=200)
        #
        # self.text2 = StringVar()
        # self.e2 = Entry(self)
        # self.e2.place(x=20, y=230)
        #
        # lable10 = Label(self, text="Pizza", font="times 18")
        # lable10.place(x=20, y=280)
        #
        #
        # self.e3 = Entry(self)
        # self.e3.place(x=20, y=310)
        #
        # lable11 = Label(self, text="Chilli Potato", font="times 18")
        # lable11.place(x=20, y=360)
        #
        # self.e4 = Entry(self)
        # self.e4.place(x=20, y=390)
        #
        # lable12 = Label(self, text="Chowmein", font="times 18")
        # lable12.place(x=250, y=120)
        #
        # self.e5 = Entry(self)
        # self.e5.place(x=250, y=150)
        #
        # lable13 = Label(self, text="Burger", font="times 18")
        # lable13.place(x=250, y=200)
        #
        # self.e6 = Entry(self)
        # self.e6.place(x=250, y=230)

        #In order to display the total amount after some time



class QueryRunner(tk.Toplevel):
    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))

    def sqlRun(self):
        sql = self.text.get('1.0', 'end')
        s = ""
        flag = False
        a = []

        for i in sql:
            if i != " " and i != ",":
                s = s + i
                continue

            elif flag == False:
                print(s)
                if s == "create" or s == "CREATE" or s == "Create":
                    ttk.Label(self, text="Can't run CREATE query !", foreground="red").grid(column=0, row=3)
                    return 0

                if s == "select" or s == "SELECT" or s == "Select":
                    flag = True
                    s = ""

            elif s == "from":
                break

            elif s != "" and s != "distinct":
                a.append(s)
                s = ""

        print(a)
        myCursor.execute(sql)

        myResult = myCursor.fetchall()

        columns = tuple(a)

        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        # tree.heading('first_name', text='First Name')
        # tree.heading('last_name', text='Last Name')
        # tree.heading('email', text='Email')

        for i in columns:
            self.tree.heading(i, text=i)

        # generate sample data
        # contacts = []
        # for n in range(1, 100):
        #     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

        # add data to the treeview
        for row in myResult:
            self.tree.insert('', tk.END, values=row)

        self.tree.bind('<<TreeviewSelect>>', self.item_selected)

        self.tree.grid(row=230, column=1000, sticky='nsew', rowspan=400, columnspan=100)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=230, column=1001, sticky='ns')



    def __init__(self, parent):
        super().__init__(parent)
        self.title("Comapny X Query Runner")

        # To specify size of a window
        self.geometry("1650x800")

        photo = tk.PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\query runner 800x800.png")

        image_label = ttk.Label(self, text="image", image=photo, padding=5)
        image_label.image = photo
        image_label.grid(column=1, row=1, sticky=tk.E, rowspan=800, columnspan=980)

        self.username = tk.StringVar()
        self.password = tk.StringVar()
        loginFont = Font(
            family="STsong",
            size=25,
            weight="bold",
            underline=1
        )
        ttk.Label(self, text="OUERY RUNNER", font=loginFont).grid(column=1000, row=190, sticky=tk.N, columnspan=10)

        self.text = tk.Text(self, height=10)
        self.text.grid(column=1000, row=200)
        self.text.focus()

        ttk.Button(self, text="Run Query", command=self.sqlRun).grid(column=1000, row=201, pady=10)


class ProjectDetails(tk.Toplevel):
    def AddNewProject(self):
        proj_name = self.text1.get()
        start_date = self.text2.get()

        sql = "insert into projects (proj_name,start_date) values (%s,%s)"
        myCursor.execute(sql, (proj_name, start_date))
        mydb.commit()

        sql = "update storage2 set val = val+1"
        myCursor.execute(sql)
        mydb.commit()

        sql = "select val from storage2"
        myCursor.execute(sql)
        myResult = myCursor.fetchall()

        projectId = int(myResult[0][0])

        sql = "insert into ncomp_project values (%s,%s)"
        myCursor.execute(sql, (projectId, "0"))
        mydb.commit()

        ttk.Label(self.frame1, text="DATA HAS BEEN INSERTED", foreground="red").grid(column=1001, row=460)
        showinfo(title="Information", message="DATA HAS BEEN INSERTED\nAlloted PROJECT ID:{}".format(projectId))

    def AssignProject(self):
        projectId = int(self.text3.get())
        employeeId = int(self.text4.get())
        join_date = self.text5.get()

        sql = "insert into proj_member values (%s,%s,%s)"
        myCursor.execute(sql, (employeeId, projectId, join_date))
        mydb.commit()

        ttk.Label(self.frame2, text="DATA HAS BEEN INSERTED", foreground="red").grid(column=1001, row=460)
        showinfo(title="Information",
                 message="Employee with EMPLOYEE ID = {} has been assigned project with PROJECT ID = {}".format(
                     employeeId, projectId))

    def updateComProject(self):
        projectId = int(self.text6.get())
        date_of_com = (self.text8.get())

        sql = "insert into comp_project values (%s,%s)"
        myCursor.execute(sql, (projectId, date_of_com))
        mydb.commit()

        sql = "delete from ncomp_project where projid = (%s)"
        myCursor.execute(sql, (projectId,))
        mydb.commit()

        ttk.Label(self.frame3, text="DATA HAS BEEN INSERTED", foreground="red").grid(column=1001, row=460)
        showinfo(title="Information", message="Completed project with\nPROJECT ID = {}".format(projectId))

    def updateStatus(self):
        projectId = int(self.text6.get())
        status = (self.text8.get())

        sql = "update ncomp_project set proj_status = (%s) where projid = (%s)"
        myCursor.execute(sql, (status, projectId))
        mydb.commit()

        ttk.Label(self.frame3, text="DATA HAS BEEN UPDATED", foreground="red").grid(column=1001, row=460)
        showinfo(title="Information", message="Updated status of project with PROJECT ID = {}".format(projectId))

    def saveChoice(self):
        regFont = Font(family="Arial",
                       weight="bold",
                       size=10)
        print(self.selected.get())

        if self.selected.get() == '1':
            label6 = ttk.Label(self.frame3, text="Enter PROJECT ID:", font=regFont)
            label6.grid(column=1000, row=455, padx=10, pady=10, sticky=tk.W)

            self.text6 = tk.StringVar()
            widget6 = ttk.Entry(self.frame3, textvariable=self.text6)
            widget6.grid(column=1001, row=455, padx=10, pady=10)

            label8 = ttk.Label(self.frame3, text="Enter DATE OF COMPLETION", font=regFont)
            label8.grid(column=1000, row=457, padx=10, pady=10, sticky=tk.W)

            self.text8 = tk.StringVar()
            widget8 = ttk.Entry(self.frame3, textvariable=self.text8)
            widget8.grid(column=1001, row=457, padx=10, pady=10)

            save2 = ttk.Button(self.frame3, text='Save', command=self.updateComProject)
            save2.grid(column=1001, row=480, padx=10, pady=10, sticky=tk.E)

        elif self.selected.get() == '2':
            label6 = ttk.Label(self.frame3, text="Enter PROJECT ID:", font=regFont)
            label6.grid(column=1000, row=455, padx=10, pady=10, sticky=tk.W)

            self.text6 = tk.StringVar()
            widget6 = ttk.Entry(self.frame3, textvariable=self.text6)
            widget6.grid(column=1001, row=455, padx=10, pady=10)

            label8 = ttk.Label(self.frame3, text="Update Status", font=regFont)
            label8.grid(column=1000, row=457, padx=10, pady=10, sticky=tk.W)

            self.text8 = tk.StringVar()
            widget8 = ttk.Entry(self.frame3, textvariable=self.text8)
            widget8.grid(column=1001, row=457, padx=10, pady=10)

            save2 = ttk.Button(self.frame3, text='Save', command=self.updateStatus)
            save2.grid(column=1001, row=480, padx=10, pady=10, sticky=tk.E)

    def __init__(self, parent):
        super().__init__(parent)

        self.title("Project Details")

        self.geometry("1200x800")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True)

        self.frame1 = ttk.Frame(self.notebook, width=400, height=280)
        self.frame2 = ttk.Frame(self.notebook, width=400, height=280)
        self.frame3 = ttk.Frame(self.notebook, width=400, height=280)

        self.frame1.pack(fill="both", expand=True)
        self.frame2.pack(fill="both", expand=True)
        self.frame3.pack(fill="both", expand=True)

        self.notebook.add(self.frame1, text="New Project")
        self.notebook.add(self.frame2, text="Assign Projects")
        self.notebook.add(self.frame3, text="Update Projects")

        photo = tk.PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\project window 800x800.png")

        image_label = ttk.Label(self.frame1, text="image", image=photo, padding=5)
        image_label.image = photo
        image_label.grid(column=1, row=1, sticky=tk.E, rowspan=800, columnspan=980)


        image_label = ttk.Label(self.frame2, text="image", image=photo, padding=5)
        image_label.image = photo
        image_label.grid(column=1, row=1, sticky=tk.E, rowspan=800, columnspan=980)


        image_label = ttk.Label(self.frame3, text="image", image=photo, padding=5)
        image_label.image = photo
        image_label.grid(column=1, row=1, sticky=tk.E, rowspan=800, columnspan=980)

        regFont = Font(family="Arial",
                       weight="bold",
                       size=10)

        label1 = ttk.Label(self.frame1, text="Project Name:", font=regFont)
        label1.grid(column=1000, row=450, padx=10, pady=10, sticky=tk.W)

        self.text1 = tk.StringVar()
        widget1 = ttk.Entry(self.frame1, textvariable=self.text1)
        widget1.focus()
        widget1.grid(column=1001, row=450, padx=10, pady=10)

        label2 = ttk.Label(self.frame1, text="Start date:", font=regFont)
        label2.grid(column=1000, row=451, padx=10, pady=10, sticky=tk.W)

        self.text2 = tk.StringVar()
        widget2 = ttk.Entry(self.frame1, textvariable=self.text2)
        widget2.grid(column=1001, row=451, padx=10, pady=10)

        label3 = ttk.Label(self.frame2, text="Enter PROJECT ID:", font=regFont)
        label3.grid(column=1000, row=452, padx=10, pady=10, sticky=tk.W)

        self.text3 = tk.StringVar()
        widget3 = ttk.Entry(self.frame2, textvariable=self.text3)
        widget3.grid(column=1001, row=452, padx=10, pady=10)

        label4 = ttk.Label(self.frame2, text="Enter EMPLOYEE ID:", font=regFont)
        label4.grid(column=1000, row=453, padx=10, pady=10, sticky=tk.W)

        self.text4 = tk.StringVar()
        widget4 = ttk.Entry(self.frame2, textvariable=self.text4)
        widget4.grid(column=1001, row=453, padx=10, pady=10)

        label5 = ttk.Label(self.frame2, text="Enter JOINING DATE:", font=regFont)
        label5.grid(column=1000, row=454, padx=10, pady=10, sticky=tk.W)

        self.text5 = tk.StringVar()
        widget5 = ttk.Entry(self.frame2, textvariable=self.text5)
        widget5.grid(column=1001, row=454, padx=10, pady=10)

        self.selected = tk.StringVar()
        r1 = ttk.Radiobutton(self.frame3, text='Add to \"COMPLETED PROJECTS\"', value='1', variable=self.selected)
        r2 = ttk.Radiobutton(self.frame3, text='Update status of \"NOT COMPLETED PROJECTS\"', value='2',
                             variable=self.selected)
        r1.grid(column=1000, row=300, sticky=tk.W)
        r2.grid(column=1000, row=301, sticky=tk.W)
        ttk.Button(self.frame3, text="Enter", command=self.saveChoice).grid(column=1000, row=310)

        # label7 = ttk.Label(frame2, text="Field of work:", font=regFont)
        # label7.grid(column=1000, row=456, padx=10, pady=10, sticky=tk.W)
        #
        # self.text7 = tk.StringVar()
        # widget7 = ttk.Combobox(frame2, textvariable=self.text7)
        # widget7["values"] = ["Engineer", "Salesperson", "Freelancer"]
        # widget7["state"] = "readonly"
        # widget7.grid(column=1001, row=456, padx=10, pady=10)
        #

        #
        # label9 = ttk.Label(frame2, text="Salary/cost per hour:", font=regFont)
        # label9.grid(column=1000, row=458, padx=1, pady=10, sticky=tk.W)
        #
        # self.text9 = tk.StringVar()
        # widget9 = ttk.Entry(frame2, textvariable=self.text9)
        # widget9.grid(column=1001, row=458, padx=10, pady=10)

        save1 = ttk.Button(self.frame1, text='Save', command=self.AddNewProject)
        save1.grid(column=1001, row=480, padx=10, pady=10, sticky=tk.E)
        save2 = ttk.Button(self.frame2, text='Save', command=self.AssignProject)
        save2.grid(column=1001, row=480, padx=10, pady=10, sticky=tk.E)

class ERdiagram (tk.Toplevel):
    def __init__(self,parent):
        super ().__init__(parent)
        self.title ("ER diagram")
        self.geometry ("800x700");

        photo = tk.PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\er diagram 800.png")

        image_label = ttk.Label(self, text="image", image=photo, padding=5)
        image_label.image = photo
        image_label.grid(column=1, row=1, sticky=tk.E, rowspan=800, columnspan=980)


class MainWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('2000x2000')
        self.title('Main Window')

        photo = tk.PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\main window 1800x1700.png")

        image_label = ttk.Label(self, text="image", image=photo, padding=5)
        image_label.image = photo
        image_label.place(x=0, y=0, relwidth=1, relheight=1)

        my_frame = Frame(self)
        my_frame.pack(pady=50)

        mainWindowFont = Font(
            family="Arial",
            size=12,
            weight="bold",
        )

        label1 = ttk.Label(my_frame, font=mainWindowFont,
                           text="Register \"NEW EMPLOYEES\",\nprovide salary,\ngive \"NEW ROLES\"")
        label1.grid(column=0, row=0, padx=20, pady=5, sticky=tk.S)

        label2 = ttk.Label(my_frame, font=mainWindowFont, text="Run complex Queries,\nRetrive custom data")
        label2.grid(column=1, row=0, padx=50, pady=10)

        label3 = ttk.Label(my_frame, font=mainWindowFont, text="Generate online payslip\nof employees")
        label3.grid(column=2, row=0, padx=50, pady=10)

        label4 = ttk.Label(my_frame, font=mainWindowFont,
                           text="\"ADD NEW PROJECTS\"\nAssign \"PROJECTS\" \nto employess and \nrgive update\"STATUS\" ")
        label4.grid(column=3, row=0, padx=50, pady=10)

        label5 = ttk.Label(my_frame, font=mainWindowFont, text="Order Online on\n\"COMPANY_X CANTEEN\"")
        label5.grid(column=4, row=0, padx=50, pady=10)

        label5 = ttk.Label(my_frame, font=mainWindowFont, text="\"ER DIAGRAM\"\n of database")
        label5.grid(column=5, row=0, padx=50, pady=10)

        button1 = ttk.Button(my_frame,
                             text='Register a NEW EMPLOYEE',
                             command=self.open_registration_window)

        button2 = ttk.Button(my_frame,
                             text="Open Query Runner",
                             command=self.open_QueryRunner_window)

        button3 = ttk.Button(my_frame,
                             text="Generate Payslip",
                             command=self.open_generatePayslip_window)

        button4 = ttk.Button(my_frame,
                             text="Add projects",
                             command=self.open_ProjectDetails_window)

        button5 = ttk.Button(my_frame,
                             text="Visit Canteen",
                             command=self.open_canteen_window)

        button6 = ttk.Button(my_frame,
                             text="ER diagram",
                             command=self.open_ER_window)

        button1.grid(column=0, row=1, padx=50)
        button2.grid(column=1, row=1, padx=50)
        button3.grid(column=2, row=1, padx=50)
        button4.grid(column=3, row=1, padx=50)
        button5.grid(column=4, row=1, padx=50)
        button6.grid (column=5, row=1, padx=50)

    def open_registration_window(self):
        window = RegistrationWindow(self)
        window.grab_set()

    def open_QueryRunner_window(self):
        window = QueryRunner(self)
        window.grab_set()

    def open_generatePayslip_window(self):
        window = GeneratePaySlip(self)
        window.grab_set()

    def open_ProjectDetails_window(self):
        window = ProjectDetails(self)
        window.grab_set()

    def open_canteen_window(self):
        print("in main window canteen button")
        window = companyx_canteen(self)
        window.grab_set()

    def open_ER_window(self):
        print("in main window canteen button")
        window =ERdiagram(self)
        window.grab_set()




class App(tk.Tk):
    def checkDetails(self):
        print("checking details")

        sql = "select password from login_details where username = %s"
        myCursor.execute(sql, (self.username.get(),))
        myResult = myCursor.fetchall()

        for i in myResult:
            print(i)
            if (i[0] == ""):
                self.destroy()
            else:
                self.correctPass = i[0]

        print(type(self.correctPass))
        if self.password.get() != self.correctPass:
            self.destroy()
        else:
            window = MainWindow(self)
            window.grab_set()

    def returnKeyPressed(self):
        print("return key pressed")
        self.checkDetails()

    def __init__(self):
        super().__init__()

        self.title("Login")
        self.geometry("1200x800")
        self.resizable(0, 0)

        # self.columnconfigure(0, weight=8)
        # self.columnconfigure(1, weight=1)
        # self.columnconfigure(2,weight = 3)

        # img = Image.open (r"C:\Users\piyush chauhan\Pictures\login page.png")
        # res_img = img.resize ((100,100))
        # photo = tk.PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\wallpaper.png")
        #
        # image_label = ttk.Label(self, text="image", image=photo, padding=5)
        # image_label.image = photo
        # image_label.grid(column=0, row=1, sticky=tk.E, rowspan=800, columnspan=980)

        # ttk.Label(self, text="").grid(column=0, row=1, columnspan=200)
        photo = tk.PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\login page 800x800.png")

        image_label = ttk.Label(self, text="image", image=photo, padding=5)
        image_label.image = photo
        image_label.grid(column=1, row=1, sticky=tk.E, rowspan=800, columnspan=980)

        self.username = tk.StringVar()
        self.password = tk.StringVar()
        loginFont = Font(
            family="STsong",
            size=25,
            weight="bold",
            underline=1
        )
        ttk.Label(self, text="LOGIN DETAILS", font=loginFont).grid(column=1000, row=299, sticky=tk.N, columnspan=10)

        # username
        username_label = ttk.Label(self, text="Username:", font=("Arial", 12))
        username_label.grid(column=1000, row=300, sticky=tk.N, padx=5, pady=10)

        username_entry = ttk.Entry(self, textvariable=self.username)
        username_entry.focus()
        username_entry.grid(column=1001, row=300, sticky=tk.N, padx=5, pady=10)

        # password
        password_label = ttk.Label(self, text="Password:", font=("Arial", 12))
        password_label.grid(column=1000, row=301, sticky=tk.N)

        password_entry = ttk.Entry(self, textvariable=self.password, show="*")
        password_entry.grid(column=1001, row=301, sticky=tk.N)

        # login button
        login_button = ttk.Button(self, text="Login", command=self.returnKeyPressed)
        # login_button.bind ('<Return>', returnKeyPressed)
        login_button.grid(column=1001, row=302, sticky=tk.E, pady=5)


if __name__ == "__main__":
    app = App()
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    app.mainloop()
