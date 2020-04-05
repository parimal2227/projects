from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '9b9ab03473d5733c41b5e88d22cca1df'

posts = [
    {
        'author': 'parimal',
        'title': 'first blog',
        'content': 'First Content',
        'dateposted': 'Jan 31 2020'
    },
    {
        'author': 'kumar',
        'title': 'second blog',
        'content': 'Second Content',
        'dateposted': 'Jan 31 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='home page')


@app.route('/about')
def about():
    return render_template('about.html', title='about page')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'asdf' :
            flash('Logged In Succesfully', 'success')
            return redirect(url_for('home'))
        else:
            flash('Log In Failure', 'danger')
    return render_template('login.html', title='LogIn', form=form)


if __name__ == '__main__':
    app.run(debug=True)
