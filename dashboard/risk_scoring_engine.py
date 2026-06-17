class RiskScoringEngine:

    def calculate_risk_score(
        self,
        inactive_days,
        privileged_access,
        mfa_enabled
    ):

        score = 0

        if inactive_days > 90:
            score += 40

        if privileged_access:
            score += 40

        if not mfa_enabled:
            score += 20

        return score


if __name__ == "__main__":

    engine = RiskScoringEngine()

    score = engine.calculate_risk_score(
        inactive_days=120,
        privileged_access=True,
        mfa_enabled=False
    )

    print(f"Risk Score: {score}")