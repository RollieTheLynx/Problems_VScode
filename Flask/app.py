# https://www.youtube.com/watch?v=3mwFC4SHY-Y&t=3724s
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text, nullable = False)
    author = db.Column(db.String(20), nullable = False, default = 'N/A')
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return "Blogpost " + str(self.id)


all_posts = [
    {
        "title": "Post 1",
        "content": "This is the content 1",
        "author": "Chuck"
    },
    {
        "title": "Post 2",
        "content": "This is the content 2"
    }
]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/posts', methods = ['GET', 'POST'])
def posts():
    if request.method == "POST":
        post_title = request.form["title"]
        post_content = request.form["content"]
        post_author = request.form['author']
        new_post = BlogPost(title = post_title, content = post_content, author = post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect("/posts")
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template("posts.html", posts = all_posts)

@app.route('/home/<string:name>/<int:id>') #decorator /or www.example.com
def hello(name):
    return "Hello " + name + ", your ID is " + id

@app.route("/onlyget", methods=['GET'])
def get_req():
    return "You can only get this page"

if __name__ == "__main__":
    app.run(debug=False)
