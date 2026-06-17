class AccessReviewDashboard:

    def get_access_reviews(self):

        reviews = [
            {
                "user": "john.doe",
                "role": "Developer",
                "status": "Approved"
            },
            {
                "user": "sarah.smith",
                "role": "SecurityAdmin",
                "status": "Pending"
            },
            {
                "user": "service-account-prod",
                "role": "IAMAdmin",
                "status": "Review Required"
            }
        ]

        return reviews


if __name__ == "__main__":

    dashboard = AccessReviewDashboard()

    reviews = dashboard.get_access_reviews()

    print("\n=== Access Review Dashboard ===\n")

    for review in reviews:
        print(
            f"{review['user']} | "
            f"{review['role']} | "
            f"{review['status']}"
        )