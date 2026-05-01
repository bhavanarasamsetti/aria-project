import streamlit as st
from analyzer import read_file
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Read Bob output
def read_bob_output():
    with open("output/battery_incident_report.txt", "r") as file:
        return file.read()

# Generate PDF
def generate_pdf(report_text):
    file_path = "output/incident_report.pdf"

    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()

    content = []

    for line in report_text.split("\n"):
        content.append(Paragraph(line, styles["Normal"]))

    doc.build(content)

    return file_path


# UI
st.title("ARIA — Voltix Autonomous Monitoring System")
st.caption("AI-powered automatic failure detection using IBM Bob")


# Start monitoring button
if st.button("Start Monitoring System"):

    st.write("🟢 Monitoring system logs...")

    log_data = read_file("data/ev_battery_issue.txt")

    if "ERROR" in log_data or "ALERT" in log_data:

        st.error("🔴 Incident Detected!")
        st.write("⚡ ARIA activated automatically...")

        # ✅ Get Bob output
        bob_output = read_bob_output()

        st.subheader("🧠 ARIA + IBM Bob Analysis")

        # ✅ SHOW SHORT VERSION (before Summary)
        if "Summary:" in bob_output:
            summary_part = bob_output.split("Summary:")[0]
        else:
            summary_part = bob_output  # fallback

        st.text(summary_part)

        # Optional: show full report expandable
        with st.expander("📄 View Full Detailed Report"):
            st.text(bob_output)

        # Alert
        if "Alert:" in bob_output:
            alert_part = bob_output.split("Alert:")[-1]
            st.warning("🚨 ALERT: " + alert_part)

        # PDF (full report)
        pdf_path = generate_pdf(bob_output)

        with open(pdf_path, "rb") as file:
            st.download_button(
                label="📄 Download Full Incident Report",
                data=file,
                file_name="ARIA_Incident_Report.pdf",
                mime="application/pdf"
            )

    else:
        st.success("✅ No issues detected. System running normally.")