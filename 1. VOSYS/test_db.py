from DataBase import Database

if __name__ == "__main__":
    print("About to connect…")
    try:
        db = Database()
        print("Connected successfully!")
    except Exception as e:
        print("Caught exception:", e)
