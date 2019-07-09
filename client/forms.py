from wtforms.fields import StringField, SelectField


class Base:
    project = StringField()
    filter_by = SelectField()
    fix_version = StringField()
