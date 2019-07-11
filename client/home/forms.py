from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import StringField, SelectField, SubmitField


class Base(FlaskForm):
    project = StringField(label='Project:',
                          validators=[validators.DataRequired()])
    filter_by = SelectField(label='Filter by:',
                            validators=[validators.DataRequired()],
                            choices=[('fix_version', 'Fix Version')])
    fix_version = StringField(label='Fix version:',
                              validators=[validators.Optional()])
    generate = SubmitField(label='GENERATE REPORT')
