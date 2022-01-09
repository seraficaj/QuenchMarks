from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired


class ReviewForm(FlaskForm):
    rating = IntegerField("Rating", validators=[DataRequired()])
    text = TextAreaField("Text", validators=[DataRequired()])
    submit = SubmitField("Add Review")