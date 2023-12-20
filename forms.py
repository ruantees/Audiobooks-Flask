from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length


class RegisterForm(FlaskForm):
    email = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Email"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    fullname = StringField(validators=[
        InputRequired(), Length(min=0, max=40)], render_kw={"placeholder": "Full Name"})

    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Email"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


class UpdateForm(FlaskForm):
    fullname = StringField(validators=[
        InputRequired(), Length(min=0, max=40)], render_kw={"placeholder": "Full Name"})

    submit = SubmitField('Update')


class ContactForm(FlaskForm):
    email = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Email"})

    fullname = StringField(validators=[
        InputRequired(), Length(min=0, max=40)], render_kw={"placeholder": "Full Name"})

    file = FileField('Upload File')

    submit = SubmitField('Send Message')
