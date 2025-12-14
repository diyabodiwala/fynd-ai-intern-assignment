import streamlit as st
import json
from datetime import datetime
from llm_utils import call_llm
import pandas as pd
import os

DATA_FILE = "data_store.json"

# Ensure file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

st.set_page_config(page_title="Feedback System", layout="wide")

page = st.sidebar.selectbox(
    "Select View",
    ["User Dashboard", "Admin Dashboard"]
)

# ---------------- USER DASHBOARD ----------------
if page == "User Dashboard":
    st.title("Customer Feedback")

    rating = st.selectbox("Select Star Rating", [1, 2, 3, 4, 5])
    review = st.text_area("Write your review")

    if st.button("Submit"):
        llm_output = call_llm(review, rating)

        with open(DATA_FILE, "r") as f:
            data = json.load(f)

        entry = {
            "rating": rating,
            "review": review,
            "user_response": llm_output["user_response"],
            "summary": llm_output["summary"],
            "recommended_action": llm_output["recommended_action"],
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        data.append(entry)

        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

        st.success("Feedback submitted!")
        st.info(llm_output["user_response"])


# ---------------- ADMIN DASHBOARD ----------------
else:
    st.title("📊 Admin Dashboard – Customer Feedback")

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    if not data:
        st.warning("No feedback data available yet.")
    else:
        df = pd.DataFrame(data)

        st.subheader("All Submissions")
        st.dataframe(df, use_container_width=True)

        st.subheader("Analytics")
        st.metric("Total Submissions", len(df))
        st.metric("Average Rating", round(df["rating"].mean(), 2))
