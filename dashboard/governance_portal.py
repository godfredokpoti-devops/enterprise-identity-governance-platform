from compliance_dashboard import ComplianceDashboard
from risk_scoring_engine import RiskScoringEngine
from access_review_dashboard import AccessReviewDashboard


print("\n===================================")
print(" Enterprise Identity Governance ")
print("===================================\n")


# Compliance Dashboard
compliance = ComplianceDashboard()
report = compliance.generate_report()

print("COMPLIANCE STATUS")
for key, value in report.items():
    print(f"{key}: {value}")

print("\n---------------------------\n")


# Risk Scoring
risk = RiskScoringEngine()

score = risk.calculate_risk_score(
    inactive_days=120,
    privileged_access=True,
    mfa_enabled=False
)

print(f"RISK SCORE: {score}")

print("\n---------------------------\n")


# Access Reviews
review = AccessReviewDashboard()

for item in review.get_access_reviews():
    print(
        f"{item['user']} | "
        f"{item['role']} | "
        f"{item['status']}"
    )

print("\n===================================")
print(" Governance Portal Completed ")
print("===================================")