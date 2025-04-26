# IT6-Take-Home-Drill
This project is a small Python script that brute-forces a 3-digit PIN by sending HTTP POST requests directly over a socket connection to a local server (`127.0.0.1:8888`).

## What It Does
- Tries all PINs from `000` to `999`.
- Sends each PIN using a **raw** HTTP POST request over TCP (no libraries like `requests` used).
- Handles server responses:
  - If the server says "Incorrect number", it tries the next PIN.
  - If the server says "Please wait", it waits a second before retrying (basic rate-limiting handling).
  - If neither of those, it assumes the PIN was correct and stops.

## How It Works
1. **Creates a socket** connection to the server.
2. **Builds a manual HTTP POST** request, including headers and form data.
3. **Sends** the request and **reads** the response.
4. **Parses** the server's reply to decide what to do next.
5. **Repeats** until the correct PIN is found.

## Files
- takehomedrill.py: The main Python script that runs the attack.
- README.md: This file explaining what’s going on.
