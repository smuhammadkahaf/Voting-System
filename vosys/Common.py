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
    def new_label_fg(frame_, text_, font_,fg_):
        return tk.Label(
            frame_,
            text=text_,
            font=("Arial", font_, "bold"),  # increased font size
            fg=fg_,
            bg="#252525"
        )