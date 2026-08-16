ALERTS = {
    "successful_login": {
        "severity": "Low",
        "mitre": "N/A",
        "description": "Normal user login.",
        "recommendation": "No action required."
    },

    "failed_login": {
        "severity": "Medium",
        "mitre": "T1110",
        "description": "Failed authentication attempt.",
        "recommendation": "Monitor for repeated login failures."
    },

    "brute_force": {
        "severity": "High",
        "mitre": "T1110",
        "description": "Multiple failed login attempts detected.",
        "recommendation": "Block source IP and reset affected account password."
    },

    "account_locked": {
        "severity": "High",
        "mitre": "T1110",
        "description": "Account locked due to repeated failed logins.",
        "recommendation": "Verify user identity before unlocking the account."
    },

    "malware": {
        "severity": "Critical",
        "mitre": "T1204",
        "description": "Malware detected on the system.",
        "recommendation": "Isolate the endpoint and perform a full malware scan."
    },

    "port_scan": {
        "severity": "High",
        "mitre": "T1046",
        "description": "Possible network reconnaissance activity.",
        "recommendation": "Block the source IP and review firewall logs."
    },

    "privilege_escalation": {
        "severity": "Critical",
        "mitre": "T1068",
        "description": "Possible privilege escalation attempt.",
        "recommendation": "Investigate the account and review system activity."
    }
}