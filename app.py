import streamlit as st
from multiapp import MultiApp
from apps import home, data, model # import your app modules here

app = MultiApp()

st.markdown("""
# Chronic Kidney Disease Prediction """)
# st.set_page_config(
#     page_title="Prediction App",
#     page_icon="🤖",
#     layout="centered",
#     initial_sidebar_state="expanded")


# Add all your application here
app.add_app("What is CKD? How can you find it ?", home.app)
app.add_app("Data Analysis", data.app)
app.add_app("Check,if you are prone to ckd", model.app)
# The main app
app.run()
