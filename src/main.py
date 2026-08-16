from parser import read_log_file
from report import generate_report
from detector import (
    detect_failed_logins,
    check_brute_force,
    detect_events,
    show_alert,
    create_incidents,
)

# Read logs
logs = read_log_file("../logs/sample.log")

# Display parsed logs
print("\n========== LOG ENTRIES ==========\n")

for log in logs:
    print("Date    :", log["date"])
    print("Time    :", log["time"])
    print("Level   :", log["level"])
    print("Message :", log["message"])
    print("-" * 50)

# Detect failed logins
failed_logins = detect_failed_logins(logs)

print("\nTotal Failed Login Attempts:", len(failed_logins))

if check_brute_force(failed_logins):
    show_alert("brute_force")

# Detect all events
events = detect_events(logs)

print("\n========== DETECTED EVENTS ==========")

for event_name, log in events:
    print(f"\nLog: {log['date']} {log['time']}")
    show_alert(event_name)


print("\n========== INCIDENTS ==========")

incidents = create_incidents(logs)

for incident in incidents:
    generate_report(incident)