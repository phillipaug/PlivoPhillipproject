


#feedback for the interview: Add path installer for packages as it can get messy with vscode, because it installs globally and not with the specified interpreter

 #SMSframework compatibility could be beneficial
from flask import Flask, render_template, request
import plivo

app = Flask(__name__)
client = plivo.RestClient("SAYTFKM2E1YJYZNJZHMT", "YTUxZDBlMGM1MjUyZTNmZTBkNWQ0MjM4ZTdhOTlk") #auth_id and auth_token

@app.route('/')
def index():
    return render_template('page.html')

@app.route('/send', methods=['POST'])
def send():
    client.messages.create( src = '+14082394955', dst = '+15127126800' , text = 'Hello')
    return inbound_sms()

@app.route('/', methods=['GET', 'POST'])
def inbound_sms():

    from_number = request.values.get('From')
    to_number = request.values.get('To')
    text = request.values.get('Text')
    print('Message Sent - From: %s, To: %s, Text: %s' %(from_number, to_number, text))

    return 'Message Sent'

    """
    def get_sms(self, message_uuid=None, params=None):
        ''' Get SMS info.
            Ref: http://plivo.com/docs/api/message/
            :rtype: dict
        '''
        endpoint = urljoin(self.api_url, 'Account/%s/Message/' % self.auth_id)

        if message_uuid:
            endpoint = urljoin(endpoint, message_uuid)

        result = self._requests('GET', endpoint, params, False)
        return result

    def get_all_sms(self, params=None):
        ''' Get all SMS log data '''
        log_data = self.get_sms(params=params)
        yield log_data['objects']

        while log_data['meta']['next']:
            log_data = self._requests('GET', urljoin(self.api_url,
                    log_data['meta']['next']))
            yield log_data['objects']

    def get_account(self):
        ''' Get Account info
            Ref: http://plivo.com/docs/api/account/
            :rtype: dict
        '''
        endpoint = urljoin(self.api_url, 'https://api.plivo.com/v1/Account/SAYTFKM2E1YJYZNJZHMT/Message/' % self.auth_id)
        result = self._requests('GET', endpoint)
        return result
        """
if __name__ == '__main__':
    app.run(debug=True)
