import time
import streamlit as st

def login():
    placeholder = st.empty()
    with placeholder.container():
        side = st.sidebar.text("Login Page")
        user = st.text_input("Username")
        password =  st.text_input("Password", type="password")
        clicked = st.button("Login")

        if clicked:
            if user == "admin" and password =="admin":
                st.success(" success login")
                time.sleep(1)
                placeholder.empty() #clean containder
                side.empty()
                return True
            else:
                st.error("wrong data")

if login():
    st.sidebar.text("Home Page")
    st.header("Home Page")


