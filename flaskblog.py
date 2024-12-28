from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a19b0a880bb9062865cd17e523db0ddf'

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
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title=about)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title="login", form=form)

if __name__ == "__main__":
    app.run(debug=True)