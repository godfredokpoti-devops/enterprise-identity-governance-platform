from flask import Flask

from database import initialize_database
from database import insert_audit_log
from database import get_audit_logs

from identity_lifecycle_manager import IdentityLifecycleManager
from user_provisioning_engine import UserProvisioningEngine
from class_privileged_session_manager import PrivilegedSessionManager


app = Flask(__name__)

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

    return f"""
<html>
<head>
<title>Enterprise Identity Governance Platform</title>

<style>
body {{
    font-family: Arial, sans-serif;
    background-color: #f4f6f9;
    padding: 30px;
}}

h1 {{
    color: #1f4e79;
}}

.card {{
    background: white;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}}

.metric {{
    font-size: 32px;
    font-weight: bold;
    color: #1f4e79;
}}

table {{
    width: 100%;
    border-collapse: collapse;
}}

th {{
    background: #1f4e79;
    color: white;
    padding: 10px;
}}

td {{
    padding: 10px;
    border: 1px solid #ddd;
}}

.status-pass {{
    color: green;
    font-weight: bold;
}}

.status-risk {{
    color: red;
    font-weight: bold;
}}
</style>
</head>

<body>

<h1>Enterprise Identity Governance Platform</h1>

<div style="display:flex;gap:20px;margin-bottom:20px;">
    <div class="card" style="width:220px;text-align:center;">
        <h3>Compliance Score</h3>
        <div class="metric">95%</div>
    </div>

    <div class="card" style="width:220px;text-align:center;">
        <h3>Risk Events</h3>
        <div class="metric">12</div>
    </div>

    <div class="card" style="width:220px;text-align:center;">
        <h3>Privileged Accounts</h3>
        <div class="metric">8</div>
    </div>
</div>

<div class="card">
    <h2>Compliance Status</h2>
    <ul>
        <li>SOC2: <span class="status-pass">PASS</span></li>
        <li>ISO27001: <span class="status-pass">PASS</span></li>
        <li>Dormant Accounts: 12</li>
        <li>Privileged Accounts: 8</li>
        <li>MFA Coverage: 95%</li>
    </ul>
</div>

<div class="card">
    <h2>Identity Risk Score</h2>
    <div class="metric">100</div>
    <p class="status-risk">High Risk: Privileged inactive account without MFA detected.</p>
</div>

<div class="card">
    <h2>Access Reviews</h2>
    <table>
        <tr>
            <th>User</th>
            <th>Role</th>
            <th>Status</th>
        </tr>
        <tr>
            <td>godfred.okpoti</td>
            <td>PlatformEngineer</td>
            <td>Approved</td>
        </tr>
        <tr>
            <td>eks-cluster-admin</td>
            <td>CloudAdmin</td>
            <td>Pending</td>
        </tr>
        <tr>
            <td>terraform-service-account</td>
            <td>IAMAdmin</td>
            <td>Review Required</td>
        </tr>
    </table>
</div>

<div class="card">
    <h2>Privileged Sessions</h2>
    <table>
        <tr>
            <th>User</th>
            <th>System</th>
            <th>Status</th>
            <th>Duration</th>
        </tr>
        <tr>
            <td>Godfred Okpoti</td>
            <td>AWS Production</td>
            <td style="color:green;">Active</td>
            <td>45 Minutes</td>
        </tr>
        <tr>
            <td>Sowah Frederick</td>
            <td>Azure Subscription</td>
            <td style="color:orange;">Pending Approval</td>
            <td>0 Minutes</td>
        </tr>
        <tr>
            <td>Michael Sowah</td>
            <td>Kubernetes Cluster</td>
            <td style="color:red;">Expired</td>
            <td>120 Minutes</td>
        </tr>
    </table>
</div>

<div class="card">
    <h2>User Provisioning Requests</h2>
    <table>
        <tr>
            <th>User</th>
            <th>Application</th>
            <th>Request Type</th>
            <th>Status</th>
        </tr>
        <tr>
            <td>Godfred Okpoti</td>
            <td>AWS Console</td>
            <td>Provision</td>
            <td style="color:green;">Completed</td>
        </tr>
        <tr>
            <td>Sowah Frederick</td>
            <td>Azure Portal</td>
            <td>Provision</td>
            <td style="color:orange;">Pending Approval</td>
        </tr>
        <tr>
            <td>Michael Sowah</td>
            <td>Kubernetes Cluster</td>
            <td>Deprovision</td>
            <td style="color:red;">In Progress</td>
        </tr>
    </table>
</div>

<div class="card">
    <h2>AI Risk Recommendations</h2>
    <ul>
        <li>High Risk: Disable inactive privileged account "Michael Sowah".</li>
        <li>Medium Risk: Review AWS Production privileged sessions exceeding 30 minutes.</li>
        <li>Medium Risk: Enforce MFA on all CloudAdmin roles.</li>
        <li>Low Risk: Remove dormant Kubernetes service accounts older than 90 days.</li>
        <li>Recommendation: Schedule quarterly access certification review.</li>
    </ul>
</div>

<div class="card">
    <h2>Identity Lifecycle Management</h2>
    <table>
        <tr>
            <th>Name</th>
            <th>Status</th>
            <th>Department</th>
        </tr>
        <tr>
            <td>Godfred Okpoti</td>
            <td>Active</td>
            <td>Platform Engineering</td>
        </tr>
        <tr>
            <td>Sowah Frederick</td>
            <td>Active</td>
            <td>Cloud Engineering</td>
        </tr>
        <tr>
            <td>Michael Sowah</td>
            <td>Inactive</td>
            <td>Security</td>
        </tr>
    </table>
</div>

<div class="card">
    <h2>Database Audit Logs</h2>
    <table>
        <tr>
            <th>Event Type</th>
            <th>User</th>
            <th>Action</th>
            <th>Status</th>
            <th>Timestamp</th>
        </tr>
        {"".join([f"<tr><td>{log[0]}</td><td>{log[1]}</td><td>{log[2]}</td><td>{log[3]}</td><td>{log[4]}</td></tr>" for log in logs])}
    </table>
</div>

</body>
</html>
"""


if __name__ == "__main__":
    app.run(debug=True)