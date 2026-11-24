# Python for Cybersecurity 

Welcome! I am Zunaira, an aspiring Cybersecurity Analyst. This repository documents my journey learning Python, from basic syntax to building practical security scripts.

## Projects

Here are the scripts I have built to practice real-world security concepts:

### 1. Caesar Cipher (`caesar_cipher.py`)
*   **Skill:** Cryptography & Logic
*   **What it does:** A fully functional encryption/decryption tool. It also includes a "brute-force" loop that can crack a secret message without knowing the encryption key. It also includes some of my basic practices as I work through this amazing skill.

### 2. Vulnerability Scanner (`vuln_report.py`)
*   **Skill:** Data Parsing (CSV)
*   **What it does:** Reads a vulnerability scan CSV file and filters for "CRITICAL" severity items. It uses `.upper()` to ensure it catches case variations (e.g., "Critical", "CRITICAL").

### 3. Brute Force Detector (`brute_force_detector.py`)
*   **Skill:** Threat Detection & Thresholds
*   **What it does:** Parses a login log CSV, counts the number of failed login attempts from a specific IP address, and triggers a security alert if the threshold reaches 3 or more.

### 4. Login Alerts (`login_alerts.py`)
*   **Skill:** Log Analysis
*   **What it does:** A script that scans login logs and prints out alerts for any failed login attempts, identifying the user and the IP address.

### 5. Command-Line Data Parser (`csv_input.py`)
*   **Skill:** Command-Line Arguments & File Handling
*   **What it does:** Reads student data from a CSV file and formats it into readable sentences, experimenting with different delimiters.
(All of these are in the csv_input.py file)

## My Goals
- Master Python syntax and logic.
- Build custom cybersecurity tools.
- Document my progress consistently.

*(More advanced tools like keyloggers and network sniffers will be added as I progress through my course!)*
