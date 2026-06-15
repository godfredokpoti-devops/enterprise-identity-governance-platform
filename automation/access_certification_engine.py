import json

access_reviews = [

    {
        "user": "john.doe",
        "role": "Developer",
        "manager_decision": "Approved"
    },

    {
        "user": "sarah.smith",
        "role": "Security Analyst",
        "manager_decision": "Approved"
    },

    {
        "user": "service-account-prod",
        "role": "Root",
        "manager_decision": "Revoked"
    }
]

for review in access_reviews:

    print(
        json.dumps(
            review,
            indent=4
        )
    )

    print(
        f"Certification Status: "
        f"{review['manager_decision']}"
    )

    print("-" * 40)