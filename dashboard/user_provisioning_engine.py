class UserProvisioningEngine:

    def provision_user(self, user):

        return {
            "user": user,
            "action": "Provisioned",
            "systems": [
                "AWS",
                "Kubernetes",
                "GitHub",
                "VPN"
            ]
        }

    def deprovision_user(self, user):

        return {
            "user": user,
            "action": "Deprovisioned",
            "systems": [
                "AWS",
                "Kubernetes",
                "GitHub",
                "VPN"
            ]
        }