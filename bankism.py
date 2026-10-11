import json
import re

print("=============================")
print("       WELCOME TO BANKSIM")
print("=============================")

balance = 5000.0

request = input("Enter your banking request: ")
text = request.lower().strip()

memo = input("Enter transaction memo (or press Enter to skip): ")
memo_text = memo.lower()

threats = [
    "ignore previous instructions",
    "ignore all security rules",
    "bypass security",
    "reveal confidential",
    "jailbreak",
    "override system instructions"
]

if (any(threat in text for threat in threats)
        or any(threat in memo_text for threat in threats)):
    result = {
        "status": "BLOCKED",
        "risk_score": 95,
        "threat_category": "PROMPT_INJECTION",
        "explanation": "Suspicious instructions detected."
    }

elif text in [
    "check balance",
    "show balance",
    "check my balance"
]:
    result = {
        "status": "APPROVED",
        "risk_score": 0,
        "threat_category": "NONE",
        "explanation": "Balance inquiry accepted.",
        "mock_balance": balance
    }

elif text.startswith("transfer "):
    match = re.fullmatch(
        r"transfer\s+(\d+(?:\.\d{1,2})?)\s+to\s+account\s+(\d+)",
        text
    )

    if not match:
        result = {
            "status": "BLOCKED",
            "risk_score": 60,
            "threat_category": "INVALID_TRANSFER_FORMAT",
            "explanation": "Use: transfer 500 to account 1234"
        }

    else:
        amount = float(match.group(1))
        account = match.group(2)

        if amount <= 0:
            result = {
                "status": "BLOCKED",
                "risk_score": 70,
                "threat_category": "INVALID_AMOUNT",
                "explanation": "Transfer amount must be positive."
            }

        elif amount > balance:
            result = {
                "status": "BLOCKED",
                "risk_score": 40,
                "threat_category": "INSUFFICIENT_FUNDS",
                "explanation": "Mock account has insufficient funds."
            }

        else:
            result = {
                "status": "APPROVED",
                "risk_score": 10,
                "threat_category": "NONE",
                "explanation": "Transfer validated in simulation.",
                "mock_amount": amount,
                "recipient_account": account
            }

else:
    result = {
        "status": "BLOCKED",
        "risk_score": 60,
        "threat_category": "AMBIGUOUS_REQUEST",
        "explanation": "Request not recognized."
    }

print(json.dumps(result, indent=4))