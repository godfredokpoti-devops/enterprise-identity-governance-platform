import json

report = {
    "total_identities": 1500,
    "privileged_accounts": 125,
    "approved_access_reviews": 120,
    "revoked_access_reviews": 5,
    "compliance_status": "PASS"
}

print("=== COMPLIANCE REPORT ===")

print(
    json.dumps(
        report,
        indent=4
    )
)