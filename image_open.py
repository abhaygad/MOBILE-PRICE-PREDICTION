from PIL import Image
import streamlit as st
import Data_process
cat_image=[]
def image_open():
    image_name=Data_process.data_name()

    for i in(image_name) :
        try :
            image = Image.open('phone_image/'+str(i)+'0.jpg')
            st.image(image, caption=i)
            st.button('More info', key="More_info"+i)

        except :
            st.title("Image not found")
            cat_image.append('phone_image/download.jpg')