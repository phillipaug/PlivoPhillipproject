import plivo

client = plivo.RestClient("SAYTFKM2E1YJYZNJZHMT", "YTUxZDBlMGM1MjUyZTNmZTBkNWQ0MjM4ZTdhOTlk")
response = client.messages.create(
    src='+14082394955',
    dst='+15127126800',
    text='Hello! Im testing my app!'
    #url='http://foo.com/sms_status/',
)
print(response)
# prints only the message_uuid
print(response.message_uuid)