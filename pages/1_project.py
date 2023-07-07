import streamlit as st
from PIL import Image
st.title("Projects")

image = Image.open('sunrise.jpg')
st.image(image, caption='Sunrise by the mountains')
st.write("You have entered")
