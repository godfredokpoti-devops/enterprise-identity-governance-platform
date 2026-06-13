# Enterprise Identity Governance Architecture

                +----------------+
                |      HRIS      |
                | Workday / HR   |
                +--------+-------+
                         |
                         v
                +----------------+
                | Identity Engine|
                | Okta / OIG     |
                +--------+-------+
                         |
        +----------------+----------------+
        |                |                |
        v                v                v

+---------------+ +---------------+ +---------------+
| AWS IAM       | | GitHub        | | Salesforce    |
| Cloud Access  | | Dev Access    | | Business Apps |
+---------------+ +---------------+ +---------------+

                         |
                         v

                +----------------+
                | Access Reviews |
                | Compliance     |
                +--------+-------+
                         |
                         v

                +----------------+
                | Audit Logs     |
                | Splunk         |
                +--------+-------+
                         |
                         v

                +----------------+
                | Security Team  |
                | SOC2 / ISO     |
                +----------------+