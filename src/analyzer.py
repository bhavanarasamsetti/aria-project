def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def generate_mock_report(log_data):
    return f"""
🧠 ARIA INCIDENT REPORT

🔴 Issue Summary:
Battery anomaly detected after firmware update v2.2.0

📍 Root Cause:
Battery calibration mismatch in module BMS-04 introduced after firmware update

💥 Impact:
Approximately 12,000 vehicles affected
Severity: HIGH

🛠 Suggested Fix:
Patch battery calibration logic or rollback firmware version

📊 Summary:
Issue is directly linked to firmware deployment and lack of validation testing

🚨 Alert:
Critical battery issue detected — immediate engineering action required
"""


def analyze():
    log_data = read_file("data/ev_battery_issue.txt")

    print("=== RAW LOG ===\n")
    print(log_data)

    print("\n=== ARIA OUTPUT ===\n")
    report = generate_mock_report(log_data)
    print(report)


if __name__ == "__main__":
    analyze()