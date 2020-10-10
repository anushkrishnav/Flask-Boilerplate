from flask import render_template, redirect, flash, url_for
from flask_login import current_user, login_user, logout_user
from .model.models import User
from application import appp
from .forms import LoginForm


@appp.route('/')
def redir():
    return redirect('/index')


@appp.route("/index")
@appp.route("/home")
def index():
    return render_template('index.html', index=True)


@appp.route("/blog")
def blog():
    return render_template('blog.html', blog=True)


@appp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@appp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@appp.route("/events")
def events():
    return render_template('events.html', events=True)


'''
@appp.route("/register",methods=['POST','GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        userID = GetIndex()
        userID += 1
        username = form.username.data
        email = form.email.data
        Github = form.Github.data
        linkdln = form.linkdln.data
        Tech = form.Tech.data
# SetData(userID,username,email,Github,linkdln,Tech)
        flash("You are successfully registered!", "success")
        return redirect(url_for('index'))
    return render_template(
        "register.html",
        title="Want to Mentor ? Register with Us",
        form=form, register=True)


# @appp.route("/user")
# def user():
#    User(UserId=1,
# username="anush",
# email="anush.venkatakrishna@gmail.com",
# Github_Url="",linkdln_Url="",Technologies="python ,c").save()
#   User(UserId=2,username="anushk",email="anush@gmail.com",Github_Url="xc",
#  linkdln_Url="xx",Technologies="python ,c").save()


# @appp.route('/test')
# def test():
#     data = GetTable()
#     data = data[0][2]
#     return render_template('test.html', data=data)
'''