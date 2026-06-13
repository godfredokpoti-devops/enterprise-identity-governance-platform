privileged_identities = [
    {
        "identity": "github-admin",
        "type": "service_account",
        "privilege": "admin",
        "last_used_days": 120
    },
    {
        "identity": "aws-deploy-role",
        "type": "machine_identity",
        "privilege": "power_user",
        "last_used_days": 12
    }
]

for identity in privileged_identities:
    if identity["last_used_days"] > 90:
        print(
            f"PRIVILEGED ACCESS REVIEW REQUIRED: "
            f"{identity['identity']} | "
            f"Type={identity['type']} | "
            f"LastUsed={identity['last_used_days']} days"
        )