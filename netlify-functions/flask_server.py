from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def handler(event, context):
    """Lambda function handler"""
    return app(event, context)
