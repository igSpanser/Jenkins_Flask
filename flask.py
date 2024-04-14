# import add
# Inmporting Flask
from flask import Flask
# Create the server
app=Flask(__name__)

####
@app.route("/")
def hello():
    return "Hello World"

if (__name__ == "__main__"):
    app.run(host='3.17.110.91',port='8080')

##### Copy IP from terminal output and put it it web browser. 
