import os
from flask import Flask, render_template
from flask_restful import Resource, Api
import streamlit as st
st.title("Main Page")
st.image("https://res.cloudinary.com/practicaldev/image/fetch/s--0cij5eUa--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/t0jgef3vyjid17z8sf3m.png", caption='this is a telegram feed')
st.subheader("this python page is hosted by streamlit ")
st.sidebar.success("Select a page above.")

