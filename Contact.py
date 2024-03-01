import streamlit as st

def contact():
    st.title("ABOUT US")
    image="DATA/PRAJWAL_PHOTO(C).jpg"
    st.image(image,width=100)
    st.write("Developed : Prajwal Purushotham Varekar")
    st.write("Gmail: Varekar@gmail.com")

    st.write("Testing : Keerthan M Shettigar")
    st.write("Gmail: keerthanmshettigar@gmail.com")

    st.write("Data Analyst : Sneha Madhu")
    st.write("Gmail: snehamadhu@gmail.com")

    st.text_input('Report issue')
    if st.button('Submit') :
        st.write('Sorry for the inconvenience caused ')