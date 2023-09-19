from flask import Blueprint, request, redirect, url_for
from flask import render_template, request
from flask_login import login_required
from .forms import RequestsForm
from .models import Requests
from src.extensions.db import db
from .schemas import RequestOut


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
                state = "pendiente"
            )

            db.session.add(create)
            db.session.commit()
            
            return redirect(url_for('requests.requests_list'))

        return render_template("request/request-create.html", form=form)


  
  
  
@bp.route("/api/get-requests")
@login_required
def request_api(): 
    requests_pendientes = Requests.query.filter_by(state="pendiente").all()
    requests_proceso = Requests.query.filter_by(state="proceso").all()
    requests_completado = Requests.query.filter_by(state="completada").all()
    
    request_out = RequestOut(many=True)
    
    return {
        "pendientes": request_out.dump(requests_pendientes),
        "proceso": request_out.dump(requests_proceso),
        "completadas": request_out.dump(requests_completado)
    }      



@bp.route("/api/edit-requests", methods=["POST"])
@login_required
def edit_request():
    if not request.is_json:
        return {
            "error": "Format data invalid must be a JSON"
        }, 422
    
    data = request.json

    id = data.get("id", None)
    
    if id == None:
        return {
            "error": "the id is required"
        }, 422
    
    state = data.get("state", None)
    if state == None:
        return {
            "error": "the state is required"
        }, 422
    

    request_by_id = Requests.query.filter_by(id=id).one_or_none()
    
    if request_by_id == None:
        return {
            "error": "this request not exists"
        }, 404

    if state == "pendiente" or state == "proceso" or state == "completada":
        request_instance = Requests.query.get(id)
        request_instance.state = state
        db.session.commit()
        
        
        return {
            "message": "Request change"
        }
    else:
        return {
            "error": "Invalid state option"
        }, 422
    
@bp.route("/api/delete-requests", methods=["POST"])
@login_required   
def delete_request():
    if not request.is_json:
        return {
            "error": "Format data invalid must be a JSON"
        }, 422
    
    data = request.json

    id = data.get("id", None)
    
    
    if id == None:
        return {
            "error": "the id is required"
        }, 422
    
    
    request_by_id = Requests.query.filter_by(id=id).one_or_none()
    
    if request_by_id == None:
        return {
            "error": "this request not exists"
        }, 404
    
    
    request_instance = Requests.query.get(id)
    db.session.delete(request_instance)
    db.session.commit()
    
    return {
        "message":"Request deleted"
    }
    