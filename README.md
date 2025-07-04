CME Detection using Aditya-L1 SWIS Data & CACTus Catalog
A project submitted for Bharatiya Antariksh Hackathon 2025

Overview:

This repository contains a robust pipeline to detect Coronal Mass Ejection (CME) Events in Aditya-L1 SWIS Level-2 datasets and match them with officially recorded CME events in the CACTus LASCO catalog.

The project: 
1. Detects anomalies in solar wind parameters using time-series feature engineering

2. Cross-verifies with CACTus-detected CMEs

3. Visualizes the results

4. Supports multi-day analysis with large-scale datasets


Purpose:

Understanding and detecting CMEs is crucial for space weather prediction, satellite safety, and mission planning.

Features:
1. Handles bulk .CDF data from Aditya-L1 SWIS (Level 2, BLK, V02)

2. Extracts and analyzes proton density, bulk speed, and thermal energy

3. Flags anomalies using statistical thresholds on gradient of smoothed signals

4. Matches events with CACTus LASCO database entries

5. Visual dashboard using Streamlit

6. Modular pipeline for future real-time integration



Tech Stack:

Languages: Python

Libraries: cdflib, pandas, numpy, matplotlib, streamlit, plotly

Data Sources:
1. https://pradan.issdc.gov.in/
2. https://www.sidc.be/cactus/


Contributions & Future Plans:
1. Enable real-time anomaly detection

2. Extend model to VELC and SUIT datasets
