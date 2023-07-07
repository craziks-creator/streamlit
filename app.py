import os
from flask import Flask, render_template
from flask_restful import Resource, Api
import streamlit as st
st.title("Main Page")
st.sidebar.success("Select a page above.")

