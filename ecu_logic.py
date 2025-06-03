import hmac
import hashlib
import os

SECRET_KEY = b"supersecretkey"
LOG_PATH = "logs/requests.log"

if not os.path.exists("logs"):
    os.makedirs("logs")

try:
    with open("logs/counter.txt", "r") as f:
        last_counter = int(f.read())
except FileNotFoundError:
    last_counter = -1

def verify_code(code):
    global last_counter
    for i in range(last_counter + 1, last_counter + 5):  # Accept next 5 values
        expected = hmac.new(SECRET_KEY, str(i).encode(), hashlib.sha256).hexdigest()
        if expected == code:
            last_counter = i
            with open("logs/counter.txt", "w") as f:
                f.write(str(last_counter))
            log_event(code, True)
            return True
    log_event(code, False)
    return False

def log_event(code, status):
    with open(LOG_PATH, "a") as f:
        f.write(f"Code: {code[:10]}..., Status: {'Accepted' if status else 'Rejected'}\n")

def get_logs():
    try:
        with open(LOG_PATH, "r") as f:
            return f.readlines()[-5:]  # Last 5 logs
    except FileNotFoundError:
        return []
def get_last_counter():
    return last_counter
