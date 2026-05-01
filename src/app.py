import streamlit as st
from analyzer import generate_mock_report, read_file

st.title("ARIA — Voltix Autonomous Monitoring System")

st.caption("AI-powered automatic failure detection using IBM Bob")

# Start monitoring button
if st.button("Start Monitoring System"):

    st.write("🟢 Monitoring system logs...")

    # Read logs automatically (no user input)
    log_data = read_file("data/ev_battery_issue.txt")

    # Simple detection logic
    if "ERROR" in log_data or "ALERT" in log_data:

        st.error("🔴 Incident Detected!")
        st.write("⚡ ARIA activated automatically...")

        # Generate report
        report = generate_mock_report(log_data)

        st.subheader("🧠 ARIA INCIDENT REPORT")
        st.text(report)

        st.warning("📧 Alert sent to engineering team")

    else:
        st.success("✅ No issues detected. System running normally.")