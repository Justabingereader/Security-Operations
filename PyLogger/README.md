# PyLogger — Endpoint Activity Monitor

## Executive Summary

PyLogger is a Python-based endpoint monitoring tool built for authorised organisational use, designed to support insider threat detection, data leak tracing, and security audit trails on company-managed systems.

The tool operates entirely offline — no data is transmitted externally — and captures three categories of activity: keystroke input, clipboard content, and periodic screenshots. All data is written to a structured SQLite database (`keylogger.db`) rather than flat files, reducing exposure of raw data and enabling efficient querying via DB Browser for SQLite or any SQL-compatible tool.

The codebase demonstrates concurrent programming (threading for periodic tasks alongside a keyboard listener), database schema design with multiple related tables, and careful handling of special key events. The project is accompanied by an ethical use disclaimer and is scoped strictly to environments where monitoring consent and legal authorisation have been established.

**Key skills demonstrated:** Python (pynput, PIL, sqlite3, threading), endpoint monitoring, SQLite database design, concurrent task scheduling, insider threat tooling, and responsible disclosure / ethical framing of offensive-adjacent tools.
