import pyotp
import qrcode
import tkinter as tk
from PIL import Image, ImageTk
import io

class MyTOTP:

    def __init__(self):
        self.key = None
        self.uri = None

    def new_key(self):
        self.key = pyotp.random_base32()
        return self.key

    def set_key(self,key):
        self.key = key

    def make_URI(self,name):
        totp = pyotp.TOTP(self.key)
        self.uri = totp.provisioning_uri(name=str(name), issuer_name="VOSYS")

    def generate_qr_code(self,frame): #this function place the qrcode on the given frame
        qr_img = qrcode.make(self.uri)
        buffer = io.BytesIO()
        qr_img.save(buffer, format="PNG")
        buffer.seek(0)
        qr_image = Image.open(buffer).resize((150, 150))
        self.tk_image = ImageTk.PhotoImage(qr_image)
        self.label = tk.Label(frame, image=self.tk_image)
        self.label.grid(row=0,column=0)

    def verify_otp(self,otp):
        totp = pyotp.TOTP(self.key)
        return totp.verify(otp)

    def setup_new_key (self,name,frame):
        self.new_key()                  # Generate a new secret key
        self.make_URI(name)             # Create the provisioning URI with the given user name
        self.generate_qr_code(frame)    # Display the QR code in the specified frame
        return self.key                 # Return the key (to store in DB or use as needed)

    def setup_old_key(self,key,name,frame):
        self.set_key(key)
        self.make_URI(name)
        self.generate_qr_code(frame)
        return self.key

    def verify(self,key,otp):
        self.set_key(key)
        return self.verify_otp(otp)