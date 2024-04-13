import Data_process
import streamlit as st

import webbrowser

def data ():
    phone_images = []
    image_name = Data_process.data_name()

    with st.sidebar:

        st.header("Configuration")

        with st.form(key="grid_reset"):
            n_cols = st.number_input("Number of columns", 2, 6, 2)
            st.form_submit_button(label="Reset images and layout")


    st.title("LIST OF MOBILE PHONE :phone:")
    st.caption(
        "You can display the image in full size by hovering it and clicking the double arrow"
    )

    for i in(image_name) :
        try :
            phone_images.append('phone_image/'+str(i)+'0.jpg')
        except:
            phone_images.append('phone_image/download.jpg')

    n_rows = 1 + len(phone_images) // int(n_cols)
    rows = [st.container() for _ in range(n_rows)]
    cols_per_row = [r.columns(n_cols) for r in rows]
    cols = [column
            for row in cols_per_row
            for column in row]

    for image_index, cat_image in enumerate(phone_images):
        cols[image_index].image(cat_image)

        cols[image_index].caption(cat_image.replace('phone_image/','').replace('0.jpg',''))
        if cols[image_index].button('More info', key=str(cat_image.replace('phone_image/','').replace('0.jpg',''))):

            #webbrowser.open_new_tab('C:/Users/varek/OneDrive/Desktop/Moblie_web/phone_source/'+str(cat_image.replace('phone_image/','').replace('0.jpg',''))+'.html')
            webbrowser.open_new_tab("https://pricebaba.com/mobile/" + str(cat_image.replace('phone_image/', '').replace('0.jpg', '').replace(" ","-")))








