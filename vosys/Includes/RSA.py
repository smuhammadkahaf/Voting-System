class RSA:
    """
        P = 283
        Q = 179
        N = 50657
        T = 50196
        E = 2083
        D = 4675
    """

    def __init__(self,n=50657,e=2083,d=4675):
        self.__N = n
        self.__E = e
        self.__D = d
        self.__msg=""

    def set_msg (self,message):
        self.__msg = message
    def get_msg (self):
        return self.__msg

    def __encrypt_num(self,m):
        message = pow(m,self.__E,self.__N)
        return message

    def __decrypt_num(self,m):
        message = pow(m,self.__D,self.__N)
        return message

    def __encrypt_char(self, char):
        message  = ord(char)
        __messageE = self.__encrypt_num(message)
        return chr(__messageE)

    def __decrypt_char(self, char):
        message = ord(char)
        message_d = self.__decrypt_num(message)
        return chr(message_d)

    def encrypt_msg(self):
        encrypted_string = ""
        if not self.__msg:
            return ""
        for char in self.__msg:
            encrypted_string +=  self.__encrypt_char(char)
        self.__msg = encrypted_string

    def decrypt_msg(self):
        decrypted_string = ""
        if not self.__msg:
            return ""
        for char in self.__msg:
            decrypted_string += self.__decrypt_char(char)
        self.__msg = decrypted_string


'''obj = RSA()

obj.set_msg("hello world")
obj.encrypt_msg()
print(obj.get_msg())

obj.decrypt_msg()
print(obj.get_msg())'''