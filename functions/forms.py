from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, EqualTo

class NewUserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired('required')])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('New Password', 
        validators=[DataRequired(),
        EqualTo('confirm', message='Passwords must match')]
    )
    confirm = PasswordField('Repeat Password')

class Login(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class CreateBlog(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])


