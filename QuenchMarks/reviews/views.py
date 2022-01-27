from flask import abort, render_template, url_for, request, redirect, flash, Blueprint
from flask_login import current_user, login_required
from werkzeug import datastructures
from QuenchMarks import db
from QuenchMarks.models import Bottle, Review
from .forms import ReviewForm

reviews = Blueprint("reviews", __name__)

# DEBUGGING = SEE ALL REVIEWS

# CREATE A REVIEW
@reviews.route("/bottles/<int:id>/addreview", methods=["GET", "POST"])
@login_required
def create_review(id):

    form = ReviewForm()

    if form.validate_on_submit():
        review = Review(
            rating = form.rating.data,
            text = form.text.data,
            author = current_user.id,
            bottle_id = Bottle.query.filter_by(id=id).first_or_404().id
        )
        db.session.add(review)
        db.session.commit()
        flash("Review Created")
        return redirect(url_for("bottles.bottle_detail", id=id))
    return render_template("reviews/input_review.html", form=form)

# UPDATE A REVIEW
@reviews.route("/updatereview/<int:id>", methods=["GET", "POST"])
@login_required
def update_review(id):

    review = Review.query.get_or_404(id)
    form = ReviewForm()

    if current_user.id != review.author.id:
        abort(403)

    if form.validate_on_submit():
        review.rating = form.rating.data
        review.text = form.text.data
        db.session.commit()
        flash("Review Created")
        return redirect(url_for("bottles.index"))
    return render_template("reviews/input_review.html", form=form)

# DELETE A REVIEW
@reviews.route("/deletereview/<int:id>", methods=["GET", "POST"])
@login_required
def delete_review(id):
    review = Review.query.get_or_404(id)
    bottle_id = review.bottle_id
    if current_user.id == review.author:
        db.session.delete(review)
        db.session.commit()
    else:
        abort(403)
    return redirect(url_for("bottles.detail", id=bottle_id))