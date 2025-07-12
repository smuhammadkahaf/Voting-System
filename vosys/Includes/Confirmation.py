import tkinter as tk
from Includes.Common import Common

class Confirmation(tk.Toplevel):
    def __init__(self, parent, message="Are you sure?"):
        super().__init__(parent)
        self.result = None
        self.title("Confirmation")
        self.geometry("300x150")
        self.configure(bg="#EAEAEA")
        self.resizable(False, False)
        self.grab_set()  # Focus lock

        # Window size
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()



        # Set window size as a percentage of screen
        width = int(screen_width * 0.3)   # 30% of screen width
        height = int(screen_height * 0.2)  # 20% of screen height

        # Center position
        pos_x = (screen_width - width) // 2
        pos_y = (screen_height - height) // 2
        self.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
        self.transient(parent)

        label = tk.Label(self, text=message, font=("Times", 17), fg="#2e3e55", bg="#EAEAEA")
        label.pack(pady=(30, 10))

        button_frame = tk.Frame(self, bg="#EAEAEA")
        button_frame.pack()

        yes_button = Common.new_button(button_frame,"Yes",lambda: (self._set_result(1)),16,10)
        # yes_button = tk.Button(button_frame, text="Yes", width=10, command=lambda: self._set_result(1))
        yes_button.pack(side="left", padx=10)

        no_button = Common.new_button(button_frame,"N0",lambda: (self._set_result(1)),16,10)
        no_button.pack(side="left", padx=10)

    def _set_result(self, value):
        self.result = value
        self.destroy()

    @classmethod
    def ask(cls, parent, message="Are you sure?"):
        dialog = cls(parent, message)
        parent.wait_window(dialog)
        return dialog.result
