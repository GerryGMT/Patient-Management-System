import tkinter
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as Tk

# Create a window .
window = tk.Tk()
window.title("                                                                                                                                                                                Patient's Management System :")

# create menubar
Menubar = tk.Menu()
window.config(menu=Menubar)

# Create a filemenu.
Filemenu = tk.Menu(Menubar, tearoff=0)
Filemenu.add_command(label="New Record")
Filemenu.add_separator()
Filemenu.add_command(label="Save As")
Filemenu.add_separator()
Filemenu.add_command(label="Save ")
Filemenu.add_separator()
Filemenu.add_command(label="Print ")
Filemenu.add_separator()
Menubar.add_cascade(label="File", menu=Filemenu)

# Create a EditMenu.
Editmenu = tk.Menu(Menubar, tearoff=0)
Editmenu.add_command(label="Delete")
Editmenu.add_separator()
Editmenu.add_command(label="Update")
Menubar.add_cascade(label="Edit", menu=Editmenu)

# Create a viewmenu.
Viewmenu = tk.Menu(Menubar, tearoff=0)
Viewmenu.add_command(label="Show Database")
Viewmenu.add_separator()
Viewmenu.add_command(label="Show tables")
Menubar.add_cascade(label="View", menu=Viewmenu)

# Create TabControl.
TabControl = ttk.Notebook(window)
Patient = tk.Frame(TabControl)
Teachers = tk.Frame(TabControl)
Parents = tk.Frame(TabControl)
Help = tk.Frame(TabControl)
TabControl.add(Patient, text="Patient")
TabControl.add(Parents, text="Parents")
TabControl.pack(expand=1, fill="both")

# Create a new tab for Patient.
TabControl = ttk.Notebook(Patient)
Patient_Personal_Details_Create = tk.Frame(TabControl, bg="dark blue")
Patient_Personal_Details_Update = tk.Frame(TabControl, bg="dark blue")
Patient_Personal_Details_Delete = tk.Frame(TabControl, bg="dark blue")
Patient_Personal_Details_List = tk.Frame(TabControl, bg="dark blue")
List_of_Patient = tk.Frame(TabControl)
Update_Patient_Record = tk.Frame(TabControl)
TabControl.add(Patient_Personal_Details_Create, text="Create New Patient Record ")
TabControl.add(Patient_Personal_Details_Update,text="Update  Patient Record ")
TabControl.add(Patient_Personal_Details_Delete,text="Delete  Patient Record ")
TabControl.add(List_of_Patient, text="List of Patient ")
TabControl.pack(expand=1, fill="both")

# Create new Record for Patient.
Patient_Personal_Details_Create_Labelframe = tk.LabelFrame(
    Patient_Personal_Details_Create, bg="grey", fg="black", text="                                                  Create New Patient Record")
Patient_Personal_Details_Create_Labelframe.pack(expand=2)
Patient_first_name = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="First Name:", bg="black", fg="white")
Patient_first_name.grid(column=0, row=0, sticky="WE")
Patient_First_name = tk.Entry(
    Patient_Personal_Details_Create_Labelframe, width=50)
Patient_First_name.grid(column=1, row=0)

Patient_Surname = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="Surname:", bg="black", fg="white")
Patient_Surname.grid(column=0, row=2, sticky="WE")
Patient_Surname = tk.Entry(
    Patient_Personal_Details_Create_Labelframe, width=50)
Patient_Surname.grid(column=1, row=2)

# Filling up space.
Patient_ = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="       ", bg="grey")
Patient_.grid(column=0, row=1)

Patient_last_name = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="Last Name:", bg="black", fg="white")
Patient_last_name.grid(column=0, row=6, sticky="WE")
Patient_last_name = tk.Entry(Patient_Personal_Details_Create_Labelframe)
Patient_last_name.grid(column=1, row=6, sticky="WE")

# Filling up space.
Patient_ = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="       ", bg="grey")
Patient_.grid(column=0, row=5)

Patient_gender = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="Gender:", bg="black", fg="white")
Patient_gender.grid(column=0, row=8, sticky="WE")
Patient_Gender = tk.Entry(Patient_Personal_Details_Create_Labelframe)
Patient_Gender.grid(column=1, row=8, sticky="WE")

Patient_Sickness_Medication = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="Sickness and Medication:", bg="black", fg="white")
Patient_Sickness_Medication.grid(column=0, row=10)
Patient_Sickness_Medication = tk.Entry(
    Patient_Personal_Details_Create_Labelframe)
Patient_Sickness_Medication.grid(column=1, row=10, sticky="WE")

# Filling up space.
Patient_ = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="       ", bg="grey")
Patient_.grid(column=0, row=7)

#Filling up space
Patient_=tk.Label(
    Patient_Personal_Details_Create_Labelframe,text="        ",bg="grey")
Patient_.grid(column=0,row=9)

Patient_Create = tk.Button(Patient_Personal_Details_Create_Labelframe,
                           text="Create Record", bg="yellow", fg="dark blue", height=5)
Patient_Create.grid(column=3, row=14, sticky="WE")

# Update Patient Record

Patient_Personal_Details_Create_Labelframe = tk.LabelFrame(
    Patient_Personal_Details_Update, bg="grey", fg="black", text="                                                  Update Patient Record")
Patient_Personal_Details_Create_Labelframe.pack(expand=2)
Patient_first_name = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="First Name:", bg="black", fg="white")
Patient_first_name.grid(column=0, row=0, sticky="WE")
Patient_First_name = tk.Entry(
    Patient_Personal_Details_Create_Labelframe, width=50)
Patient_First_name.grid(column=1, row=0)

Patient_Surname = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="Surname:", bg="black", fg="white")
Patient_Surname.grid(column=0, row=2, sticky="WE")
Patient_Surname = tk.Entry(
    Patient_Personal_Details_Create_Labelframe, width=50)
Patient_Surname.grid(column=1, row=2)

# Filling up space.
Patient_ = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="       ", bg="grey")
Patient_.grid(column=0, row=1)

Patient_Last_Name = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="Last Name:", bg="black", fg="white")
Patient_Last_Name.grid(column=0, row=6, sticky="WE")
Patient_Last_Name = tk.Entry(Patient_Personal_Details_Create_Labelframe)
Patient_Last_Name.grid(column=1, row=6, sticky="WE")

# Filling up space.
Patient_ = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="       ", bg="grey")
Patient_.grid(column=0, row=5)

Patient_gender = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="Gender:", bg="black", fg="white")
Patient_gender.grid(column=0, row=8, sticky="WE")
Patient_Gender = tk.Entry(Patient_Personal_Details_Create_Labelframe)
Patient_Gender.grid(column=1, row=8, sticky="WE")

Patient_Sickness_Medication = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="Sickness and Medication:", bg="black", fg="white")
Patient_Sickness_Medication.grid(column=0, row=10)
Patient_Sickness_Medication = tk.Entry(
    Patient_Personal_Details_Create_Labelframe)
Patient_Sickness_Medication.grid(column=1, row=10, sticky="WE")

# Filling up space.
Patient_ = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="       ", bg="grey")
Patient_.grid(column=0, row=7)

#Filling up space
Patient_=tk.Label(
    Patient_Personal_Details_Create_Labelframe,text="        ",bg="grey")
Patient_.grid(column=0,row=9)



Patient_Create = tk.Button(Patient_Personal_Details_Create_Labelframe,
                           text="Update Record", bg="yellow", fg="blue", height=5)
Patient_Create.grid(column=3, row=14, sticky="WE")

# Delete Patient Record.
Patient_Personal_Details_Create_Labelframe = tk.LabelFrame(
    Patient_Personal_Details_Delete, bg="grey", fg="black", text="                                                  Delete Patient Record")
Patient_Personal_Details_Create_Labelframe.pack(expand=2)
Patient_first_name = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="First Name:", bg="black", fg="white")
Patient_first_name.grid(column=0, row=0, sticky="WE")
Patient_First_name = tk.Entry(
    Patient_Personal_Details_Create_Labelframe, width=50)
Patient_First_name.grid(column=1, row=0)
Patient_ = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="       ", bg="grey")
Patient_.grid(column=0, row=1)
Patient_Surname = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="Surname:", bg="black", fg="white")
Patient_Surname.grid(column=0, row=2, sticky="WE")
Patient_Surname = tk.Entry(
    Patient_Personal_Details_Create_Labelframe, width=50)
Patient_Surname.grid(column=1, row=2)

# Filling up space.
Patient_ = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="       ", bg="grey")
Patient_.grid(column=0, row=3)
Patient_Last_Name = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="Last Name:", bg="black", fg="white")
Patient_Last_Name.grid(column=0, row=4, sticky="WE")
Patient_Last_Name = tk.Entry(Patient_Personal_Details_Create_Labelframe)
Patient_Last_Name.grid(column=1, row=4, sticky="WE")

# Filling up space.
Patient_ = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="       ", bg="grey")
Patient_.grid(column=0, row=5)

Patient_gender = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="Gender:", bg="black", fg="white")
Patient_gender.grid(column=0, row=6, sticky="WE")
Patient_Gender = tk.Entry(Patient_Personal_Details_Create_Labelframe)
Patient_Gender.grid(column=1, row=6, sticky="WE")

Patient_Sickness_Medication = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="Sickness and Medication:", bg="black", fg="white")
Patient_Sickness_Medication.grid(column=0, row=8)
Patient_Sickness_Medication = tk.Entry(
    Patient_Personal_Details_Create_Labelframe)
Patient_Sickness_Medication.grid(column=1, row=8, sticky="WE")

# Filling up space.
Patient_ = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="       ", bg="grey")
Patient_.grid(column=0, row=7)

#Filling up space
Patient_=tk.Label(
    Patient_Personal_Details_Create_Labelframe,text="        ",bg="grey")
Patient_.grid(column=0,row=9)

Patient_Create = tk.Button(Patient_Personal_Details_Create_Labelframe,
                           text="Update Record", bg="yellow", fg="blue", height=5)
Patient_Create.grid(column=3, row=13, sticky="WE")

#List of Patient.
Patient_Personal_Details_Create_Labelframe = tk.LabelFrame(
List_of_Patient, bg="dark blue", fg="white", text="       ")
Patient_Personal_Details_Create_Labelframe.pack(expand=1, fill="both")
Patient_Sickness_Medication = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="List of Patient Record", bg="grey", fg="black")
Patient_Sickness_Medication.grid(column=0, row=0)
Patient_Parent_Sickness_Medication = tk.Entry(
    Patient_Personal_Details_Create_Labelframe)
Patient_Sickness_Medication.grid(column=0, row=0, sticky="WE")
Patient_Create = tk.Button(Patient_Personal_Details_Create_Labelframe,
                            text="Search", bg="brown", fg="white", height=3)
Patient_Create.grid(column=0, row=2, sticky="WE")

# Filling up space.
Patient_ = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="       ", bg="dark blue")
Patient_.grid(column=0, row=3)

Patient_list = tk.scrolledtext.ScrolledText(Patient_Personal_Details_Create_Labelframe, width=150)
Patient_list.grid(column=0, row=3)

# Filling up space.
Patient_ = tk.Label(
    Patient_Personal_Details_Create_Labelframe, text="       ", bg="dark blue")
Patient_.grid(column=0, row=7)

Patient_Create = tk.Button(Patient_Personal_Details_Create_Labelframe,
                            text="List Patient Record", bg="brown", fg="white", height=3)
Patient_Create.grid(column=0, row=8, sticky="WE")

# Create a new tab for Parents.
TabControl = ttk.Notebook(Parents)
Parents_Personal_Details_Create = tk.Frame(TabControl, bg="brown")
Parents_Personal_Details_Update = tk.Frame(TabControl, bg="brown")
Parents_Personal_Details_Delete = tk.Frame(TabControl, bg="brown")
Parents_Fee_Payment = tk.Frame(TabControl)
List_of_Parents = tk.Frame(TabControl)
Update_Parent_Record = tk.Frame(TabControl)
TabControl.add(Parents_Personal_Details_Create, text="Create New Parents Record ")
TabControl.add(Parents_Personal_Details_Update,text="Update  Parents Record ")
TabControl.add(List_of_Parents, text="List of Parents ")
TabControl.pack(expand=1, fill="both")

#create new parents Record
Parents_Personal_Details_Create_Labelframe = tk.LabelFrame(
    Parents_Personal_Details_Create, bg="grey", fg="black", text="                                                  Create New Parent Record")
Parents_Personal_Details_Create_Labelframe.pack(expand=1)
Parent_first_name = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="First Name:", bg="black", fg="white")
Parent_first_name.grid(column=0, row=0, sticky="WE")
Parent_First_name = tk.Entry(
    Parents_Personal_Details_Create_Labelframe, width=50)
Parent_First_name.grid(column=1, row=0)

Parent_Surname = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Surname:", bg="black", fg="white")
Parent_Surname.grid(column=0, row=2, sticky="WE")
Parent_Surname = tk.Entry(
    Parents_Personal_Details_Create_Labelframe, width=50)
Parent_Surname.grid(column=1, row=2)

# Filling up space.
Parent_ = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="grey")
Parent_.grid(column=0, row=1)

Parent_Last_Name = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Last Name:", bg="black", fg="white")
Parent_Last_Name.grid(column=0, row=4, sticky="WE")
Parent_Last_Name = tk.Entry(Parents_Personal_Details_Create_Labelframe)
Parent_Last_Name.grid(column=1, row=4, sticky="WE")

# Filling up space.
Parent_ = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="grey")
Parent_.grid(column=0, row=3)

Parent_gender = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Gender:", bg="black", fg="white")
Parent_gender.grid(column=0, row=6, sticky="WE")
Parent_Gender = tk.Entry(Parents_Personal_Details_Create_Labelframe)
Parent_Gender.grid(column=1, row=6, sticky="WE")

Parents_parent_Phone_Number = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Phone Number:", bg="black", fg="white")
Parents_parent_Phone_Number.grid(column=0, row=8)
Parents_Parent_Phone_Number = tk.Entry(
    Parents_Personal_Details_Create_Labelframe)
Parents_Parent_Phone_Number.grid(column=1, row=8, sticky="WE")

#Filling up space.
Parent_ = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="grey")
Parent_.grid(column=0, row=5)

Parent_location= tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Location:", bg="black", fg="white")
Parent_location.grid(column=0, row=10, sticky="WE")
Parent_Location = tk.Entry(Parents_Personal_Details_Create_Labelframe)
Parent_Location.grid(column=1, row=10, sticky="WE")

#Filling up space
Parent_=tk.Label(
    Parents_Personal_Details_Create_Labelframe,text="          ",bg="grey")
Parent_.grid(column=0,row=7)
Parent_=tk.Label(
    Parents_Personal_Details_Create_Labelframe,text="          ",bg="grey")
Parent_.grid(column=0,row=9)

Parent_Create = tk.Button(Parents_Personal_Details_Create_Labelframe,
                           text="Create Record", bg="yellow", fg="blue", height=5)
Parent_Create.grid(column=3, row=13, sticky="WE")


# Update Parents Record.
Parents_Personal_Details_Create_Labelframe = tk.LabelFrame(
    Parents_Personal_Details_Update, bg="grey", fg="black", text="                                                  Update Parents Record")
Parents_Personal_Details_Create_Labelframe.pack(expand=1)
Parents_first_name = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="First Name:", bg="black", fg="white")
Parents_first_name.grid(column=0, row=0, sticky="WE")
Parents_First_name = tk.Entry(
    Parents_Personal_Details_Create_Labelframe, width=50)
Parents_First_name.grid(column=1, row=0)

Parents_Surname = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Surname:", bg="black", fg="white")
Parents_Surname.grid(column=0, row=2, sticky="WE")
Parents_Surname = tk.Entry(
    Parents_Personal_Details_Create_Labelframe, width=50)
Parents_Surname.grid(column=1, row=2)

# Filling up space.
Parents_ = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="grey")
Parents_.grid(column=0, row=1)

Parents_Last_Name = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Last Name:", bg="black", fg="white")
Parents_Last_Name.grid(column=0, row=4, sticky="WE")
Parents_Last_Name = tk.Entry(Parents_Personal_Details_Create_Labelframe)
Parents_Last_Name.grid(column=1, row=4, sticky="WE")

# Filling up space.
Parents_ = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="grey")
Parents_.grid(column=0, row=3)
Parents_ = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="grey")
Parents_.grid(column=0, row=5)

Parents_gender = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Gender:", bg="black", fg="white")
Parents_gender.grid(column=0, row=6, sticky="WE")
Parents_Gender = tk.Entry(Parents_Personal_Details_Create_Labelframe)
Parents_Gender.grid(column=1, row=6, sticky="WE")

Parents_Phone_Number = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Phone Number:", bg="black", fg="white")
Parents_Phone_Number.grid(column=0, row=8)
Parents_Phone_Number = tk.Entry(
    Parents_Personal_Details_Create_Labelframe)
Parents_Phone_Number.grid(column=1, row=8, sticky="WE")

# Filling up space.
Parents_ = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="grey")
Parents_.grid(column=0, row=7)

Parent_location= tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Location:", bg="black", fg="white")
Parent_location.grid(column=0, row=10, sticky="WE")
Parent_Location = tk.Entry(Parents_Personal_Details_Create_Labelframe)
Parent_Location.grid(column=1, row=10, sticky="WE")

#Filling up space
Parents_=tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="grey")
Parents_.grid(column=0, row=9)

Parents_Create = tk.Button(Parents_Personal_Details_Create_Labelframe,
                            text="Update Record", bg="yellow", fg="blue", height=5)
Parents_Create.grid(column=3, row=13, sticky="WE")

#List of Parents.
Parents_Personal_Details_Create_Labelframe = tk.LabelFrame(
List_of_Parents, bg="brown", fg="white", text="      ")
Parents_Personal_Details_Create_Labelframe.pack(expand=1, fill="both")
Parents_Phone_Number = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="List of  Parents Record", bg="grey", fg="black")
Parents_Phone_Number.grid(column=0, row=0)
Parents_Parent_Phone_Number = tk.Entry(
    Parents_Personal_Details_Create_Labelframe)
Parents_Parent_Phone_Number.grid(column=1, row=0, sticky="WE")
Parents_Create = tk.Button(Parents_Personal_Details_Create_Labelframe,
                            text="Search", bg="dark blue", fg="white", height=3)
Parents_Create.grid(column=0, row=2, sticky="WE")

# Filling up space.
Parents_ = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="brown")
Parents_.grid(column=0, row=3)

Parents_list = tk.scrolledtext.ScrolledText(Parents_Personal_Details_Create_Labelframe, width=150)
Parents_list.grid(column=0, row=3)

# Filling up space.
Parents_ = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="brown")
Parents_.grid(column=0, row=7)

Parents_Create = tk.Button(Parents_Personal_Details_Create_Labelframe,
                            text="List Parents Record", bg="yellow", fg="blue", height=3)
Parents_Create.grid(column=0, row=8, sticky="WE")


window.mainloop()
