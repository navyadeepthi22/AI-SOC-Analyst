import os
import json
from pathlib import Path

from dotenv import load_dotenv
from google import genai


# =====================================================
# LOAD ENVIRONMENT VARIABLES
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY was not found. "
        "Make sure your .env file is in the project root."
    )


# =====================================================
# GEMINI CLIENT
# =====================================================

client = genai.Client(
    api_key=api_key
)


# =====================================================
# INDIVIDUAL INCIDENT AI ANALYSIS
# =====================================================

def analyze_incident(incident):
    """
    Uses Gemini AI to analyze one SOC security incident.
    """

    prompt = f"""
You are an experienced SOC Level 1 Security Analyst.

Analyze the following cybersecurity incident.

Incident Details:
Attack: {incident['attack']}
User: {incident['user']}
Source IP: {incident['source_ip']}
Attempts: {incident['attempts']}
Severity: {incident['severity']}
MITRE ATT&CK: {incident['mitre']}

Respond ONLY as valid JSON.

Use exactly this format:

{{
    "summary": "...",
    "impact": "...",
    "confidence": "...",
    "actions": [
        "...",
        "...",
        "..."
    ]
}}

Do not include markdown.
Do not include text outside the JSON.
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        text = response.text.strip()

        # Remove Markdown code fences if Gemini adds them
        if text.startswith("```"):
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

        result = json.loads(text)

        return result

    except Exception as e:

        return {
            "summary": "AI analysis could not be completed.",
            "impact": str(e),
            "confidence": "Unknown",
            "actions": [
                "Review the incident manually.",
                "Verify Gemini API configuration.",
                "Check application logs."
            ]
        }


# =====================================================
# EXECUTIVE AI SUMMARY
# =====================================================

def generate_executive_summary(incidents):
    """
    Uses Gemini to analyze all detected incidents
    and generate an overall SOC assessment.
    """

    if not incidents:
        return "No security incidents were detected."

    incident_text = ""

    for i, incident in enumerate(incidents, start=1):

        incident_text += f"""
Incident {i}
Attack: {incident['attack']}
Severity: {incident['severity']}
User: {incident['user']}
Source IP: {incident['source_ip']}
MITRE ATT&CK: {incident['mitre']}
Attempts: {incident['attempts']}
"""

    prompt = f"""
You are a Senior SOC Analyst.

Analyze the following security incidents as a whole:

{incident_text}

Provide a concise executive SOC assessment.

Include:

1. Overall Risk Level
2. Main Threats
3. Potential Business Impact
4. Immediate Priority Actions

Keep the response professional and under 180 words.

Do not return JSON.
Do not use markdown tables.
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:

        return f"Executive AI summary unavailable: {e}"