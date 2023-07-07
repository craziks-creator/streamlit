import os
from flask import Flask, render_template
from flask_restful import Resource, Api
import streamlit as st
st.title("Main Page")
st.image("https://images.indianexpress.com/2022/11/Telegram-bots-2-1.jpg", caption='this is a telegram feed')
st.write("this python page is hosted by streamlit ")
st.sidebar.success("Select a page above.")

