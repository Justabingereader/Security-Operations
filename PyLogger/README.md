PyLogger: The Local Keylogger

Overview:

PyLogger is an offline keylogger written in Python that captures clipboard data, takes screenshots, and logs keystrokes. This program is designed to help organizations monitor how their employees enter data on company systems, serving as a backup for data and a means of enhancing security practices. In the event of a data breach, PyLogger facilitates the tracing of any leaks.

Features:

Keystroke Logging: Records all keystrokes made on the system.

Clipboard Monitoring: Captures and logs clipboard data.

Screenshot Capture: Takes screenshots at specified intervals.

SQLite Database: All logged data is stored in a SQLite database (keylogger.db), which can be easily viewed using DB Browser for SQLite.

Local Operation: Operates entirely on the local machine without transmitting data externally, ensuring privacy and security.

Purpose:

PyLogger is designed to assist organizations in implementing best security practices and guidelines. By monitoring user activity, it helps to identify potential data leaks and ensures that sensitive information is handled appropriately.

Installation:

To run PyLogger, you can execute it through your code editor or command line terminal. Ensure you have Python installed on your system.

Prerequisites:

Python 3.x
Required libraries (install using pip):

pip install pywin32 pynput pillow sounddevice scipy cryptography requests

Usage:
Clone the repository:

git clone https://github.com/yourusername/PyLogger.git
cd PyLogger

Run the program:
Through your code editor or command line terminal:

python main.py

Access the logged data:
Open the keylogger.db file using DB Browser for SQLite to view the logged keystrokes, clipboard data, and paths to screenshots.

Security Considerations:
For security purposes, keystrokes and clipboard data are not directly created as separate files. Instead, all information is logged into the SQLite database. This approach minimizes the risk of unauthorized access to sensitive data.

Disclaimer:
This program is intended for ethical use only. Ensure that you have the necessary permissions to monitor any system or user activity. Unauthorized use of keyloggers may violate privacy laws and regulations.
