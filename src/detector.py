from alert_database import ALERTS


# ---------------------------------------------------
# Detect Failed Login Attempts
# ---------------------------------------------------
def detect_failed_logins(logs):
    return [log for log in logs if "Failed login" in log["message"]]


# ---------------------------------------------------
# Brute Force Detection
# ---------------------------------------------------
def check_brute_force(failed_logins):
    return len(failed_logins) >= 3


# ---------------------------------------------------
# Detect Security Events
# ---------------------------------------------------
def detect_events(logs):
    events = []

    for log in logs:
        message = log["message"]

        if "logged in successfully" in message:
            events.append(("successful_login", log))

        elif "Failed login" in message:
            events.append(("failed_login", log))

        elif "Account" in message and "locked" in message:
            events.append(("account_locked", log))

        elif "Malware detected" in message:
            events.append(("malware", log))

        elif "Port scanning detected" in message:
            events.append(("port_scan", log))

        elif "Privilege escalation" in message:
            events.append(("privilege_escalation", log))

    return events


# ---------------------------------------------------
# Display Alert (Terminal)
# ---------------------------------------------------
def show_alert(event_name):

    alert = ALERTS[event_name]

    print("\n" + "=" * 50)
    print("Event          :", event_name.replace("_", " ").title())
    print("Severity       :", alert["severity"])
    print("MITRE ATT&CK   :", alert["mitre"])
    print("Description    :", alert["description"])
    print("Recommendation :", alert["recommendation"])
    print("=" * 50)


# ---------------------------------------------------
# Create Security Incidents
# ---------------------------------------------------
def create_incidents(logs):

    incidents = []

    failed_logins = detect_failed_logins(logs)

    # -----------------------------
    # Brute Force
    # -----------------------------
    if check_brute_force(failed_logins):

        first_log = failed_logins[0]
        message = first_log["message"]

        user = message.split("user ")[1].split(" from")[0]
        source_ip = message.split("from ")[1]

        incidents.append({
            "attack": "Brute Force",
            "attempts": len(failed_logins),
            "user": user,
            "source_ip": source_ip,
            "severity": ALERTS["brute_force"]["severity"],
            "mitre": ALERTS["brute_force"]["mitre"],
            "recommendation": ALERTS["brute_force"]["recommendation"]
        })

    # -----------------------------
    # Other Security Events
    # -----------------------------
    for log in logs:

        message = log["message"]

        # Malware
        if "Malware detected" in message:

            incidents.append({
                "attack": "Malware",
                "attempts": 1,
                "user": "N/A",
                "source_ip": "N/A",
                "severity": ALERTS["malware"]["severity"],
                "mitre": ALERTS["malware"]["mitre"],
                "recommendation": ALERTS["malware"]["recommendation"]
            })

        # Port Scan
        elif "Port scanning detected" in message:

            source_ip = message.split("from ")[1]

            incidents.append({
                "attack": "Port Scan",
                "attempts": 1,
                "user": "Unknown",
                "source_ip": source_ip,
                "severity": ALERTS["port_scan"]["severity"],
                "mitre": ALERTS["port_scan"]["mitre"],
                "recommendation": ALERTS["port_scan"]["recommendation"]
            })

        # Privilege Escalation
        elif "Privilege escalation" in message:

            user = message.split("user ")[1]

            incidents.append({
                "attack": "Privilege Escalation",
                "attempts": 1,
                "user": user,
                "source_ip": "N/A",
                "severity": ALERTS["privilege_escalation"]["severity"],
                "mitre": ALERTS["privilege_escalation"]["mitre"],
                "recommendation": ALERTS["privilege_escalation"]["recommendation"]
            })

        # Account Locked
        elif "Account" in message and "locked" in message:

            user = message.split("Account ")[1].split(" locked")[0]

            incidents.append({
                "attack": "Account Locked",
                "attempts": len(failed_logins),
                "user": user,
                "source_ip": "N/A",
                "severity": ALERTS["account_locked"]["severity"],
                "mitre": ALERTS["account_locked"]["mitre"],
                "recommendation": ALERTS["account_locked"]["recommendation"]
            })

    return incidents