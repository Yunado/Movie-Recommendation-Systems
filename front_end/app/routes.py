""" Specifies routing for the application"""
from flask import render_template, request, jsonify
from app import app

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title='Home Page')

@app.route("/user_content")
def user_content():
    return render_template("user_content.html", title='User Based Recommendation')    

@app.route("/content_based")
def content_based():
    return render_template("content_based.html", title='Contant Based Recommendation') 

@app.route("/autoencoder_based")
def autoencoder_based():
    return render_template("autoencoder_based.html", title='Autoencoder Recommendation') 