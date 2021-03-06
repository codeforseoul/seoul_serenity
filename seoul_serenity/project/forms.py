from flask_wtf import Form

from wtforms import TextField, PasswordField
from wtforms.fields.html5 import DateField


from wtforms.validators import DataRequired, Email, EqualTo, Length

# from .models import User
from .models import Project

class RegisterProjectForm(Form):
	name = TextField('Project', validators=[DataRequired(), Length(min=3)])

	start_date = DateField('Start Date', validators=[DataRequired()])
	end_date = DateField('End Date', validators=[DataRequired()])
	description = TextField('Description', validators=[Length(min=0)])

	## TODO : session id ( users.id )  
	# created_user_id = session['username']

	def __init__(self, *args, **kwargs):
		super(RegisterProjectForm, self).__init__(*args, **kwargs)
        # self.user = None

	def validate(self):
		return True
