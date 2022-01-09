from flask import render_template, url_for, request, redirect, flash, Blueprint
from flask_login import current_user, login_required
from QuenchMarks import db
from QuenchMarks.models import Review
from .forms import ReviewForm

reviews = Blueprint("reviews", __name__)

# CREATE A REVIEW
@reviews.route("/bottles/<int:id>/addreview", methods=["GET", "POST"])
@login_required
def create_review(id):
    form = ReviewForm()
    if form.validate_on_submit():
        print(form)
        flash("Review Created")
        return redirect(url_for("bottles.index"))
    return render_template("reviews/add_review.html", form=form)


# DELETE A REVIEW