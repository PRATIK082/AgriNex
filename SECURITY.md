# Security Policy
Report vulnerabilities privately through GitHub private vulnerability reporting if enabled, or contact the repository owner through the verified GitHub profile contact. Do not publish exploitable details or farm credentials.

Principles: unique device identity; TLS; encryption at rest for sensitive data; least privilege/RBAC/tenant isolation; signed OTA and rollback protection; secure boot where supported; secrets outside source control; SBOM and dependency scanning; audit logs; network segmentation between cloud, farm LAN, safety controller and machine control; offline-safe behavior; expiring/replay-resistant commands.

Cybersecurity does not replace functional safety. A compromised or disconnected cloud service must not disable local E-stop or machine safety controls.
