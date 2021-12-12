from flask import render_template, url_for, request, redirect, flash, Blueprint
from flask_login import current_user, login_required
from QuenchMarks import db
from QuenchMarks.models import Bottle
from QuenchMarks.bottles.forms import BottlePostForm

bottles = Blueprint("bottles", __name__)

@bottles.route("/create", methods=["GET", "POST"])
@login_required
def create_post():
    form = Bottle()

    if form.validate_on_submit():
        new_bottle = Bottle(
            
        )
        db.session.add(new_bottle)
        db.session.commit()
        flash("Bottle Created")
        return redirect(url_for("core.index"))
    return render_template("create_bottle.html", form=form)