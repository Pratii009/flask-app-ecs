from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello jenkins ,this is my first webhook experiment.hope it works well in first use'

@app.route('/health')
def health():
    return 'Server is up and running'
