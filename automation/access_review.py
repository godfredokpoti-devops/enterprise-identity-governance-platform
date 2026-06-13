users = [
    {
        "name": "John Doe",
        "last_login_days": 120
    },
    {
        "name": "Sarah Smith",
        "last_login_days": 10
    }
]

for user in users:

    if user["last_login_days"] > 90:

        print(
            f"REVIEW REQUIRED: "
            f"{user['name']}"
        )