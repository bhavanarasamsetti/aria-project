# ARIA — EV Battery Failure Analysis System

## Overview

ARIA (AI-powered Root-cause Intelligence Agent) is a smart monitoring and analysis system designed to detect, analyze, and respond to electric vehicle (EV) battery anomalies in real time. It helps identify critical battery failures, determine root causes, and generate actionable insights to improve fleet reliability and safety.

---

## Problem

EV fleets rely on battery management systems (BMS) for safe operation. However, firmware updates or calibration issues can introduce hidden failures that are difficult to detect early. These issues can lead to sudden battery drops, overheating risks, charging inefficiencies, and large-scale vehicle impact.

Traditional analysis is manual and slow, increasing response time and operational risk.

---

## Solution

ARIA automates EV battery failure detection and analysis by processing log data and generating intelligent insights.

It detects anomalies such as:

* Sudden battery drops
* Voltage imbalance
* Temperature spikes

Once detected, ARIA provides:

* Root cause analysis
* Impact assessment
* Recommended fixes
* Validation test strategies
* Real-time alerts

---

## Key Features

* Real-time EV battery anomaly detection
* AI-driven root cause analysis
* Interactive dashboard visualization
* Automated fix and test recommendations
* Scalable design for fleet monitoring

---

## Technology Stack

* **Backend:** FastAPI (Python)
* **Frontend:** HTML, CSS, JavaScript
* **AI Development:** IBM Bob
* **AI Analysis:** IBM watsonx.ai (Llama model)

---

## IBM Bob Usage

IBM Bob was used throughout development for:

* Generating backend logic and APIs
* Designing system architecture
* Debugging and improving code
* Producing structured AI-based analysis (root cause, fix, tests, alerts)

Bob sessions and task history are included in the `bob_sessions/` folder as required.

---

## Project Structure

```
aria-project/
├── backend/
├── frontend/
├── src/
├── data/
├── docs/
├── bob_sessions/
├── README.md
└── requirements.txt
```

---

## How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run backend server

```
uvicorn main:app --reload
```

### 3. Open dashboard

```
http://127.0.0.1:8000/dashboard
```

---

## Demo

A demo video (≤ 3 minutes) showcasing the problem, solution, and system workflow is included in the submission.

---

## Impact

ARIA reduces failure detection time from hours to minutes, enabling faster response, improved safety, and better reliability for EV fleet operations.

---

## Authors

* Bhavana Rasamsetti
* Deepika Rasamsetti

---

## Note

API keys and sensitive credentials are not included in this repository for security reasons.
