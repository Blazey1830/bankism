# bankism
a rule based banking security firewall simulation


Bankism is a beginner-friendly, rule-based prototype that simulates a defensive security layer for banking requests.

Problem

Banking interfaces must distinguish legitimate requests from suspicious or malformed input, including prompt-injection-style instructions.

Features

- Detects selected suspicious instruction phrases.
- Classifies requests using rule-based checks.
- Assigns a risk score and threat category.
- Demonstrates mock balance inquiries and transfer validation.
- Displays security analysis in a browser-based dashboard.

Technology

- Python — command-line prototype
- HTML — website structure
- CSS — dashboard styling
- JavaScript — browser-side request analysis

How to Run

Open "index.html" in a web browser to try the website demo.

Run the Python prototype separately in a Python 3 environment.

Limitations

Bankism is an educational simulation, not a production banking system. It does not connect to real accounts, move money, or provide comprehensive AI-based security. Its detection rules are limited and can miss attacks.

Future Improvements

- Connect the dashboard to a Python backend.
- Add structured JSON responses and more test cases.
- Improve threat detection and input validation.
- Add automated security tests.
