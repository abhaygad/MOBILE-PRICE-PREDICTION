import time

import Data_process
import Recomdation
import streamlit as st
import webbrowser

import selection_algo

option1_n=[]

option2_n=[]

def option():
    opt = []
    del opt[::]
    opt.append(option1_n)
    opt.append(option2_n)
    return opt

def algori():
    st.title("MOBLIE RECOMMANDATION")

    No_Recemend = st.slider('Enter the number of phone to be recommended: ', 1, 10, 2)

    st.write("Recommending {} moblie Phone for You".format(No_Recemend))

    prize = st.number_input('Enter thr prize limit', min_value=15000, key="prize")

    selection_algo.option()


    if st.button('RECOMMEND', key="Recommend"):

        Full_Data = Data_process.data_read()
        Required_Data = Data_process.data_manupulate(Full_Data,prize)
        required_instance,a=selection_algo.req(Required_Data)
        ind = Recomdation.recommend(No_Recemend, required_instance,a)
        short_output = Recomdation.recommend_output(Required_Data, ind, No_Recemend)


        st.subheader("Recommended Moblie Phone For You")
        with st.container():

            for i in range(No_Recemend):
                st.write(str(short_output[i]))
                #st.button('More info',key="key"+str(i),on_click=webbrowser.open_new_tab('C:/Users/varek/OneDrive/Desktop/Moblie_web/phone_source/' + str(short_output[i]) +'.html'))
                webbrowser.open_new_tab(("https://pricebaba.com/mobile/" + str(short_output[i])
                    ).replace(" ","-"))






