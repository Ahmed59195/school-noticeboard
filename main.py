import streamlit as st
import pandas as pd
from datetime import datetime
import os

# File to store notices
FILE = "notices.csv"

# Load notices
def load_notices():
    if os.path.exists(FILE):
        return pd.read_csv(FILE)
    return pd.DataFrame(columns=["Date", "Title", "Message"])

# Save notice
def save_notice(title, message):
    df = load_notices()
    new_notice = {"Date": datetime.now().strftime("%Y-%m-%d %H:%M"), "Title": title, "Message": message}
    df = pd.concat([df, pd.DataFrame([new_notice])], ignore_index=True)
    df.to_csv(FILE, index=False)

# UI
st.set_page_config(page_title="School Noticeboard", page_icon="📌")

st.title("📢 School Noticeboard")

with st.expander("📝 Add New Notice"):
    title = st.text_input("Notice Title")
    message = st.text_area("Notice Message")
    if st.button("Post Notice"):
        if title and message:
            save_notice(title, message)
            st.success("Notice posted successfully.")
        else:
            st.warning("Please fill in all fields.")

# Show all notices
st.subheader("📄 All Notices")
notices = load_notices()
if not notices.empty:
    for _, row in notices.iloc[::-1].iterrows():
        st.markdown(f"### {row['Title']}  \n*{row['Date']}*  \n{row['Message']}")
        st.markdown("---")
else:
    st.info("No notices yet.")
