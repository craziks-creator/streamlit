import streamlit as st
from PIL import Image
st.title("Projects")

image = Image.open('https://pixabay.com/vectors/telegram-app-logo-icon-application-5662082/')
st.image(image, caption='Sunrise by the mountains')
st.write("You have entered")
