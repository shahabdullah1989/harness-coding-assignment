from datetime import date
import time

def hello_world():
    today = date.today()
    print("Hello, World! Today's date is:", today)
    return "Hello, World!"


if __name__ == "__main__":
    hello_world()
    
print("Script completed.")
time.sleep(3600)  # Keeps container alive for 1 hour