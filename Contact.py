import streamlit as st

def contact():
    st.title("ABOUT US")
    # image="DATA/PRAJWAL_PHOTO(C).jpg"
    # st.image(image,width=100)
    st.write("Developed : Prajwal Purushotham Varekar")
    st.write("Gmail: Varekar@gmail.com")

    st.write("Testing : Abhay S Gad")
    st.write("Gmail: abhaygad977@gmail.com")

    st.write("Data Analyst : Akshay C")
    st.write("Gmail: akshayc612001@gmail.com")

    st.text_input('Report issue')
    if st.button('Submit') :
        st.write('Sorry for the inconvenience caused ')
