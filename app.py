import streamlit as st
import re
from dbase import DB
db=DB()
#st.write("Welcome if you are new please register else login")
option1=''
option= st.sidebar.selectbox("Welcome if you are new please register else login",['Register','Login'])
if option=='Register':
    def is_valid_email(email):
        # Regular expression for a basic email format validation
        x=re.findall("^[a-zA-Z][a-z0-9]+@{1}[a-z]+[.][a-z]+$",email)
        return x
    with st.form("Registration Form",clear_on_submit=True):
        name=st.text_input("Enter your Name")
        email=st.text_input("Enter your Email")
        password=st.text_input("Enter your Password",type="password")
        submit=st.form_submit_button("Register")
    if submit:
        name=name.lower()
        if not name :
                st.error("Required user name.")
        elif not email:
            st.error("Required Email.id")
        elif not is_valid_email(email):
            st.error('Invalid email')
        elif not password:
            st.error("Enter a password")
        elif len(password)<5 or len(password)>8:
            st.error("password should be in between 5 to 8 letters")
        else:
        # db.insert(name,email,password)
            st.success('You are a member now')
        
if option == 'Login':
    with st.form("Login Form",clear_on_submit=True):
        email=st.text_input("Enter your Email")
        password=st.text_input("Enter your Password",type="password")
        col1,col2,col3=st.columns(3)
        with col1:
             submit=st.form_submit_button("Login")
        with col3:
             submit1=st.form_submit_button("Log out")
        if submit:
            data=db.check(email,password)
            if db.check(email,password) :
                st.success('Welcome back')
            else:
                st.error('Wrong email or password')
        if submit1:
             if db.check(email,password):
                 db.delete(email,password)
             else:
                 st.error("Cannot be deleted")