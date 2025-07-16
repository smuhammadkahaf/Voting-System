import tkinter as tk
from Includes.Common import Common
from Logic.Admin.Person import  Person
from Logic.Admin.Category import Category
from Includes.TOTP import MyTOTP

class updatePersonFrame(tk.Frame):
    def __init__(self, parent,id):
        super().__init__(parent, bg="#EAEAEA")
        self.id = id
        self.parent = parent
        self.user = Person()
        data = self.user.get_person(id)
        self.name = Common.unlocker(data["name"])
        self.cnic = Common.unlocker((data["cnic"]))
        self.date_of_birth = data["date_of_birth"]
        self.phone_number = Common.unlocker((data["phone_number"]))
        self.email = Common.unlocker((data["email"]))
        self.key = Common.unlocker((data["key_"]))
        print(self.key)
        self.safe = MyTOTP()


        self.buildUI()

    def buildUI(self):
        title = tk.Frame(self.parent, bg="#EAEAEA")
        title.pack(pady=(50, 10))  # slightly space from top
        title_label = Common.new_label(title, "Edit Person", 30)
        title_label.pack()

        warning = tk.Frame(self.parent, bg="#EAEAEA")
        warning.pack()
        self.warning_label = Common.new_label(warning, "", 16)
        self.warning_label.pack(pady=(15, 0))

        center_frame = Common.get_scroll_bar(self.parent)

        self.qr_frame = tk.Frame(center_frame, bg="#EAEAEA")
        self.qr_frame.grid(row=0, column=0, padx=(0, 80), pady=(0, 30))
        self.safe.setup_old_key(self.key,self.name,self.qr_frame)

        new_key_button = Common.new_button(center_frame,"New Key",self.new_key_button_pressed)
        new_key_button.grid(row=0,column=1)
        # name input
        name_label = Common.new_label(center_frame, "name*", 16)
        name_label.grid(row=1, column=0, sticky="w", pady=(0, 5), padx=(60, 0))
        self.name_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=25  # wider input
        )
        self.name_entry.grid(row=2, column=0, pady=(0, 15), padx=(60, 0))
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, self.name)
        self.name_entry.config(state="readonly")

        #CNIC input
        cnic_label = Common.new_label(center_frame, "CNIC* (no dashes)", 16)
        cnic_label.grid(row=1, column=1, sticky="w", pady=(0, 5),padx=(60,0))
        self.cnic_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=25  # wider input
        )
        self.cnic_entry.grid(row=2, column=1, pady=(0, 15),padx=(60,0))
        self.cnic_entry.delete(0, tk.END)
        self.cnic_entry.insert(0, self.cnic)
        self.cnic_entry.config(state="readonly")

        # DOB Input
        DOB_label = Common.new_label(center_frame, "Date of Birth* (YYYY-MM-DD)", 16)
        DOB_label.grid(row=3, column=0, sticky="w", pady=(0, 5), padx=(60, 0))
        self.DOB_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=25
        )
        self.DOB_entry.grid(row=4, column=0, pady=(0, 15), padx=(60, 0))
        self.DOB_entry.delete(0, tk.END)
        self.DOB_entry.insert(0, self.date_of_birth)
        self.DOB_entry.config(state="readonly")

        # Phone number
        phone_label = Common.new_label(center_frame, "Phone Number", 16)
        phone_label.grid(row=3, column=1, sticky="w", pady=(0, 5), padx=(60, 0))
        self.phone_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=25
        )
        self.phone_entry.grid(row=4, column=1, pady=(0, 15), padx=(60, 0))
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, self.phone_number)

        # Email Input
        email_label = Common.new_label(center_frame, "Email Address", 16)
        email_label.grid(row=5, column=0, sticky="w", pady=(0, 5), padx=(60, 0))
        self.email_entry = tk.Entry(
            center_frame,
            font=("Arial", 16),
            width=25
        )
        self.email_entry.grid(row=6, column=0, pady=(0, 15), padx=(60, 0))
        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, self.email)

        #adding check boxes
        options_frame = tk.Frame(center_frame, bg="#EAEAEA")
        options_frame.grid(row=7, column=0, sticky="w")

        category_object = Category()
        categories = category_object.get_categories_list()  # All categories
        in_categories = self.user.person_in_categories(self.id)  # Categories person is already registered in

        self.category_vars = {}
        for category_name in categories:
            var = tk.BooleanVar(value=category_name in in_categories)
            checkbox = tk.Checkbutton(
                options_frame,
                text=category_name,
                variable=var,
                bg="#EAEAEA",
                fg="#2e3e55",
                font=("Arial", 14),
                selectcolor="#EAEAEA"
            )
            checkbox.pack(anchor='w', padx=(60, 0))
            self.category_vars[category_name] = var
            update_person_button = Common.new_button(center_frame, "Update", self.update_person_button_clicked)
            update_person_button.grid(row=7, column=1, sticky="e", padx=(60, 0))


    def update_person_button_clicked(self):

        CNIC = self.cnic_entry.get()
        phone_number = self.phone_entry.get()
        email_address = self.email_entry.get()

        if not phone_number or not email_address:
            self.warning_label.config(text="All Fields are required", fg="red")

        else:
            print(CNIC)
            condition  = f"cnic = '{Common.locker(CNIC)}'"
            data = {
                "phone_number": Common.locker(phone_number),
                "email": Common.locker(email_address)
            }
            response = self.user.update_person(data,condition)
            if response == -1:
                self.warning_label.config(text = "email already registered",fg="red")
                return

        self.add_person_in_class(self.cnic)
        self.warning_label.config(text = "Person Details Updated Successfully",fg = "green")

    def add_person_in_class(self,cnic):
        category_object  = Category()
        person_object = Person()
        person_id = person_object.get_person_id(cnic)
        print(person_id)
        categories = category_object.get_categories_list()
        print(categories)
        add_in = []
        for category_name in categories:
            variable = self.category_vars[category_name]
            checked = variable.get()
            if checked:
                add_in.append(category_name)
        print(add_in)
        categories_id = category_object.get_categories_id(add_in)
        print(categories_id)
        person_object.add_person_in_class(person_id,categories_id)

    def new_key_button_pressed(self):
        Common.clear_content(self.qr_frame)
        self.key = self.safe.setup_new_key(self.name,self.qr_frame)
        print(self.key)
        self.key = Common.locker(self.key)
        data = {
            "key_": self.key,
        }
        condition = "id = " + str(self.id)
        self.user.db.update("users",data,condition)
        self.warning_label.config(text="Key Updated Successfully",fg = "green")


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