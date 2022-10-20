from PIL import Image
import streamlit as st

st.title("Welcome to my first web app")
st.text("Wellcome")
st.header("Cyber class")
st.subheader(" link to Streamlit Learmung https://streamlit-review.onrender.com/")
# Open Terminal
# c:> streamlit run <python file .py>

name = st.text_input("username")
button_click = st.button("click me")
if button_click:
    if name == "admin":
        st.text("good user")
        st.success("good user")
    else:
        st.error("bad user")

#data_file = Image.open('Cyber.png')
#st.image(data_file)