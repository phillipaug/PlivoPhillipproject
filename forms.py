from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, DataRequired, ValidationError
import phonenumbers

class SendMessageForm(FlaskForm):
    pnumber = StringField('Phone Number', validators=[DataRequired()])
    message = StringField('Message Body')
    send = SubmitField("Send Message")

    def validate_phone(self, phone):
        try:
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError('Invalid phone number')

