from flask import Flask, render_template

from database import initialize_database
from database import insert_audit_log
from database import get_audit_logs

from identity_lifecycle_manager import IdentityLifecycleManager
from user_provisioning_engine import UserProvisioningEngine
from class_privileged_session_manager import PrivilegedSessionManager


app = Flask(
    __name__,
    template_folder="templates",
    static_folder="."
)

initialize_database()


@app.route("/")
def home():
    lifecycle = IdentityLifecycleManager()
    employees = lifecycle.get_users()

    provisioning = UserProvisioningEngine()
    provisioned = provisioning.provision_user("Godfred Okpoti")
    deprovisioned = provisioning.deprovision_user("Michael Sowah")

    pam = PrivilegedSessionManager()
    sessions = pam.get_sessions()

    insert_audit_log(
        "ACCESS_REVIEW",
        "Godfred Okpoti",
        "Approved PlatformEngineer Access",
        "SUCCESS"
    )

    insert_audit_log(
        "PROVISIONING",
        "Sowah Frederick",
        "Azure Portal Access Request",
        "PENDING"
    )

    logs = get_audit_logs()

    return render_template(
        "dashboard.html",
        employees=employees,
        provisioned=provisioned,
        deprovisioned=deprovisioned,
        sessions=sessions,
        logs=logs
    )

if __name__ == "__main__":
    app.run(debug=True)