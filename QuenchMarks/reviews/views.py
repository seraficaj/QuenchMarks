from flask import render_template, url_for, request, redirect, flash, Blueprint
from flask_login import current_user, login_required
from QuenchMarks import db
from QuenchMarks.models import Review

reviews = Blueprint("reviews", __name__)

# CREATE A REVIEW
@reviews.route("/bottles/<int:id>/addreview", methods=["GET", "POST"])
@login_required
def create_review(id):
    # form = ReviewPostForm()

    # if form.validate_on_submit():
    #     print(form)
    #     new_review = Review(
    #         name=form.name.data,
    #         brand=form.brand.data,
    #         material=form.material.data.lower(),
    #         volume=form.volume.data
    #     )
    #     db.session.add(new_review)
    #     db.session.commit()
    #     flash("Review Created")
    #     return redirect(url_for("bottles.index"))
    return render_template("reviews/add_review.html")


# DELETE A REVIEW