# CourseProject

Please fork this repository and paste the github link of your fork on Microsoft CMT. Detailed instructions are on Coursera under Week 1: Course Project Overview/Week 9 Activities.

# Project Title

This project is a movie recommendation system website. 

## Description

In this project, the users can get movie recommendations based on three recommendation systems.

1. Autoencoder-based System

2. Content-based Filter System

  The users could use this system by searching a movie, and the system will show ten relevant movies based on the input movie. This recommendation system is based on two kinds of filters. 
      - The overview expresses the basic content of the movie and we use the overview to build a TF-IDF matrix to get the similar movies.
      - The keyword, cast, crew, and genres are also good for finding the relevant movies that the users may like so we create a count vector for these factors to get the relevant movies.
  Each filter would return top 5 relevant movies so the whole content-based filter system would return 10 movies for the users. 

3. User-based Filter System

## Getting Started

### Dependencies

* pandas
* numpy
* sklearn
* python >= 3.5

### Installing

* git pull
* pip install flask flask_sqlalchemy pymysql pyyaml

### Executing program

```bash
cd front_end 
source env/bin/activate
export FLASK_APP=app && export FLASK_DEBUG=1
flask run
```
You can now running the website by clicking http://127.0.0.1:5000/home

## Help

1. The movie name for searching in the content-based page must exist in the database.

## Authors


Xipeng Song, xipengs2@illinois.edu

Xinyi Ai xinyia2@illinois.edu

