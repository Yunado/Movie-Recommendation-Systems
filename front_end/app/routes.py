""" Specifies routing for the application"""
from flask import render_template, request, jsonify
from app import app
from webforms import SearchForm
import content_based_system as cb
import matrix_factorization_system as mfs
import user_based_system as ubs


app.config['SECRET_KEY'] = 'any secret string'

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title='Home Page')

@app.route("/user_content",methods=['GET', 'POST'])
def user_content():
    targetItem = []
    res = ubs.movies_ranking()
    if request.method == 'POST':
        form = request.form
        genre = request.form['submit_button']
        for movie_name in res[genre]:
            item = {
                 "movie_name" : movie_name,
                 "genre" : genre
            }
            targetItem.append(item)

    return render_template("user_content.html",
                            targetItem=targetItem
    )    

@app.route('/content_based', methods=['GET', 'POST'])
def content_based():
    form = SearchForm()
    targetItem = []
    if request.method == 'POST':
         print("what do you mean???")
         form = SearchForm()
         data = form.searched.data #input value
         data = data.strip()
         rec_movies = cb.get_recommendations(data)
         for index, movie in rec_movies:
            item = {
                "movie_name" : movie
            }
            targetItem.append(item)
    return render_template(
        "content_based.html",
        form=form,
        targetItem=targetItem
    )
@app.route("/autoencoder_based",methods=['GET', 'POST'])
def autoencoder_based():
    form = SearchForm()
    targetItem = []
    if request.method == 'POST':
         form = SearchForm()
         data = form.searched.data #input value
         data = int(data.strip())
         recommend_list = mfs.recommend_movie(data)
         for movie_name, rating in recommend_list:
            item = {
                "movie_name" : movie_name,
                "rating":rating
            }
            targetItem.append(item)
    return render_template(
        "autoencoder_based.html", 
        form=form,
        targetItem=targetItem
    ) 