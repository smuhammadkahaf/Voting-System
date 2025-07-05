import tkinter as tk
from Includes.RSA import RSA
import math
from tkinter import  ttk
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
    def generate_table(frame_,data,encrypted_fields=[],is_action=False,action=None,action_name=None,field = 'id', hide_columns=[]):
        #is_action means give button or not
        #action means what function do
        #action name is button name
        if not data:
            return ""
        scrollable_frame = Common.get_scroll_bar(frame_)

        row_frame = tk.Frame(scrollable_frame, bg="#252525")
        row_frame.pack(fill="x", pady=2)  # pack vertically stacked rows

        visible_keys = [k for k in data[0].keys() if k not in hide_columns]
        column_count = len(visible_keys) + (1 if is_action else 0)
        width = math.ceil(100 / column_count) - 1

        for heading in visible_keys:
            tk.Label(row_frame, text=heading, font=("Arial", 12), fg="black", bg="#ffffff", width=width).pack(
                side="left", padx=2, pady=2)


        if is_action :
            tk.Label(row_frame, text="Action", font=("Arial", 12), fg="black", bg="#ffffff", width=width).pack(side="left",padx=2, pady=2)
        #current_row = -1
        for row in data:
            #current_row+=1
            # column_count = len(row)
            row_frame = tk.Frame(scrollable_frame, bg="#252525")
            row_frame.pack(fill="x", pady=2)  # pack vertically stacked rows

            # current_column = -1
            for key in visible_keys:
                value = row[key]
                if key in encrypted_fields:
                    value = Common.unlocker(value)
                tk.Label(row_frame, text=value, font=("Arial", 12), fg="black", bg="#ffffff", width=width, height=2).pack(side="left", padx=2, pady=2)
            if is_action:
                login_button=tk.Button(row_frame,text=action_name,font=("Arial", 16),bg="#444",fg="white",width=width-8, command=lambda a=row: action(a[field]))  # action is called on click, not before)
                login_button.pack(side="top", padx=2, pady=2)

    @staticmethod
    def get_scroll_bar(frame_):
        canvas = tk.Canvas(frame_, bg="#252525", highlightthickness=0)
        scrollbar = tk.Scrollbar(frame_, orient="vertical", command=canvas.yview)

        outer_frame = tk.Frame(canvas, bg="#252525")  # NEW: wrapper to center contents
        scrollable_frame = tk.Frame(outer_frame, bg="#252525")  # same as before

        scrollable_frame.pack(anchor="center")  # pack table in center inside wrapper

        canvas.create_window((0, 0), window=outer_frame, anchor="n")  # CENTER wrapper, not raw frame

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        return scrollable_frame  # return only the actual frame where you place widgets

    @staticmethod
    def generate_table2(frame_, data, encrypted_fields=[], is_action=False, action=None, action_name=None, field='id'):
        if not data:
            return ""

            # Setup scrollable Treeview area
        container = tk.Frame(frame_, bg="#252525")
        container.pack(fill="both", expand=True)

        columns = list(data[0].keys())
        if is_action:
            columns.append("Action")

        tree = ttk.Treeview(container, columns=columns, show="headings", height=len(data))
        tree.pack(side="left", fill="both", expand=True)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scrollbar.set)

        # Define column headers
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=120)

        # Insert data rows
        for row in data:
            row_data = []
            for key in data[0].keys():
                value = row[key]
                if key in encrypted_fields:
                    value = Common.unlocker(value)
                row_data.append(value)

            # For Action column, use placeholder — we'll add buttons manually
            if is_action:
                row_data.append("")

            tree.insert("", "end", values=row_data)

        # Attach action buttons after Treeview is rendered
        if is_action and action:
            # This is just for interaction, no actual buttons inside Treeview (not supported)
            def on_select(event):
                selected = tree.focus()
                values = tree.item(selected, 'values')
                if values:
                    action_value = values[columns.index(field)]
                    action(action_value)

            tree.bind("<Double-1>", on_select)  # double-click to trigger action

        return tree  # In case you want to manipulate it later