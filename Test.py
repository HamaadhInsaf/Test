import streamlit as st

def Note():
    st.write("This is a test application")
    st.write("I am testing web hosting and this is my first web hosted application!")

def Video():
    st.video("https://www.youtube.com/watch?v=FyUIEOcYMrY")

Options = ["Both", "Note", "Video"]
Option = st.sidebar.selectbox("Options", Options)

st.title("Streamlit sharing")

if Option == "Both":
    Note()
    Video()
elif Option == "Note":
    Note()
elif Option == "Video":
    Video()
else:
    st.write("Nothing selected")