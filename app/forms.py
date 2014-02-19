from flask.ext.wtf import Form
from wtforms.fields import TextField, BooleanField
from wtforms.validators import Required

class ListItem(Form):
	additem = TextField('item', validators = [Required()])