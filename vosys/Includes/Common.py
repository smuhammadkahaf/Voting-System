import tkinter as tk
from Includes.RSA import RSA
import math
from tkinter import  ttk
class Common:

    """
    background color         = #EAEAEA
    Label text color         = #2e3e55
    button color             = #3498db
    button Hover color       = #2980b9
    tab bar color            = #395472
    tab hover color          = #2c3e50
    tab selected color       = #3498db
    card background          = #bde4ff
    """

    background_color = "#EAEAEA"
    label_text_color = "#2e3e55"
    button_color= "#3498db"
    button_hover_color = "#2980b9"
    tab_bar_color = "#395472"
    tab_hover_color ="#2c3e50"
    tab_selected_color = "#3498db"
    card_background =  "#bde4ff"





    #functions
    @staticmethod
    def new_label(frame_ , text_, font_):
        return tk.Label(
            frame_,
            text=text_,
            font=("Times", font_, "bold"),  # increased font size
            fg="#2e3e55",
            bg="#EAEAEA"
        )
    @staticmethod
    def on_enter_buttons(e):
        e.widget.config(bg="#2980b9")

    @staticmethod
    def on_leave_buttons(e):
        e.widget.config(bg="#3498db")

    @staticmethod
    def on_enter_tabs(e):
        current_color = e.widget.cget("bg").lower()
        if current_color in ("#3498db", "#2980b9"):  # If selected or selected-hover
            e.widget.config(bg="#2980b9")  # Hover on selected
        else:
            e.widget.config(bg="#2c3e50")  # Hover on default

    @staticmethod
    def on_leave_tabs(e):
        current_color = e.widget.cget("bg").lower()
        if current_color in ("#3498db", "#2980b9",):  # Leaving selected-hover
            e.widget.config(bg="#3498db")  # Back to selected color
        else:
            e.widget.config(bg="#395472")  # Back to default

    @staticmethod
    def new_button(frame_,text_,command_=None,size=16,width =15):
        btn = tk.Button(
            frame_,
            text=text_,
            font=("Times", size),
            bg="#3498db",
            fg="white",
            width=width,
            command=command_,
            cursor="hand2"
        )
        btn.bind("<Enter>", Common.on_enter_buttons)
        btn.bind("<Leave>", Common.on_leave_buttons)
        return btn

    @staticmethod
    def new_tab(frame_,text_,command_=None,size=16,width =9):
        btn = tk.Button(
            frame_,
            text=text_,
            font=("Times", size),
            bg="#395472",
            fg="white",
            height = 2,
            width=width,
            command=command_,
            cursor="hand2",
            bd = 0
        )
        btn.bind("<Enter>", Common.on_enter_tabs)
        btn.bind("<Leave>", Common.on_leave_tabs)
        return btn

    @staticmethod
    def new_radio_button(frame,text,variable,):
        return tk.Radiobutton(
        frame,
        text=text,
        variable=variable,
        value=text,
        font=("Arial", 14,"bold"),
        bg="#EAEAEA",
        fg="#2e3e55",
        selectcolor="#EAEAEA",  # to blend in background
        activebackground="#EAEAEA"
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

        row_frame = tk.Frame(scrollable_frame, bg="#EAEAEA")
        row_frame.pack(fill="x", pady=2,padx=(15,0))  # pack vertically stacked rows

        visible_keys = [k for k in data[0].keys() if k not in hide_columns]
        column_count = len(visible_keys) + (1 if is_action else 0)
        width = math.ceil(100 / column_count) - 1

        for heading in visible_keys:
            heading = heading.replace("_"," ")

            tk.Label(row_frame, text=heading, font=("Times", 12), fg="black", bg="#ffffff", width=width,bd=2,relief="solid").pack(
                side="left", padx=2, pady=2)


        if is_action :
            tk.Label(row_frame, text="Action", font=("Times", 12), fg="black",  bg="#ffffff", width=width,bd=2,relief="solid").pack(side="left",padx=2, pady=2)
        #current_row = -1
        for row in data:
            #current_row+=1
            # column_count = len(row)
            row_frame = tk.Frame(scrollable_frame, bg="#EAEAEA")
            row_frame.pack(fill="x", pady=2,padx=(15,0))  # pack vertically stacked rows

            # current_column = -1
            for key in visible_keys:
                value = row[key]
                if key in encrypted_fields:
                    value = Common.unlocker(value)
                tk.Label(row_frame, text=value, font=("Times", 12), fg="black", bg="#ffffff", width=width, height=2,bd=2,relief="solid").pack(side="left", padx=2, pady=2)
            if is_action:
                login_button=Common.new_button(row_frame,text_=action_name, command_=lambda a=row: action(a[field]),size = 16,width=width-8)  # action is called on click, not before)
                login_button.pack(side="top", padx=2, pady=2)
    @staticmethod
    def get_scroll_bar(frame_):
        canvas = tk.Canvas(frame_, bg="#EAEAEA", highlightthickness=0)
        scrollbar = tk.Scrollbar(frame_, orient="vertical", command=canvas.yview,bg="red")

        outer_frame = tk.Frame(canvas, bg="#EAEAEA")  # NEW: wrapper to center contents
        scrollable_frame = tk.Frame(outer_frame, bg="#EAEAEA")  # same as before

        scrollable_frame.pack(anchor="center")  # pack table in center inside wrapper

        canvas.create_window((0, 0), window=outer_frame, anchor="n")  # CENTER wrapper, not raw frame

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


        def _on_mousewheel(event):
            # delta is positive or negative based on scroll direction
            move = -1 * int(event.delta / 120)

            # Get the current scroll fraction (top and bottom)
            first, last = canvas.yview()

            # Only scroll if not already at the top or bottom
            if not (move < 0 and first <= 0) and not (move > 0 and last >= 1):
                canvas.yview_scroll(move, "units")

        def _bind_mousewheel(event):
            canvas.bind("<MouseWheel>", _on_mousewheel)

        def _unbind_mousewheel(event):
            canvas.unbind("<MouseWheel>")

        # Bind when mouse enters/leaves the canvas
        canvas.bind("<Enter>", _bind_mousewheel)
        canvas.bind("<Leave>", _unbind_mousewheel)

        return scrollable_frame  # return only the actual frame where you place widgets


