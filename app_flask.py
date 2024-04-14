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
    app.run(host='0.0.0.0',port='8080', debu=True)

##### Copy IP from terminal output and put it it web browser. 
