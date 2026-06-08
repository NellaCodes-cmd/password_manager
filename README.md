# Password Manager Tool

A Python cybersecurity tool that analyzes password strength, generates secure passwords, and checks for data breaches using the HaveIBeenPwned API.

## Features
- ✅ Check password strength with detailed feedback
- ✅ Generate strong random passwords
- ✅ Check if a password has appeared in known data breaches
- ✅ Uses k-Anonymity — your password never leaves your machine

## Technologies Used
- Python 3
- Object Oriented Programming (OOP)
- HaveIBeenPwned API
- SHA-1 Hashing

## How to Run
1. Clone the repository
2. Install dependencies: `pip install requests`
3. Run: `python main.py`

## OOP Structure
| Class | Responsibility |
|-------|---------------|
| `PasswordAnalyzer` | Scores password across 6 security criteria |
| `PasswordGenerator` | Generates cryptographically varied passwords |
| `BreachChecker` | Queries HaveIBeenPwned API using SHA-1 + k-Anonymity |
