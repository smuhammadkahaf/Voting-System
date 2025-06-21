
import pyotp
import qrcode

key = pyotp.random_base32()
totp = pyotp.TOTP(key)
print(key)
uri = totp.provisioning_uri(name="kahaf",issuer_name="VOSYS")
print(uri)
qrcode.make(uri).save("totp.png")
print(totp.verify(input("Enter:")))