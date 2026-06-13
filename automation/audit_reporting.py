audit_events = [
    {
        "user": "john.doe",
        "action": "login",
        "status": "success"
    },
    {
        "user": "sarah.smith",
        "action": "privilege_change",
        "status": "review_required"
    }
]

for event in audit_events:
    print(
        f"User={event['user']} "
        f"Action={event['action']} "
        f"Status={event['status']}"
    )