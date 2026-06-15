import json

accounts = [
    {
        "user": "godfred.okpoti",
        "role": "Administrator",
        "privileged": True
    },
    {
        "user": "sarah.smith",
        "role": "Security Analyst",
        "privileged": False
    },
    {
        "user": "service-account-prod",
        "role": "Root",
        "privileged": True
    }
]

for account in accounts:

    if account["privileged"]:

        print(
            f"High Risk Access Detected: "
            f"{account['user']}"
        )

        print(
            json.dumps(
                account,
                indent=4
            )
        )