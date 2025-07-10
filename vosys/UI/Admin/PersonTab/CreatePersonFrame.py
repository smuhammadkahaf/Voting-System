import tkinter as tk

from Logic.Admin.Person import Person
from Logic.Admin.Category import Category
from Includes.TOTP import MyTOTP

from Includes.Common import Common
from Logic.Admin.Person import Person

class CreatePersonFrame(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent,bg="#EAEAEA")
        self.parent = parent
        self.buildUI()


    def buildUI(self):
        title = tk.Frame(self.parent, bg="#EAEAEA")
        title.pack(pady=(50, 0))  # slightly space from top
        title_label = Common.new_label(title, "Create Person", 30)
        title_label.pack()

        warning = tk.Frame(self.parent, bg="#EAEAEA")
        warning.pack()

        self.warning_label = Common.new_label(warning, "", 16)
        self.warning_label.pack(pady=(15,30))

        center_frame = Common.get_scroll_bar(self.parent)

        self.qr_frame = tk.Frame(center_frame, bg="#EAEAEA")
        self.qr_frame.grid(row=0, column=0,padx=(0,80) ,pady=(0,30))


        #name input
        name_label = Common.new_label(center_frame, "name*", 16)
        name_label.grid(row=1, column=0, sticky="w", pady=(0, 5),padx=(60,0))
        self.name_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=25  # wider input
        )
        self.name_entry.grid(row=2, column=0, pady=(0, 15),padx=(60,0))

        #CNIC input
        cnic_label = Common.new_label(center_frame, "CNIC* (no dashes)", 16)
        cnic_label.grid(row=1, column=1, sticky="w", pady=(0, 5),padx=(60,0))
        self.cnic_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=25  # wider input
        )
        self.cnic_entry.grid(row=2, column=1, pady=(0, 15),padx=(60,0))

        #DOB Input
        DOB_label = Common.new_label(center_frame, "Date of Birth* (YYYY-MM-DD)", 16)
        DOB_label.grid(row=3, column=0, sticky="w", pady=(0, 5),padx=(60,0))
        self.DOB_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=25
        )
        self.DOB_entry.grid(row=4, column=0, pady=(0, 15),padx=(60,0))

        #Phone number
        phone_label = Common.new_label(center_frame, "Phone Number", 16)
        phone_label.grid(row=3, column=1, sticky="w", pady=(0, 5),padx=(60,0))
        self.phone_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=25
        )
        self.phone_entry.grid(row=4, column=1, pady=(0, 15),padx=(60,0))

        #Email Input
        email_label = Common.new_label(center_frame, "Email Address", 16)
        email_label.grid(row=5, column=0, sticky="w", pady=(0, 5),padx=(60,0))
        self.email_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=25
        )
        self.email_entry.grid(row=6, column=0, pady=(0, 15),padx=(60,0))

        # Dynamic Category Checkboxes
        options_frame = tk.Frame(center_frame, bg="#EAEAEA")
        options_frame.grid(row=7, column=0, sticky="w")

        category_heading = Common.new_label(options_frame,"Available Categories",16)
        category_heading.pack(anchor="w",padx=(60,0))

        category_object = Category()
        categories = category_object.get_categories_list()  # e.g., ['Student', 'Teacher']

        self.category_vars = {}
        for index, category_name in enumerate(categories):
            var = tk.BooleanVar()
            checkbox = tk.Checkbutton(
                options_frame,
                text=category_name,
                variable=var,
                bg="#EAEAEA",
                fg="#2e3e55",
                font=("Arial", 14),
                selectcolor="#EAEAEA"
            )
            checkbox.pack(anchor='w',padx=(60,0))
            self.category_vars[category_name] = var


        # create Button - larger font and width, aligned right
        create_person_button = Common.new_button(center_frame, "Create",self.create_person_button_clicked)
        create_person_button.grid(row=8, column=1, sticky="e",padx=(60,0),pady=(0,30))

    def create_person_button_clicked(self):
        name = self.name_entry.get()
        CNIC = self.cnic_entry.get()
        date_of_birth = self.DOB_entry.get()
        phone_number = self.phone_entry.get()
        email_address = self.email_entry.get()

        if not name or not CNIC or not date_of_birth or not phone_number or not email_address:
            self.warning_label.config(text="All Fields are required",fg="red")

        elif " " in CNIC or "-" in CNIC :
            self.warning_label.config(text="CNIC should not contain dashes and white spaces", fg="red")
        elif (len(CNIC)!=13):
            self.warning_label.config(text="CNIC should not contain more than 13 numbers", fg="red")

        elif not CNIC.isdigit():
            self.warning_label.config(text= "cnic must be digit")
            return

        elif self.is_valid_date_format(date_of_birth) == False:
            self.warning_label.config(text = "Please check date format",fg = "red")
        else:
            self.otp = MyTOTP()
            key = self.otp.setup_new_key(name,self.qr_frame)
            response = self.new_person(name, CNIC, date_of_birth, phone_number, email_address,key)
            self.warning_label.config(text = "Person registered successfully",fg="green")
            if response == 0:
                self.add_person_in_class(CNIC)



    def new_person(self,name, CNIC, date_of_birth, phone_number, email_address,key):
        person = Person()
        result = person.create_person(name, CNIC, date_of_birth, phone_number, email_address,key)

        if result == 0:
            self.warning_label.config(text="CNIC already in registered", fg="red")
            return -1
        elif result == 1:
            self.warning_label.config(text="email already registered", fg="red")
            return -1
        return 0

    def add_person_in_class(self,cnic):
        category_object  = Category()
        person_object = Person()
        person_id = person_object.get_person_id(cnic)

        categories = category_object.get_categories_list()

        add_in = []
        for category_name in categories:
            variable = self.category_vars[category_name]
            checked = variable.get()
            if checked:
                add_in.append(category_name)
        categories_id = category_object.get_categories_id(add_in)
        person_object.add_person_in_class(person_id,categories_id)


    def is_valid_date_format(self,date):
        # Check total length
        if len(date) != 10:
            return False

        # Check hyphens at correct positions
        if date[4] != '-' or date[7] != '-':
            return False

        # Check digits and extract year, month, day
        year_str = date[0:4]
        month_str = date[5:7]
        day_str = date[8:10]
        if not (year_str.isdigit() and month_str.isdigit() and day_str.isdigit()):
            return False
        year = int(year_str)
        month = int(month_str)
        day = int(day_str)

        # Validate ranges
        if not (1 <= month <= 12):
            return False
        if not (1 <= day <= 31):
            return False
        return True