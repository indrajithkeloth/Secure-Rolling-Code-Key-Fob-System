# Secure-Rolling-Code-Key-Fob-System
This project simulates a secure automotive keyless entry system using Flask, HMAC-based rolling codes, and a replay-protection mechanism. It demonstrates how a simple key fob (transmitter) and ECU (receiver) pair can use synchronized counters to securely authorize vehicle unlocking.

## Features

- HMAC-SHA256 based rolling code generation
- ECU accepts only the next 5 valid codes (anti-replay)
- ECU persists the last used counter across restarts
- Replay simulation route
- Web interface using Flask

## Project Structure

- `app.py`: Main Flask app simulating the key fob
- `ecu_logic.py`: ECU backend with verification and logging
- `fob_logic.py`: Code generator logic (simulates the key fob chip)
- `logs/`: Stores accepted/rejected code logs and persistent counter

  ## Setup
  1. Ensure Python is installed
  2. Install Flask
     pip install flask
  3. Run the app:  
     python app.py
  4. Open your browser at `http://127.0.0.1:5000/`
 
     
## Security Note

This project is a simplified simulation and not intended for real vehicle security use. In practice, hardware-level encryption, nonces, and rolling key windows with secure storage are used.


![Screenshot 2025-06-03 172832](https://github.com/user-attachments/assets/cc081e37-f4fa-43ba-9273-ee6dd96bfcc6)
