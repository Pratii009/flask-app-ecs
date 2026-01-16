from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello jenkins ,this is my first webhook experiment.please work this time man.thankk uhhh yup worked well'

@app.route('/health')
def health():
    return 'Server is up and running'
