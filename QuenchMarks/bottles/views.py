from flask import render_template, url_for, request, redirect, flash, Blueprint
from flask_login import current_user, login_required
from QuenchMarks import db
from QuenchMarks.models import Bottle
from QuenchMarks.bottles.forms import BottlePostForm

bottles = Blueprint("bottles", __name__)

@bottles.route("/bottles/index")
def index():
    bottles = Bottle.query.order_by(Bottle.name.asc()).all()
    print(bottles)
    return render_template("bottle_index.html")

@bottles.route("/bottles/create", methods=["GET", "POST"])
@login_required
def create_post():
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
    return render_template("create_bottle.html", form=form)