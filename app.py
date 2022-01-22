import streamlit as st
from multiapp import MultiApp
from apps import page1, page2
app = MultiApp()
st.title("Streamlit App Demo")

st.write("""
# Select Page as per Your Choice
""")


app.add_app("page1",page1.app)
app.add_app("page2",page2.app)
app.run()