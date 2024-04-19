import streamlit as st
from streamlit_option_menu import option_menu
import algo
import Contact
import phone
import home

EXAMPLE_NO = 1

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu("Main Menu", ["HOME", 'RECOMMENDATION','PHONE','About Us'],
        icons=['house', 'gear','phone','person-rolodex'], menu_icon="cast", default_index=0)


if selected == "HOME":
    home.home()
if selected == "RECOMMENDATION":
    algo.algori()
if selected == "PHONE":
    phone.data()
if selected == "About Us":
    Contact.contact()



