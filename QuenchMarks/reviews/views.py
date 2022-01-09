from flask import render_template, url_for, request, redirect, flash, Blueprint
from flask_login import current_user, login_required
from werkzeug import datastructures
from QuenchMarks import db
from QuenchMarks.models import Bottle, Review
from .forms import ReviewForm

reviews = Blueprint("reviews", __name__)

# DEBUGGING = SEE ALL REVIEWS

@reviews.route("/reviews", methods=["GET"])
def all_review():
    reviews = Review.query.order_by(Review.rating.asc()).all()
    print(reviews)
    return redirect(url_for("bottles.index"))

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
        return redirect(url_for("bottles.index"))
    return render_template("reviews/add_review.html", form=form)


# DELETE A REVIEW