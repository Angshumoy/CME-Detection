import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
#Extract The 7z file to access the swis_with_anomalies_and_matches_new.csv file
df = pd.read_csv("C:\\Users\\ANGSHUMOY\\Downloads\\B_A_Hackathon For GitHub\\CME-Detection\\swis_with_anomalies_and_matches_new.csv", parse_dates=['time'])
cme_df = pd.read_csv("C:\\Users\\ANGSHUMOY\\Downloads\\B_A_Hackathon For GitHub\\CME-Detection\\cactus_cme_filtered_new.csv", parse_dates=['datetime'])

# Title
st.title("CME-SWIS Detector Dashboard")
st.markdown("Visualizing Solar Wind Anomalies & CACTus CME Events")

# Optional filter
with st.expander("Filter by Time Range"):
    start = st.date_input("Start Date", df['time'].min().date())
    end = st.date_input("End Date", df['time'].max().date())
    df = df[(df['time'] >= pd.to_datetime(start)) & (df['time'] <= pd.to_datetime(end))]
    cme_df = cme_df[(cme_df['datetime'] >= pd.to_datetime(start)) & (cme_df['datetime'] <= pd.to_datetime(end))]

# Main plot
st.subheader("Smoothed Speed with Anomalies & CME Events")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df['time'], df['speed_smooth'], label='Speed (Smoothed)', color='blue')
ax.scatter(df[df['anomaly_flag']]['time'], df[df['anomaly_flag']]['speed_smooth'], color='red', label='Anomaly', s=15)
for i, t in enumerate(cme_df['datetime']):
    ax.axvline(t, color='green', linestyle='--', alpha=0.5)
ax.set_xlabel("Time")
ax.set_ylabel("Speed (km/s)")
ax.legend()
st.pyplot(fig)

# Metrics
st.subheader("-Detection Metrics")
tp = df[df['anomaly_flag'] & df['confirmed_cme']].shape[0]
fp = df[df['anomaly_flag'] & ~df['confirmed_cme']].shape[0]
fn = len(cme_df) - tp if len(cme_df) > tp else 0
precision = tp / (tp + fp)
recall = tp / (tp + fn) if tp + fn > 0 else 0
f1 = 2 * (precision * recall) / (precision + recall) if precision + recall > 0 else 0

st.metric("True Positives", tp)
st.metric("False Positives", fp)
st.metric("False Negatives", fn)
st.write(f"**Precision:** {precision:.2f}  |  **Recall:** {recall:.2f}  |  **F1-Score:** {f1:.2f}")

# Data table
st.subheader("-Anomaly Table")
st.dataframe(df[df['anomaly_flag']][['time', 'speed', 'speed_smooth', 'confirmed_cme']])
