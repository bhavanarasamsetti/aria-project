import json
import os
import sys
from dotenv import load_dotenv

load_dotenv()

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def generate_report(log_data):
    use_api = os.getenv("USE_WATSONX_API", "false").lower() == "true"
    
    if not use_api:
        print("⚡ ARIA → Running in MOCK mode...")
        return {
            "summary": "Battery anomaly detected after firmware update v2.2.0",
            "root_cause": "Battery calibration mismatch in module BMS-04 introduced after firmware update",
            "impact": {
                "vehicles": 12000,
                "severity": "CRITICAL"
            },
            "fix": "Rollback firmware or patch calibration logic",
            "tests": [
                "High-load battery stress test",
                "Firmware compatibility test for BMS-04",
                "Thermal response validation after OTA update"
            ],
            "alert": "🚨 Critical battery issue detected — immediate engineering action required"
        }
    
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from watsonx_client import generate_text
        
        print("⚡ ARIA → Connecting to IBM watsonx.ai...")
        
        prompt = f"""You are ARIA, an AI failure analysis agent for Voltix EVs.

Analyze these logs and respond ONLY with valid JSON:

{log_data}

Required JSON format:
{{
    "summary": "brief issue summary",
    "root_cause": "detailed root cause",
    "impact": {{"vehicles": number, "severity": "CRITICAL"}},
    "fix": "recommended fix",
    "tests": ["test1", "test2", "test3"],
    "alert": "alert message"
}}"""
        
        print("🧠 IBM watsonx.ai analyzing...")
        response = generate_text(prompt)
        
        if not response:
            raise Exception("No response from API")
        
        print("✅ Response received\n")
        
        # Parse JSON from response
        response = response.strip()
        if "```json" in response:
            response = response.split("```json")[1].split("```")[0].strip()
        elif "```" in response:
            response = response.split("```")[1].split("```")[0].strip()
        
        report = json.loads(response)
        return report
        
    except Exception as e:
        print(f"⚠️ API failed: {e}")
        print("⚠️ Falling back to mock data\n")
        return {
            "summary": "Battery anomaly detected after firmware update v2.2.0",
            "root_cause": "Battery calibration mismatch in module BMS-04 introduced after firmware update",
            "impact": {
                "vehicles": 12000,
                "severity": "CRITICAL"
            },
            "fix": "Rollback firmware or patch calibration logic",
            "tests": [
                "High-load battery stress test",
                "Firmware compatibility test for BMS-04",
                "Thermal response validation after OTA update"
            ],
            "alert": "🚨 Critical battery issue detected — immediate engineering action required"
        }

def analyze():
    log_data = read_file("data/ev_battery_issue.txt")
    
    print("=== RAW LOG ===\n")
    print(log_data)
    
    print("\n=== ARIA OUTPUT ===\n")
    report = generate_report(log_data)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    analyze()

# Made with Bob
