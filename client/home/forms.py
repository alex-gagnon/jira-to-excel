from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import StringField, SelectField, SubmitField


class Base(FlaskForm):
    project = SelectField(label='Project: ',
                          validators=[validators.DataRequired()],
                          choices=[('TM', 'Title Management'),
                                   ('TMT', 'Title Management Training'),
                                   ('REL', 'Release'),
                                   ('CUST', 'Customers')])
    filter_by = SelectField(label='Filter by: ',
                            validators=[validators.DataRequired()],
                            choices=[('fix_version', 'Fix Version'),
                                     ('latest_version', 'Latest Version')])
    version = StringField(label='Version: ',
                          validators=[validators.Optional()])
    generate = SubmitField(label='DOWNLOAD REPORT')
