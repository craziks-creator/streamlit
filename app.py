import os
from flask import Flask, render_template
from flask_restful import Resource, Api

import streamlit as st

import streamlit.components.v1 as components
st.title("Main Page")
st.title('A title with _italics_ :blue[colors] and emojis :sunglasses:')
st.image("https://res.cloudinary.com/practicaldev/image/fetch/s--0cij5eUa--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/t0jgef3vyjid17z8sf3m.png", caption='this is a telegram feed')
st.header("this python page is hosted by streamlit ")
st.subheader('Breakfast Favourites')
st.text('🍲 Omega 3 & Blueberry Oatmeal')
st.text('🌯 Kale, Spinach & Rocket Smoothie')
st.text('🥚 Hard-Boiled Free-Range Egg')
st.text('🥝🧉 Avacado Toast')
st.sidebar.success("Select a page ")
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Collapsible Group Item #1
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #1 content
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-header" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Collapsible Group Item #2
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #2 content
          </div>
        </div>
      </div>
    </div>
    """,
    height=600,
)
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

