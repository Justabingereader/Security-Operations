# Password Manager CLI

## Executive Summary

This project is a command-line password manager built in Python, designed to securely store and retrieve credentials for individuals or organisations. It demonstrates applied knowledge of cryptography, secure software design, and database-backed application development.

Passwords are encrypted using `pycryptodome` and stored in a MySQL database, accessible only via a master password — never exposed in plaintext. The CLI supports adding entries (with site name, URL, email, and username), searching for specific credentials, masked display of all stored entries, and secure clipboard copying for practical use without exposing passwords on screen.

The application includes a configuration script for first-time setup and database provisioning, as well as guard logic to prevent duplicate entries and misconfiguration errors. The overall design reflects an understanding of credential management best practices aligned with cybersecurity industry standards.

**Key skills demonstrated:** Python application development, cryptographic libraries (pycryptodome), MySQL integration, CLI design, secure credential storage, master password architecture, and applied security engineering.
