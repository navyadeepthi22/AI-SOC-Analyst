import streamlit as st
import pandas as pd
import plotly.express as px
import tempfile
import os

from parser import read_log_file
from detector import create_incidents
from report import create_report_text
from ai_engine import analyze_incident, generate_executive_summary

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="AI SOC Analyst Assistant",
    page_icon="🛡️",
    layout="wide"
)


# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #0b1220;
        color: white;
    }


    .header-box {

        background: linear-gradient(
            90deg,
            #111827,
            #1e3a5f
        );

        padding: 25px;
        border-radius: 15px;
        margin-bottom: 25px;

    }


    .title {

        font-size: 38px;
        font-weight: bold;
        color: white;

    }


    .subtitle {

        color: #b8c7d9;
        font-size: 17px;

    }


    .metric-card {

        background-color: #111827;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #243447;
        text-align: center;

    }


    .metric-title {

        color: #94a3b8;
        font-size: 15px;

    }


    .metric-value {

        color: white;
        font-size: 32px;
        font-weight: bold;

    }


    </style>
    """,
    unsafe_allow_html=True
)



# =====================================================
# HEADER
# =====================================================

st.markdown(
    """
    <div class="header-box">

    <div class="title">
    🛡️ AI SOC Analyst Assistant
    </div>

    <div class="subtitle">
    Automated Threat Detection & AI-Powered Incident Analysis Platform
    </div>

    <br>

    🟢 SYSTEM STATUS : ACTIVE

    </div>
    """,
    unsafe_allow_html=True
)



# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.title("🛡 SOC Console")

    st.write(
        """
        ### Modules

        📊 Dashboard

        📂 Log Analysis

        🚨 Incident Monitoring

        🤖 AI Analyst

        📄 Reports
        """
    )

    st.divider()

    st.info(
        "AI SOC Analyst v1.0"
    )



# =====================================================
# FILE UPLOAD
# =====================================================

st.subheader("📂 Security Log Analysis")


uploaded_file = st.file_uploader(
    "Upload log file",
    type=["log", "txt"]
)


analyze_button = st.button(
    "🔍 Analyze Logs",
    use_container_width=True
)



# =====================================================
# PROCESS LOGS
# =====================================================

if uploaded_file and analyze_button:


    with st.spinner(
        "Analyzing security events..."
    ):


        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".log"
        ) as temp_file:


            temp_file.write(
                uploaded_file.getvalue()
            )


            temp_path = temp_file.name



        logs = read_log_file(
            temp_path
        )


        incidents = create_incidents(
            logs
        )


        os.remove(
            temp_path
        )



    st.success(
        "✅ Analysis completed successfully"
    )



    if incidents:


        # =====================================================
        # RISK SCORE
        # =====================================================

        risk_score = 0


        for incident in incidents:

            if incident["severity"] == "Critical":

                risk_score += 10


            elif incident["severity"] == "High":

                risk_score += 7


            elif incident["severity"] == "Medium":

                risk_score += 4


            else:

                risk_score += 1



        risk_score = min(
            risk_score,
            100
        )



        if risk_score >= 70:

            risk_status = "🔴 HIGH RISK"


        elif risk_score >= 40:

            risk_status = "🟠 MEDIUM RISK"


        else:

            risk_status = "🟢 LOW RISK"



        # =====================================================
        # METRICS
        # =====================================================

        total_logs = len(logs)

        total_incidents = len(incidents)

        critical_count = len(
            [
                i for i in incidents
                if i["severity"] == "Critical"
            ]
        )


        c1, c2, c3, c4 = st.columns(4)


        with c1:

            st.metric(
                "📄 Log Events",
                total_logs
            )


        with c2:

            st.metric(
                "🚨 Incidents",
                total_incidents
            )


        with c3:

            st.metric(
                "🔴 Critical Alerts",
                critical_count
            )


        with c4:

            st.metric(
                "🛡 Risk Score",
                f"{risk_score}/100"
            )


        st.caption(
            risk_status
        )


        st.divider()
        # =====================================================
# EXECUTIVE AI ASSESSMENT
# =====================================================

        st.subheader("🤖 Executive AI Assessment")

        with st.spinner("Generating AI executive summary..."):

         executive_summary = generate_executive_summary(
            incidents
        )

        st.info(executive_summary)

        st.divider()

        

        # =====================================================
        # DATA TABLE + CHARTS
        # =====================================================


        df = pd.DataFrame(
            incidents
        )


        st.subheader(
            "📋 Incident Overview"
        )


        st.dataframe(
            df,
            use_container_width=True
        )


        col1, col2 = st.columns(2)


        with col1:

            severity_data = (
                df["severity"]
                .value_counts()
                .reset_index()
            )


            severity_data.columns = [
                "Severity",
                "Count"
            ]


            fig1 = px.pie(
                severity_data,
                names="Severity",
                values="Count",
                title="Threat Severity"
            )


            st.plotly_chart(
                fig1,
                use_container_width=True
            )


        with col2:

            attack_data = (
                df["attack"]
                .value_counts()
                .reset_index()
            )


            attack_data.columns = [
                "Attack",
                "Count"
            ]


            fig2 = px.bar(
                attack_data,
                x="Attack",
                y="Count",
                title="Attack Categories"
            )


            st.plotly_chart(
                fig2,
                use_container_width=True
            )


        st.divider()
        # =====================================================
# INCIDENT INVESTIGATION PANEL
# =====================================================


        st.subheader(
            "🚨 Active Incident Queue"
        )


        for incident in incidents:


            severity = incident["severity"]


            if severity == "Critical":

                icon = "🔴"


            elif severity == "High":

                icon = "🟠"


            elif severity == "Medium":

                icon = "🟡"


            else:

                icon = "🟢"



            with st.expander(
                f"{icon} {incident['attack']} | {severity}"
            ):


                col1, col2 = st.columns(2)



                with col1:


                    st.write(
                        "**Attack:**",
                        incident["attack"]
                    )


                    st.write(
                        "**User:**",
                        incident["user"]
                    )


                    st.write(
                        "**Source IP:**",
                        incident["source_ip"]
                    )


                    st.write(
                        "**Attempts:**",
                        incident["attempts"]
                    )



                with col2:


                    st.write(
                        "**Severity:**",
                        incident["severity"]
                    )


                    st.write(
                        "**MITRE ATT&CK:**",
                        incident["mitre"]
                    )


                    st.write(
                        "**Status:** 🔴 OPEN"
                    )



                st.divider()



                # =====================================================
                # AI SOC ANALYST SECTION
                # =====================================================


                st.subheader(
                    "🤖 AI Analyst Assessment"
                )


                ai_result = analyze_incident(
                    incident
                )



                st.write(
                    "**Threat Summary:**"
                )


                st.info(
                    ai_result["summary"]
                )



                st.write(
                    "**Potential Impact:**"
                )


                st.warning(
                    ai_result["impact"]
                )



                st.write(
                    "**Recommended Response:**"
                )


                for action in ai_result["actions"]:

                    st.write(
                        f"✅ {action}"
                    )



                st.divider()



                # =====================================================
                # REPORT DOWNLOAD
                # =====================================================


                st.subheader(
                    "📄 Incident Report"
                )


                report_text = create_report_text(
                    incident
                )


                st.download_button(
                    label="📥 Download Report",
                    data=report_text,
                    file_name=f"{incident['attack']}_Incident_Report.txt",
                    mime="text/plain"
                )



    else:


        st.success(
            "🎉 No security threats detected in the uploaded logs."
        )



elif uploaded_file is None:


    st.info(
        "Upload a security log file to begin analysis."
    )