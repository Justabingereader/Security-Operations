Password Manager CLI

Overview:

The Password Manager CLI is a command-line application designed to provide a safe and secure way to store passwords.
Utilizing Python and MySQL, this application serves as a central repository for passwords that individuals or organizations
wish to protect from unauthorized access. It adheres to best security standards and guidelines required by the cybersecurity domain.

Requirements:

To run this application, ensure you have the following installed:
Python
MySQL setup on your computer

You will need to install the following Python packages:

pip install rich
pip install pycryptodome
pip install mysql-connector-python
pip install pyperclip

Usage:

Initial Setup
Run the Configuration Script:
Open Windows PowerShell and execute the following command to see the help options:

python config.py --help

Configuration Options:
You will be presented with three options: make, delete, and remake. To set up the application for the first time, run:

python config.py make

Set Master Password:
You will be prompted to create a master password. Make it as secure as possible and store it safely, as it will not be shown to you again.
You will need to retype the password for confirmation.

Database Creation:
A database named pm will be created to store your passwords.

Adding a User
To add a new password entry, run the following command:

python pm.py add -s sitename -u siteurl -e email -l username
After executing this command, you will be prompted to enter your master password. Once entered,
you will be asked to input the password you wish to store. After entering the password, press Enter to save it.

Viewing Stored Passwords
To view a list of all stored passwords, run:

python pm.py e
You will need to enter your master password to access the stored data. All passwords will be displayed as {hidden} for security.

Error Handling
If you attempt to add the same entry twice or run python config.py make after already configuring the application, you will receive appropriate error messages.

Searching for Specific Entries
To check for a specific password entry, use the following command:

python pm.py e -s entryname
You will be prompted to enter your master password to view the specific entry.

Copying Passwords
If you want to copy a password for personal use, run:

python pm.py e -s entryname --copy
After entering your master password, a message will confirm that your password has been copied to the clipboard.

Conclusion
This Password Manager CLI application provides a secure and user-friendly way to manage your passwords.
By following the setup and usage instructions, you can ensure that your sensitive information is stored safely and accessed securely.
