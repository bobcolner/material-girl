from flask import render_template, redirect, request, url_for, flash, jsonify
from flask.ext.login import login_user, logout_user, login_required, current_user
from . import matgirl
from .. import db
from ..models import User
from .forms import LoginForm, RegistrationForm

@matgirl.route('/')
@matgirl.route('/index')
@matgirl.route('/base')
def base():
    return render_template('matgirl/base.html')

@matgirl.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('matgirl/login.html', form=form)

@matgirl.route('/register')
def register():
    form = RegistrationForm()
    return render_template('matgirl/register.html', form=form)

@matgirl.route('/cards')
def cards():
    return render_template('matgirl/cards.html')

@matgirl.route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

