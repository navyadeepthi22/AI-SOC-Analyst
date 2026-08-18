# 🛡️ AI SOC Analyst

### AI-Powered Security Operations Center Investigation & Threat Analysis

An AI-assisted Security Operations Center (SOC) application designed to analyze security logs, identify suspicious activity, explain potential threats, map detections to the **MITRE ATT&CK framework**, assess severity, and provide recommended remediation actions.

🔴 **Live Demo:** https://ai-soc-analyst.streamlit.app/

---

## 🚀 Overview

**AI SOC Analyst** is a cybersecurity project that combines traditional rule-based security detection with AI-powered analysis to assist with SOC investigation workflows.

The application is designed to help security analysts move from **raw security events → detection → investigation → threat explanation → remediation** in a single workflow.

Instead of only displaying suspicious log entries, the system attempts to provide security context around detected activity and make the results easier to understand.

---

## 🎯 Project Objectives

The main objectives of this project are to:

* Detect suspicious security events from logs
* Identify potential brute-force and unauthorized access activity
* Analyze security events using AI
* Explain the possible attack and its impact
* Assign an appropriate severity level
* Map detected activity to **MITRE ATT&CK techniques**
* Provide recommended remediation actions
* Present investigation results through an interactive SOC dashboard
* Demonstrate an end-to-end SOC investigation workflow

---

## ✨ Key Features

### 🔍 Security Log Analysis

The application processes security-related log data and looks for suspicious patterns and events.

Examples include:

* Failed login attempts
* Repeated authentication failures
* Suspicious source activity
* Potential brute-force behavior
* Security alerts generated from detected events

### 🤖 AI-Powered Security Analysis

Detected events can be analyzed using an AI model to generate security-focused insights.

The AI analysis is designed to provide:

* Threat summary
* Potential impact
* Confidence assessment
* Recommended actions
* Security context for the detected event

### 🎯 MITRE ATT&CK Mapping

Detected attack behavior can be mapped to relevant **MITRE ATT&CK techniques**.

For example, repeated authentication failures may be associated with:

**T1110 — Brute Force**

This helps connect individual alerts with a recognized adversary behavior framework.

### 🚨 Severity Assessment

Security events are categorized according to their potential risk, helping analysts prioritize alerts that require attention.

### 📊 SOC Dashboard

The Streamlit interface provides a centralized dashboard for viewing investigation results, alerts, and security analysis.

### 📄 Investigation Reporting

The project supports generating structured security findings that can be used to document an investigation.

---

## 🧠 Architecture

```text
                    ┌─────────────────────┐
                    │     Security Logs   │
                    │ Windows / Linux /   │
                    │ Firewall / IDS      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Log Parser        │
                    │     parser.py       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Detection Engine    │
                    │    detector.py      │
                    └──────────┬──────────┘
                               │
                    Suspicious Events
                               │
                               ▼
              ┌────────────────────────────────┐
              │      AI Security Analyzer      │
              │        ai_analyzer.py          │
              │                                │
              │  Threat Explanation            │
              │  Impact Analysis               │
              │  Confidence                    │
              │  Recommended Actions           │
              └───────────────┬────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │  MITRE ATT&CK       │
                    │  Technique Mapping  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   SOC Dashboard     │
                    │      app.py         │
                    └─────────────────────┘
```

---

## 🔄 Investigation Workflow

```text
Log Input
   ↓
Log Parsing
   ↓
Event Detection
   ↓
Suspicious Activity Identified
   ↓
AI Security Analysis
   ↓
Severity Assessment
   ↓
MITRE ATT&CK Mapping
   ↓
Recommended Remediation
   ↓
SOC Investigation Report
```

---

## 🛠️ Technology Stack

| Technology                    | Purpose                                |
| ----------------------------- | -------------------------------------- |
| **Python**                    | Core application development           |
| **Streamlit**                 | SOC dashboard and web interface        |
| **Google Gemini API**         | AI-assisted security analysis          |
| **Pandas**                    | Data processing                        |
| **Matplotlib**                | Data visualization                     |
| **Scikit-learn**              | Machine-learning related functionality |
| **MITRE ATT&CK**              | Threat behavior mapping                |
| **Git & GitHub**              | Version control and source management  |
| **Streamlit Community Cloud** | Application deployment                 |

---

## 📁 Project Structure

```text
AI-SOC-Analyst/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── ai_analyzer.py
│   ├── alert_database.py
│   ├── detector.py
│   ├── parser.py
│   └── main.py
│
├── logs/
│   └── sample.log
│
└── ...
```

> The exact project structure may evolve as additional features are added.

---

## 🔐 Security Approach

The project follows a **hybrid security analysis approach**:

### Rule-Based Detection

Traditional detection logic is used to identify known suspicious patterns.

This provides:

* Predictable detection behavior
* Fast identification of known patterns
* A deterministic first layer of analysis

### AI-Assisted Investigation

After suspicious activity is detected, AI is used to provide additional context and explanation.

This allows the system to go beyond simply saying:

> "Suspicious activity detected."

and instead provide analyst-oriented information such as:

* What may have happened
* Why the activity is suspicious
* Potential impact
* Confidence in the assessment
* Suggested next steps

This combination is intended to demonstrate how **traditional SOC detection and modern AI-assisted analysis can work together**.

---

## 🧪 Example Investigation

A simplified investigation can follow this pattern:

```text
Multiple failed login attempts
            ↓
Detection Engine
            ↓
Potential Brute Force Activity
            ↓
Severity: High
            ↓
MITRE ATT&CK: T1110
            ↓
AI Analysis
            ↓
Threat Explanation
            ↓
Recommended Remediation
```

---

## 🌐 Live Application

The project is deployed using **Streamlit Community Cloud**.

### 🔴 Try the Application

**https://ai-soc-analyst.streamlit.app/**

Streamlit Community Cloud provides GitHub-connected deployment, allowing committed repository changes to be reflected in the deployed application.

---

## 💻 Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/navyadeepthi22/AI-SOC-Analyst.git
cd AI-SOC-Analyst
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root and add your API configuration.

```env
GEMINI_API_KEY=your_api_key_here
```

> **Never commit API keys or other secrets to GitHub.**

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

The application will then be available through the local Streamlit URL shown in the terminal.

---

## ⚠️ Disclaimer

This project is intended for **educational, research, and cybersecurity learning purposes**.

The AI-generated analysis should be treated as an assistance layer rather than a replacement for professional security analysts or established incident-response procedures.

Detection results may depend on the quality and format of the input logs.

---

## 🔮 Future Improvements

Potential future enhancements include:

* Real-time log ingestion
* Additional log-source integrations
* Windows Event Log integration
* Linux authentication log integration
* Firewall and IDS/IPS integrations
* SIEM integrations
* Advanced anomaly detection
* Automated incident correlation
* Expanded MITRE ATT&CK coverage
* Threat intelligence integration
* Historical alert tracking
* Authentication and role-based access
* Automated incident-response playbooks
* Improved AI confidence evaluation
* Containerized deployment

---

## 📚 Learning Outcomes

This project helped demonstrate practical concepts in:

* Security Operations Center workflows
* Log analysis
* Threat detection
* Authentication attack detection
* AI-assisted cybersecurity
* MITRE ATT&CK
* Security alert triage
* Python development
* Streamlit application development
* API integration
* Git/GitHub version control
* Cloud deployment

---

## 👩‍💻 Author

**Navya Deepthi**

B.Tech Computer Science Engineering
Cybersecurity Enthusiast

### Project

**AI SOC Analyst — AI-Assisted Security Investigation Dashboard**

🔗 **Live Demo:** https://ai-soc-analyst.streamlit.app/

---

## ⭐ Project Status

**Status: Deployed & Functional**

The application is currently deployed through Streamlit Community Cloud and connected to its GitHub repository.

---

### ⭐ If you find this project interesting, consider giving the repository a star!
