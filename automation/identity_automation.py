import json

users = [
    {
        "name": "John Doe",
        "department": "Engineering",
        "role": "Developer"
    },
    {
        "name": "Sarah Smith",
        "department": "Finance",
        "role": "Analyst"
    }
]

def provision_access(user):

    access_map = {
        "Developer": [
            "GitHub",
            "AWS",
            "Jira"
        ],

        "Analyst": [
            "PowerBI",
            "Salesforce"
        ]
    }

    permissions = access_map.get(
        user["role"],
        []
    )

    print(
        f"Provisioning {user['name']} "
        f"with access to {permissions}"
    )

for user in users:
    provision_access(user)