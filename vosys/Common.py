import tkinter as tk
from RSA import RSA

class Common:
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
    def new_button(frame_,text_,command_):
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