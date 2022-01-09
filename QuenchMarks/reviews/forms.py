from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, TextAreaField
from wtforms.widgets import html5
from wtforms.validators import DataRequired


class ReviewForm(FlaskForm):
    rating = IntegerField("Rating (1-5 Stars)", widget=html5.NumberInput(step=1,min=1, max=5), validators=[DataRequired()])
    text = TextAreaField("Text", validators=[DataRequired()])
    submit = SubmitField("Add Review")