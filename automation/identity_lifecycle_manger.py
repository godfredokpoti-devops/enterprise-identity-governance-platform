import json


employees = [
    {
        "name": "Godfred Okpoti",
        "department": "Engineering",
        "role": "Developer"
    },
    {
        "name": "Frederick Sowah",
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