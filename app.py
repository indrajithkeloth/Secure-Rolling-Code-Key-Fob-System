from flask import Flask, render_template, redirect, url_for
from ecu_logic import verify_code, get_logs, get_last_counter
from fob_logic import generate_code

app = Flask(__name__)
counter = get_last_counter() + 1  # Sync with ECU

@app.route("/")
def index():
    logs = get_logs()
    return render_template("index.html", logs=logs)

@app.route("/unlock")
def unlock():
    global counter
    code = generate_code(counter)
    if verify_code(code):  # Only increment if accepted
        counter += 1
    return redirect(url_for("index"))

@app.route("/replay")
def replay():
    code = generate_code(counter - 1)
    verify_code(code)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
