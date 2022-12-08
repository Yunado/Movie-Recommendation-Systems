""" Specifies routing for the application"""
from flask import render_template, request, jsonify
from app import app
from webforms import SearchForm
import content_based_system as cb
import matrix_factorization_system as mfs
# from app import database

app.config['SECRET_KEY'] = 'any secret string'

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title='Home Page')

@app.route("/user_content")
def user_content():
    return render_template("user_content.html", title='User Based Recommendation')    

# @app.route("/content_based")
# def content_based():
#     return render_template("content_based.html", title='Contant Based Recommendation') 

# @app.route("/content_result")
# def content_based():
#     return render_template("content_based.html", title='Contant Based Recommendation') 

# @app.route('/content_based', methods=["POST","GET"])
# def search():
#     print("wtf")
#     form = SearchForm()
#     data = form.searched.data #input value
#     print(data)
#     rec_movies = cb.get_recommendations('The Dark Knight Rises')
#     targetItem = []
#     for index, movie in rec_movies:
#         item = {
#             "movie_name" : movie
#         }
#         targetItem.append(item)
#     return render_template(
#         "content_based.html",
#         form=form,
#         targetItem=targetItem
#     )
@app.route('/content_based', methods=['GET', 'POST'])
def content_based():
    form = SearchForm()
    targetItem = []
    if request.method == 'POST':
         print("what do you mean???")
         form = SearchForm()
         data = form.searched.data #input value
         data = data.strip()
         print(data)
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