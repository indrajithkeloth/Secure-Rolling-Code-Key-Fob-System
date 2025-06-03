import hmac
import hashlib

SECRET_KEY = b"supersecretkey"

def generate_code(counter):
    return hmac.new(SECRET_KEY, str(counter).encode(), hashlib.sha256).hexdigest()