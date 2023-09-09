from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class BottlePostForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    brand = StringField("Brand", validators=[DataRequired()])
    material = StringField("Material", validators=[DataRequired()])
    volume = IntegerField("Volume (mL)", validators=[DataRequired()])
    submit = SubmitField("Post")


class BottleUpdateForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    brand = StringField("Brand", validators=[DataRequired()])
    material = StringField("Material", validators=[DataRequired()])
    volume = IntegerField("Volume (mL)", validators=[DataRequired()])
    submit = SubmitField("Update Info")
