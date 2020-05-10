from flask_wtf import Form
from wtforms.fields.html5 import URLField
from wtforms import StringField
from wtforms.validators import DataRequired, url
class BookmarkForm(Form):
    url = URLField('The URL for your bookmark:', validators=[DataRequired(), url()])
    description = StringField('Add an optional description: ')
