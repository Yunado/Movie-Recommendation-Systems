# Movie Recommendation Systems

Project and Setup Tutorial Presentation
**https://www.youtube.com/watch?v=o72IUbud1Zg**

## Overview

We are building a website of recommender systems to recommend
movies to users. It is essential and exciting because films are very close to our daily life and the performance of the recommended system will affect the users’ experience. 

We implemented three architectures in our recommendation system, the
matrix factorization, content-based filter and user-based filter based on the public dataset on Kaggle.

## Related work

We have a literature review on some related papers to seek inspiration.

Autorec: Autoencoders meet collaborative filtering [1]

This essay proposes AutoRec, a new Collective Filter (CF) model based on the
autoencoder paradigm; our interest in this paradigm stems from the recent
successes of (deep) neural network models for vision and speech tasks. The
authors argue that AutoRec has representational and computational advantages
over existing neural approaches to CF, and demonstrate empirically that it
outperforms the current state-of-the-art methods.

Collaborative denoising auto-encoders for top-n recommender systems [2]

In this paper, the researchers present a new model-based collaborative filtering
(CF) method for top-N recommendation called Collaborative. Denoising
Auto-Encoder (CDAE). CDAE assumes that whatever user-item interactions are
observed are a corrupted version of the user’s full preference set. The model
learns latent representations of corrupted user-item preferences that can best
reconstruct the full input.1 This also means, during training, the authors feed the
model a subset of a user’s item set and train the model to recover the whole item
set; at prediction time, the model recommends new items to the user given the
existing preference set as input. Training on corrupted data effectively recovers
co-preference patterns. This essay shows that this is an effective approach for
collaborative filtering.

A Practical Introduction to Information Retrieval and Text Mining. Chapters 10 - Section 10.4, Chapters 11 [3]

We have learnt how machine learning can be used to combine multiple scoring
factors to optimize the ranking of documents in web search and learn techniques
used in recommender systems (also called filtering systems), including
content-based recommendation/filtering and collaborative filtering.

Deep Learning Based Recommender System [4]

In the essay, the researchers provided an extensive review of the most notable
works to date on deep learning-based recommender systems. They proposed
a two-dimensional classification scheme for organizing and clustering existing
publications. They also conduct a brief statistical analysis of these works to
identify the contributions and characteristics of these studies. They highlight a
bunch of influential research prototypes and analyze their
advantages/disadvantages and applicable scenarios. The goal of this essay is to
thoroughly review the literature on the advances of deep learning-based
recommender systems. It provides a panorama with which readers can quickly
understand and step into the field of deep learning-based recommendation.

## Dataset
We searched online on different platforms to find the best movie dataset for our
recommendation system. After the comparison, we find the “TMDB 5000
Movie Dataset” from Kaggle [5], which is the most suitable one for the project.
In this dataset, there are about 5000 movie rows and many useful columns from
two CSV files so that we could set up our recommender system based on
various content. For instance, the famous movie Avatar has the genres of action,
adventure, and fantasy, the language of English, the production company
Twentieth Century Fox Film Corporation, and a popular value from the first file.

## System Design

We developed a website that is used for recommending movies to the user. The website is based on the three recommender system algorithms:

1. Content-based Filter System

  The users could use this system by searching for a movie, and the system will show ten relevant movies based on the input movie. This recommendation system is based on two kinds of filters. 
  - The overview expresses the basic content of the movie and we use the overview to build a TF-IDF matrix to get similar movies.
  - The keyword, cast, crew, and genres are also good for finding the relevant movies that the users may like so we create a count vector for these factors to get the relevant movies.
  Each filter would return the top 5 relevant movies so the whole content-based filter system would return 10 movies for the users. 

2. User-based Filter System
  The users could use this system by searching for a movie based on the movie's genre. The system will show top 50 relevant movies and show them in different genres. In this project, we don't ask new users to rating movies, the users only need to search movies based on genre types. And we focus on recommending movies by genres.

3. Matrix Factorization-based System

  The matrix factorization system is a system based on the Singular Value Decomposition (SVD) method. Popularized by Simon Funk and tied for third place on the Netflix Prize. The system utilizes matrix factorization to generalize users' ratings and recommend based on the rating trend. Users can input a user id to observe other users' rating history, whereas entering an id can recommend the top 10 relevant movies to the user based on the prediction score generated by the system.
 
  3.1. Hyperparameter tuning for Matrix Factorization-based System

  To find the best parameters for this prediction algorithm, we run a grid search with 10-fold cross-validations on a set of parameters, where at the end we pick the parameters that yield the smallest root mean square deviation and mean absolute error.
  The grid search requires some computation time and space, in the end, we deployed the matrix factorization system with the best parameters found in tuning.
  
Evaluating RMSE, MAE of algorithm SVD on 10 split(s).
```bash
                  Fold 1  Fold 2  Fold 3  Fold 4  Fold 5  Fold 6  Fold 7  Fold 8  Fold 9  Fold 10 Mean    Std     
RMSE (testset)    1.3388  1.1147  1.1958  1.1558  1.2166  1.0997  1.2294  1.0925  1.2551  1.3314  1.2030  0.0845  
MAE (testset)     0.8888  0.7712  0.8202  0.8272  0.8453  0.8101  0.8396  0.8060  0.8436  0.9225  0.8375  0.0406      

Average MAE:  0.8374585298155782
Average RMSE:  1.2029845887182495

# Grid-Search for best params
param_grid = {
  'n_factors': [20, 50, 100, 200, 500],
  'n_epochs': [5, 10, 20, 50]
}
```
At the end, the Matrix-Factorization-based system is deployed with n_factors = 500 and n_epochs = 5.

## Setup Tutorial

### Web Application Structure
```bash
front_end
├── app/
│ ├── static/
│ │ ├── script/
│ │ │ └── model.js
│ │ ├── styles/
│ │ │ └── custom.css
│ │ └── layout.html
│ ├── templates/
│ │ └── autoencoder_based.html
│ │ └── content_based.html
│ │ └── home.html
│ │ └── layout.html
│ │ └── user_content
│ └── __init__.py
│ ├── routes.py
├── Back_end
│ └── user_based_system.py
│ └── matrix_factorization_system.py
│ └── content_based_system.py
│ └── dataset 
│── webforms
└── main.py
```

### Dependencies

* random
* pandas
* numpy
* sklearn
* flask 
* scikit-suprise
* python >= 3.5

### Installing

* git clone git@github.com:woshicqy/CS410-Final-Project-Team-Early-Offer.git
* pip install flask flask_sqlalchemy pymysql pyyaml
* pip install scikit-surprise

### Executing program

```bash
cd front_end
python3 -m venv env
source env/bin/activate
export FLASK_APP=app && export FLASK_DEBUG=1
flask run
```
You can now running the website by clicking http://127.0.0.1:5000/home

## Note

1. The movie name for searching in the content-based page must exist in the database.
2. The user id for searching in the matrix-factorization-based page must exist in the dataset, or else it will result in IndexError in HTML.

## Authors

Xinyi Ai, xinyia2@illinois.edu
Front-end website design and implementation

Xipeng Song, xipengs2@illinois.edu
Content-based Filter Recommendation System design and implementation

Yunfei Ouyang, yunfeio2@illinois.edu
Matrix Factorization-based Recommendation System design and implementation

Qiyang Chen, qiyangc2@illinois.edu
User-based Filter Recommendation System design and implementation

Yanhao Qiu, yanhaoq2@illinois.edu
Data Acquisition, Preparation and Processing

## References

[1] Sedhain, Suvash, et al. Autorec: Autoencoders meet collaborative filtering. Proceedings
of the 24th International Conference on World Wide Web. ACM, 2015

[2] Wu, Yao, et al. Collaborative denoising auto-encoders for top-n recommender systems.
Proceedings of the Ninth ACM International Conference on Web Search and Data Mining.
ACM, 2016

[3] C. Zhai and S. Massung. Text Data Management and Analysis: A Practical Introduction to
Information Retrieval and Text Mining, ACM Book Series, Morgan & Claypool Publishers,
2016

[4]Shuai Zhang, Lina Yao, Aixin Sun, and Yi Tay. 2019. Deep Learning Based Recommender
System: A Survey and New Perspectives. ACM Comput. Surv. 52, 1, Article 5 (January
2020), 38 pages. https://doi.org/10.1145/3285029

[5] Kaggle TMDB 5000 Movie Dataset.
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_credits.csv
