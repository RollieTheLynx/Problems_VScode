from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import re
import requests
import html
import os
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post ' + str(self.id)

@app.route('/')
def index():
    return render_template("mainpage.html")

@app.route('/library')
def library():
    return render_template("library.html")

@app.route('/regex', methods=['GET', 'POST'])
def regex():
    if request.method == 'POST':
        input_text = request.form['input_text']
        results = re.findall(r'\S*@\S*', input_text)
        return render_template('regex.html', results = results)
    else:
        return render_template('regex.html')

@app.route('/socials')
def socials():
    return render_template("socials.html")

@app.route('/chuck_norris', methods=['GET', 'POST'])
def chuck_norris():
    if request.method == 'POST':
        try:
            api_request = requests.get("http://api.icndb.com/jokes/random")
            joke = json.loads(api_request.content)
        except Exception:
            joke = "Error..."
        return render_template("Chuck_norris.html", text=html.unescape(joke["value"]["joke"]))
    else:
        return render_template("Chuck_norris.html", text="")

@app.route('/parse')
def parse():
    return render_template("parse.html")

@app.route('/css')
def css():
    return render_template("css.html")

@app.route('/gallery')
def gallery():
    relevant_path = "C:\\Users\Rollie\Documents\Python Scripts\Problems\Mike's Playground\static\images"
    included_extensions = ['jpg','jpeg', 'png', 'gif']
    file_names = [fn for fn in os.listdir(relevant_path)
        if any(fn.endswith(ext) for ext in included_extensions)]
    
    return render_template("gallery.html", images = file_names)

@app.route('/posts', methods=['GET', 'POST'])
def posts():

    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts.html', posts=all_posts)

@app.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')

@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    
    post = BlogPost.query.get_or_404(id)

    if request.method == 'POST':
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html', post=post)

@app.route('/posts/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('new_post.html')

@app.route('/parsing')
def parsing():
    page = "https://forecast.weather.gov/MapClick.php?lat=40.7146&lon=-74.0071#.XyMUXOdn2Uk"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(page, headers = headers)
    #response.status_code
    soup = BeautifulSoup(response.content, "html.parser")
    week = soup.find(id = "seven-day-forecast-body")

    items = week.find_all(class_ = "tombstone-container")

    items[0].find(class_ = "period-name").get_text()
    items[0].find(class_ = "short-desc").get_text()
    items[0].find(class_ = "temp").get_text()

    #list comprehension
    period_names = [item.find(class_ = "period-name").get_text() for item in items]
    short_descriptions = [item.find(class_ = "short-desc").get_text() for item in items]
    temperatures = [item.find(class_ = "temp").get_text() for item in items]

    return render_template('parsing.html', period = period_names, descriptions = short_descriptions, temperature = temperatures)

if __name__ == "__main__":
    app.run(debug=True)