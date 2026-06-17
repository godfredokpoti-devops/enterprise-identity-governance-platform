class ComplianceDashboard:

    def generate_report(self):

        report = {
            "SOC2": "PASS",
            "ISO27001": "PASS",
            "Dormant Accounts": 12,
            "Privileged Accounts": 8,
            "MFA Coverage": "95%"
        }

        return report


if __name__ == "__main__":

    dashboard = ComplianceDashboard()

    report = dashboard.generate_report()

    print("\n=== Compliance Dashboard ===")

    for key, value in report.items():
        print(f"{key}: {value}")