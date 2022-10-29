# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 11:50:56 2022

@author: CHEETAH
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
   app.run(host='0.0.0.0',port=8080)