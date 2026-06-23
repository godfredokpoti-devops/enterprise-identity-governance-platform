class PrivilegedSessionManager:

    def get_sessions(self):
        return [
            {
                "user": "godfred.okpoti",
                "account": "root-admin",
                "system": "AWS Production",
                "duration": "30 Minutes",
                "status": "Active"
            },
            {
                "user": "terraform-service-account",
                "account": "CloudAdmin",
                "system": "Kubernetes",
                "duration": "15 Minutes",
                "status": "Expired"
            }
        ]