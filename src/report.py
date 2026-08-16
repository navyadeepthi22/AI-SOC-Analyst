# ---------------------------------------------------
# Terminal Report Generator
# ---------------------------------------------------

def generate_report(incident):

    print("\n" + "=" * 50)
    print("         AI SOC INCIDENT REPORT")
    print("=" * 50)

    print(f"Attack         : {incident['attack']}")
    print(f"Attempts       : {incident['attempts']}")
    print(f"User           : {incident['user']}")
    print(f"Source IP      : {incident['source_ip']}")
    print(f"Severity       : {incident['severity']}")
    print(f"MITRE ATT&CK   : {incident['mitre']}")

    print("\nRecommended Actions:")

    recommendation = incident["recommendation"]

    if isinstance(recommendation, list):
        for action in recommendation:
            print(f"• {action}")
    else:
        print(f"• {recommendation}")

    print("=" * 50)



# ---------------------------------------------------
# Download Report Generator (Frontend Support)
# ---------------------------------------------------

def create_report_text(incident):

    report = ""

    report += "=" * 50 + "\n"
    report += "          AI SOC INCIDENT REPORT\n"
    report += "=" * 50 + "\n\n"

    report += f"Attack         : {incident['attack']}\n"
    report += f"Attempts       : {incident['attempts']}\n"
    report += f"User           : {incident['user']}\n"
    report += f"Source IP      : {incident['source_ip']}\n"
    report += f"Severity       : {incident['severity']}\n"
    report += f"MITRE ATT&CK   : {incident['mitre']}\n"

    report += "\nRecommended Actions:\n"

    recommendation = incident["recommendation"]

    if isinstance(recommendation, list):

        for action in recommendation:
            report += f"• {action}\n"

    else:

        report += f"• {recommendation}\n"


    report += "\n" + "=" * 50 + "\n"

    return report