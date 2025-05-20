# from flask import Flask, url_for
# app = Flask(__name__)

# @app.route('/')
# def hello():
#     image_url = url_for('static', filename='cat_meme_1.gif')
#     return f"""
#     <h1>God Damn It!</h1>
#     <img src="{image_url}" />
#     """

from flask import Flask, render_template

app = Flask(__name__)
name = 'Henry'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route("/")
def index():
    return render_template("index.html", name = name, movies = movies)