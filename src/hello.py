from datetime import date

def hello_world():
    today = date.today()
    print("Hello, World! Today's date is:", today)
    return "Hello, World!"


if __name__ == "__main__":
    hello_world()