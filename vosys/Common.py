import tkinter as tk
from RSA import RSA
import math
class Common:
    #variables

    #functions
    @staticmethod
    def new_label(frame_ , text_, font_):
        return tk.Label(
            frame_,
            text=text_,
            font=("Arial", font_, "bold"),  # increased font size
            fg="white",
            bg="#252525"
        )
    @staticmethod
    def new_button(frame_,text_,command_=None):
        return tk.Button(
            frame_,
            text=text_,
            font=("Arial", 16),
            bg="#444",
            fg="white",
            width=15,
            command=command_
        )
    @staticmethod
    def new_radio_button(frame,text,variable,):
        return tk.Radiobutton(
        frame,
        text=text,
        variable=variable,
        value=text,
        font=("Arial", 14),
        bg="#252525",
        fg="white",
        selectcolor="#252525",  # to blend in background
        activebackground="#252525"
        )
    @staticmethod
    def clear_content(frame):
        for widget in frame.winfo_children():
            widget.destroy()
    @staticmethod
    def locker(msg):
        locker = RSA()
        locker.set_msg(msg)
        locker.encrypt_msg()
        return locker.get_msg()

    @staticmethod
    def unlocker(msg):
        unlocker = RSA()
        unlocker.set_msg(msg)
        unlocker.decrypt_msg()
        return unlocker.get_msg()

    @staticmethod
    def generate_table(frame_,data,encrypted_fields=[],is_action=False,action=None,action_name=None):
        row_frame = tk.Frame(frame_, bg="#252525")
        row_frame.pack(fill="x", pady=2)  # pack vertically stacked rows
        column_count = len(data[0])
        column_count = column_count + 1 if is_action else column_count
        width = math.ceil(100 / column_count)
        for heading, value_data in data[0].items():
            tk.Label(row_frame, text=heading, font=("Arial", 12), fg="black", bg="#ffffff", width=width).pack(side="left",padx=2, pady=2)
        if is_action :
            tk.Label(row_frame, text="Action", font=("Arial", 12), fg="black", bg="#ffffff", width=width).pack(side="left",padx=2, pady=2)
        #current_row = -1
        for row in data:
            #current_row+=1
            # column_count = len(row)
            row_frame = tk.Frame(frame_, bg="#252525")
            row_frame.pack(fill="x", pady=2)  # pack vertically stacked rows

            # current_column = -1
            for key, value in row.items():
                # current_column+=1
                if key in encrypted_fields :
                    value = Common.unlocker(value)
                tk.Label(row_frame, text=value, font=("Arial", 12), fg="black", bg="#ffffff",width=width).pack(side="left", padx=2, pady=2)
            if is_action:
                login_button=tk.Button(row_frame,text=action_name,font=("Arial", 16),bg="#444",fg="white",width=15, command=lambda a=row: action(a['admin_id']))  # action is called on click, not before)
                login_button.pack(side="left", padx=2, pady=2)