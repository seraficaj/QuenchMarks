from flask import render_template, url_for, request, redirect, flash, Blueprint
from flask_login import current_user, login_required
from QuenchMarks import db
from QuenchMarks.models import Bottle
from QuenchMarks.bottles.forms import BottlePostForm, BottleUpdateForm

bottles = Blueprint("bottles", __name__)

@bottles.route("/bottles/")
def index():
    bottles = Bottle.query.order_by(Bottle.name.asc()).all()
    print(bottles)
    return render_template("bottles/bottle_index.html", bottles=bottles)

@bottles.route("/bottles/<id>")
def bottle_detail(id):
    bottle = Bottle.query.filter_by(id=id).first_or_404()
    return render_template('bottles/bottle_detail.html', bottle=bottle)
    

@bottles.route("/bottles/create", methods=["GET", "POST"])
# @login_required
def create_bottle():
    form = BottlePostForm()

    if form.validate_on_submit():
        print(form)
        new_bottle = Bottle(
            name=form.name.data,
            brand=form.brand.data,
            material=form.material.data,
            volume=form.volume.data
        )
        db.session.add(new_bottle)
        db.session.commit()
        flash("Bottle Created")
        return redirect(url_for("core.index"))
    return render_template("bottles/create_bottle.html", form=form)


@bottles.route("/bottles/<id>/update", methods=["GET", "POST"])
# @login_required
def update_bottle(id):
    updateForm = BottleUpdateForm()
    bottle = Bottle.query.get_or_404(id)
    if updateForm.validate_on_submit():
        bottle.name=updateForm.name.data
        bottle.brand=updateForm.brand.data
        bottle.material=updateForm.material.data
        bottle.volume=updateForm.volume.data
        db.session.commit()
        return redirect(url_for('bottles.index'))
    return render_template('bottles/edit_bottle.html', form=updateForm, bottle=bottle)