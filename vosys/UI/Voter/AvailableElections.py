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
        self.build_ui()

    def build_ui(self):
        pass