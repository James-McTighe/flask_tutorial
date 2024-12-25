from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': "James Mctighe",
        'title' : 'blog post 1',
        'content' : 'first post content',
        'date_posted' : 'April 20th 2018',
    },
    {
       'author': "Jon Alsip",
        'title' : 'blog post 2',
        'content' : 'Second post content',
        'date_posted' : 'April 21th 2018', 
    }
]

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title=about)


if __name__ == "__main__":
    app.run(debug=True)