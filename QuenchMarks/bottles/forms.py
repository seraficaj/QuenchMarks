from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class BottlePostForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    brand = StringField("Brand", validators=[DataRequired()])
    material = StringField("Text", validators=[DataRequired()])
    submit = SubmitField("Post")