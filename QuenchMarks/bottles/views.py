from cgitb import text
from flask import render_template, url_for, request, redirect, flash, Blueprint
from flask_login import current_user, login_required
from QuenchMarks import db
from QuenchMarks.models import Bottle, Review
from QuenchMarks.bottles.forms import BottlePostForm, BottleUpdateForm

bottles = Blueprint("bottles", __name__)


# INDEX BOTTLES
@bottles.route("/bottles/")
def index():
    bottles = Bottle.query.order_by(Bottle.name.asc()).all()
    return render_template("bottles/bottle_index.html", bottles=bottles)


@bottles.route("/bottles/<int:id>")
def bottle_detail(id):
    bottle = Bottle.query.filter_by(id=id).first_or_404()
    reviews = Review.query.filter_by(bottle_id=id)
    return render_template(
        "bottles/bottle_detail.html", bottle=bottle, reviews=reviews
    )


# CRUD FOR BOTTLES


# CREATE A BOTTLE
@bottles.route("/bottles/create", methods=["GET", "POST"])
@login_required
def create_bottle():
    form = BottlePostForm()

    if form.validate_on_submit():
        print(form)
        new_bottle = Bottle(
            name=form.name.data,
            brand=form.brand.data,
            material=form.material.data,
            volume=form.volume.data,
        )
        db.session.add(new_bottle)
        db.session.commit()
        flash("Bottle Created")
        return redirect(url_for("bottles.index"))
    return render_template("bottles/create_bottle.html", form=form)


# UPDATE A BOTTLE INFO
@bottles.route("/bottles/<int:id>/update", methods=["GET", "POST"])
@login_required
def update_bottle(id):
    # get bottle
    bottle = Bottle.query.get_or_404(id)
    # pre-populate edit form
    updateForm = BottleUpdateForm()
    updateForm.name.data = bottle.name
    updateForm.brand.data = bottle.brand
    updateForm.material.data = bottle.material
    updateForm.volume.data = bottle.volume

    if updateForm.validate_on_submit():
        bottle.name = updateForm.name.data
        bottle.brand = updateForm.brand.data
        bottle.material = updateForm.material.data.lower()
        bottle.volume = updateForm.volume.data
        db.session.commit()
        return redirect(url_for("bottles.index"))
    return render_template("bottles/edit_bottle.html", form=updateForm, bottle=bottle)


# DELETE A BOTTLE
@bottles.route("/bottles/<int:id>/delete", methods=["GET", "POST"])
@login_required
def delete_bottle(id):
    bottle = Bottle.query.get_or_404(id)
    db.session.delete(bottle)
    db.session.commit()
    return redirect(url_for("bottles.index"))
