
#  import the Flask dependency
from flask import Flask

# Create a New Flask App Instance
app = Flask(__name__)

# Create Flask Routes
# create a function called hello_world()
@app.route('/')
def hello_world():
    return 'Hello world'
