import json


employees = [
    {
        "name": "John Doe",
        "department": "Engineering",
        "role": "Developer"
    },
    {
        "name": "Sarah Smith",
        "department": "Security",
        "role": "Security Analyst"
    }
]


def onboard_user(user):
    print(f"Creating identity for {user['name']}")

    identity = {
        "name": user["name"],
        "department": user["department"],
        "role": user["role"],
        "status": "Active"
    }

    return identity


for employee in employees:
    result = onboard_user(employee)

    print(
        json.dumps(
            result,
            indent=4
        )
    )