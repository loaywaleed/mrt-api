#!/usr/bin/env python3
"""
MRT Api
"""

from flask import Flask

app = Flask('__name__')

@app.route('/')
def home():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
