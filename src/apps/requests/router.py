from flask import Blueprint, request, redirect, url_for
from flask import render_template
from flask_login import login_required
from .forms import RequestsForm
from .models import Requests
from src.extensions.db import db

bp = Blueprint("requests", __name__, template_folder="./templates")


@bp.route("/requests")
@login_required
def requests_list():
    requests = Requests.query.all()

    return render_template("request/request-list.html", requests=requests)


@bp.route("/create-requests", methods=["GET", "POST"])
@login_required
def create_request():
    if request.method == "GET":
        form = RequestsForm()
               
        print(form.errors)
               
        return render_template("request/request-create.html", form=form)

        
    else:
        form = RequestsForm(request.form)
               
        print(form.errors)
               
               
        if form.validate_on_submit():
            create = Requests(
                name = form.name.data,
                mount = form.mount.data,
                reason = form.reason.data,
                discount = form.discount.data,
                deadlines = form.deadlines.data,
                location = form.location.data,
                state = "Pendiente"
            )

            db.session.add(create)
            db.session.commit()
            
            return redirect(url_for('requests.requests_list'))

        return render_template("request/request-create.html", form=form)


        
        



