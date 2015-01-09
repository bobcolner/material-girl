from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required, current_user
from . import matgirl
from .. import db
from .forms import WelcomeForm



@matgirl.route('/welcome')
def welcome():
    form = WelcomeForm()
    return render_template('matgirl/welcome.html', form=form)
