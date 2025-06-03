import tkinter as tk

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