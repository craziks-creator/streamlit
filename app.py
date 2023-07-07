import os
from flask import Flask, render_template
from flask_restful import Resource, Api
'''
app = Flask(__name__)
api = Api(app)

class Greeting (Resource):
    def get(self):
        return "Clever Cloud is Up & Running!"

api.add_resource(Greeting, '/')
app.run(host="0.0.0.0", port=os.environ.get("PORT", 8080))
'''

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
    
@app.route("/py")
def salvador():
    return "Hello, Salvador"
    
if __name__ == "__main__":
    app.run(debug=True)
