from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, current_user, logout_user
from .models import User
from .forms import RegisterForm
from src.extensions.db import db

bp = Blueprint("auth", __name__, template_folder="./templates")


@bp.route("/login", methods=["GET", "POST"])
def Login():
    if current_user.is_authenticated:
                 
        return redirect(url_for("requests.create_request"))
    
    
    
    if request.method == "GET":
        return render_template("auth/login.html")
    else:
        data = request.form
        username = data.get("username", None)
        password = data.get("password", None)
         
        if username == None or password == None:
            flash("The user or password are incorrect. Try Again", category="Error") 
        
        
        
        user_by_user_name = User.query.filter_by(username=username).one_or_none()
    
        if user_by_user_name == None:
            flash("The user or password are incorrect. Try Again", category="Error") 
            return render_template("auth/login.html")
        
        if not check_password_hash(user_by_user_name.password, password):
            flash("The user or password are incorrect. Try Again", category="Error") 
            return render_template("auth/login.html")
    
        
        print(user_by_user_name.id)
        user_instance = User.query.get(user_by_user_name.id)
    
        
        
        login_user(user=user_instance, remember=True)
        
        
        return redirect(url_for("requests.create_request"))
    
    
        
@bp.route("/register", methods=["GET", "POST"])
def Register():
    if request.method == "GET":
        form = RegisterForm()
        return render_template("auth/register.html", form=form)
    
    else:
        form = RegisterForm(request.form)
        if not form.validate_on_submit():
            
            return render_template("auth/register.html", form=form)

        
        
        username = form.username.data

        user_by_username = User.query.filter_by(username=username).one_or_none()

        if user_by_username != None:
            flash("El nombre de usuario ya esta registrado", category="Error")            
            return render_template("auth/register.html", form=form)
    
            
        pwd_hash = generate_password_hash(form.password.data)

        create = User(
            username = username,
            password = pwd_hash
        )
        db.session.add(create)
        db.session.commit()
                
        
        return render_template("auth/register.html", form=form)
  
@bp.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()                 

    return redirect(url_for('auth.Login'))
  
    