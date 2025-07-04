import tkinter as tk

from Includes.Common import Common
from Logic.Voter.Voter import Voter
from Includes.TOTP import MyTOTP

class AvailableElections:
    def __init__(self, root):
        self.root = root
        self.root.title("Available Elections")
        self.root.geometry("1024x600")
        self.root.configure(bg="#252525")
        self.root.resizable(False, False)
        self.buildUI()

    def buildUI(self):
        title = tk.Frame(self.root, bg="#252525")
        title.pack(pady=(50, 0))  # slightly space from top
        title_label = Common.new_label(title, "On Going Elections", 30)
        title_label.pack()

        button_frame = tk.Frame(self.root, bg="#252525")
        button_frame.pack(fill="x", pady=(0, 10))

        back_button = Common.new_button(button_frame, "Results")
        back_button.pack(side="right")
    #
        warning = tk.Frame(self.root, bg="#252525")
        warning.pack()