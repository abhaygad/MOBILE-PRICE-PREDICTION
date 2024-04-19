import streamlit as st
def home():
    st.title("HOME")
    #st.subheader('We used to spend hours looking for insights in dozens of tools and reports. Now we login to one place to find out what costumers are doing and how to meet them where it matters most')
    st.write("We serve customers by recommending the best 5G mobile phone currently available in the market, based on the required specifications of the customer and in different categories. The most obvious goal of a recommendation system is to recommend relevant products to the user.")
    st.write("Our website compares mobile phones based on their performance in various categories like display, battery, CPU, and graphics performance, and finds our customer the best smartphone based on their requirements.")
    st.image("DATA/algo_flow.jpeg",caption="Algorithm Flow")
