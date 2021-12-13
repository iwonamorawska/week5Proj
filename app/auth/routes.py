from flask import Blueprint, render_template, request, redirect, url_for

from .forms import UserInfoForm
from app.models import User, Post

auth= Blueprint('auth',__name__, template_folder="auth_template")
from app.models import db
@auth.route('/login')
def logIn():
    return render_template('login.html')

@auth.route('/signup', methods=["GET", "POST"])
def signUp():
    my_form= UserInfoForm()
    if request.method == "POST":
        if my_form.validate():
            
            username=my_form.username.data
            email=my_form.email.data
            password=my_form.password.data 
            
            user=User(username,email, password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            print("not validated")
    
    return render_template('signup.html', form=my_form )
