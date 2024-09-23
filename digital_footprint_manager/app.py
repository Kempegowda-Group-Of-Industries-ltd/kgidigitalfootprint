import streamlit as st
from scraper import track_online_presence
from remover import request_data_removal
from privacy_advisor import provide_privacy_tips

# Set app configuration
st.set_page_config(page_title="Digital Footprint Manager", page_icon="assets/logo.png")

# App Title and Logo
st.image("assets/logo.png", width=100)
st.title("Digital Footprint Manager")
st.subheader("Track and Minimize Your Digital Footprint")

# Sidebar for navigation
st.sidebar.title("Menu")
options = st.sidebar.radio("Go to", ['Track Online Presence', 'Data Removal', 'Privacy Tips'])

# Track online presence
if options == 'Track Online Presence':
    st.header("Track Your Online Presence")
    email = st.text_input("Enter your email address to scan your online profiles:")
    
    if st.button("Start Scan"):
        with st.spinner("Scanning..."):
            profiles = track_online_presence(email)
        st.write("Detected Online Profiles:")
        for profile in profiles:
            st.write(f"- {profile['platform']}: {profile['link']}")

# Data Removal Request
elif options == 'Data Removal':
    st.header("Request Data Removal")
    platform = st.selectbox("Select Platform", ["Facebook", "Instagram", "Twitter", "LinkedIn", "Other"])
    data_type = st.selectbox("Select Data Type to Remove", ["Posts", "Comments", "Entire Profile"])
    
    if st.button("Request Removal"):
        with st.spinner("Sending request..."):
            success = request_data_removal(platform, data_type)
        if success:
            st.success("Data removal request sent successfully!")
        else:
            st.error("Failed to send data removal request.")

# Privacy Tips
elif options == 'Privacy Tips':
    st.header("Privacy Recommendations")
    privacy_tips = provide_privacy_tips()
    for tip in privacy_tips:
        st.write(f"• {tip}")
