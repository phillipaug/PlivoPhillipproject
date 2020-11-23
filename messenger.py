from datetime import datetime
from flask import Flask, request, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from forms import SendMessageForm
import plivo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = "SECRETKEY"
db = SQLAlchemy(app)

######## PLIVO API CONFIG ##########
##### plivo.RestClient("Auth ID", "Auth Token") #####
client = plivo.RestClient("SAYTFKM2E1YJYZNJZHMT","YTUxZDBlMGM1MjUyZTNmZTBkNWQ0MjM4ZTdhOTlk")
##### Plivo App Phone Number #####
PPNUMBER = '+14082394955'

class Message(db.Model):
    __tablename__= 'message'
    id = db.Column(db.Integer, primary_key=True)
    pnumber = db.Column(db.String, nullable=False)
    message = db.Column(db.String(), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 
    sender = db.Column(db.Boolean, nullable=False)
    

    def __repr__(self):
        return f"Messages('{self.pnumber}', '{self.time}', '{self.message}', '{self.sender}')"

def send_sms(to, body):
    """
    function for sending sms
        to = destination number
        body = message body
    """
    client.messages.create(
        src=PPNUMBER,
        dst='+'+to,
        text=body
    )
    return

def unique_nums_indb():
    arr = []
    for value in Message.query.with_entities(Message.pnumber).distinct():
        arr.append(value[0])
    return arr

@app.route('/')
@app.route('/home')
def index():
    image_file = url_for('static', filename='image.jpg')
    return render_template('home.html', image_file=image_file)

@app.route('/send-message', methods=['GET', 'POST'])
def send_message():
    """
    function that takes input from form and validates.
        takes the input and sends the message, and adds the message to message db.
    """
    form = SendMessageForm()
    if form.validate_on_submit():
        send_sms(form.pnumber.data, form.message.data)
        message = Message(pnumber = form.pnumber.data, message=form.message.data, time=datetime.utcnow(), sender=True)
        db.session.add(message)
        db.session.commit()
        flash(f'Message, ({form.message.data}) sent to {form.pnumber.data}!', 'success')
        return redirect(url_for('list_message'))
    return render_template('send_message.html', title='Send Message', form=form)

@app.route('/list-messages', methods=['GET', 'POST'])
def list_message():
    """
    function that lists all the messages from the db
        takes input from form and filters either by date or phone number
    """
    HTML = 'list_messages.html'
    TITLE = 'Message History'
    numbers=unique_nums_indb()
    if request.method == 'POST':
        pnumber = request.form['pnumber']
        sdate = request.form['sdate']
        print(sdate)
        edate = request.form['edate']
        print(edate)
        if pnumber == '' or pnumber == 'Choose number':
            if edate == '':
                return render_template(HTML, title=TITLE, pnumbers=numbers, messages=Message.query.filter(Message.time>=sdate))
            return render_template(HTML, title=TITLE, pnumbers=numbers, messages=Message.query.filter(Message.time>=sdate).filter(Message.time<=edate))
        else:
            if edate == '':
                return render_template(HTML, title=TITLE, pnumbers=numbers, messages=Message.query.filter(Message.time>=sdate).filter(Message.pnumber==pnumber))
            return render_template(HTML, title=TITLE, pnumbers=numbers, messages=Message.query.filter(Message.time>=sdate).filter(Message.time<=edate).filter(Message.pnumber==pnumber))    
    return render_template(HTML, title=TITLE, pnumbers=numbers, messages=Message.query.all())


@app.route('/receive_sms', methods=['GET', 'POST'])
def inbound_sms():
    """
    function that uses Plivo API to get incoming messages
    takes the messages and adds to message db
    """
    from_number = request.values.get('From')
    to_number = request.values.get('To')
    text = request.values.get('Text')
    print('Message received - From: %s, To: %s, Text: %s' %(from_number, to_number, text))

    message = Message(pnumber=from_number, message=text, time=datetime.utcnow(), sender=False)
    db.session.add(message)
    db.session.commit()

    return 'Message Recevived'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)