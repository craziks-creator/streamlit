import os
from flask import Flask, render_template
from flask_restful import Resource, Api

import streamlit as st
'''
st.title("Main Page")
st.image("https://res.cloudinary.com/practicaldev/image/fetch/s--0cij5eUa--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/t0jgef3vyjid17z8sf3m.png", caption='this is a telegram feed')
st.header("this python page is hosted by streamlit ")
st.subheader('Breakfast Favourites')
st.text('🍲 Omega 3 & Blueberry Oatmeal')
st.text('🌯 Kale, Spinach & Rocket Smoothie')
st.text('🥚 Hard-Boiled Free-Range Egg')
st.text('🥝🧉 Avacado Toast')
st.sidebar.success("Select a page ")
'''
app = Flask(__name__)

@app.route("/")
def home():
    #return "Hello, World!"
    return render_template('home.html')

@app.route("/streamlit")
def streamlit():
    st.set_page_config(page_title="My Streamlit App")
    st.write("Hello, world!")
if __name__ == "__main__":
    app.run()

