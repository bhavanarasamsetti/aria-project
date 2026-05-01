import streamlit as st
from analyzer import generate_mock_report, read_file

st.title("ARIA — Voltix Failure Analysis System")

st.write("Paste system logs or use sample data")

# Input box
user_input = st.text_area("Enter system logs here")

# Button
if st.button("Analyze"):

    if user_input.strip() == "":
        # Use sample data if nothing entered
        log_data = read_file("data/ev_battery_issue.txt")
    else:
        log_data = user_input

    report = generate_mock_report(log_data)

    st.subheader("🧠 ARIA INCIDENT REPORT")
    st.text(report)
    st.caption("AI-powered debugging using IBM Bob — from failure to fix in seconds")