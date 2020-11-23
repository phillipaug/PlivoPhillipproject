# Plivo-SMSWebAppPhillip 

Hi! This is a SMS web application using Flask, a web development framework written in Python. This web app uses a Plivo phone number and the Plivo API
to send and receive SMS messages. The web app also has the ability to show and filter your message history. 

## How to send a message using Python (basic)
1- open the file sendmessage.py either by typing python sendmessage.py or run in the terminal using your favorite program
To send the message to a specific number change (dst='desired number'), to customize the message change  (text='your text')
   
2-To check message records open the file record.py and it should appear in the terminal the last message logs




## To build and deploy the web app: (in dev)

### 1. Create a local directory
$ mkdir 'directory name'

$ sudo apt-get install -y python python-pip python-virtualenv

### 2. Setup a virtual env and install the requirements 
$ virtualenv env

You will also need to install all the dependencies in the requirements file

### 3. Note: Still have some debugging to do, but the Sendmessage.py and record.py files work.

### 4. Configure the variables 
There are a few variables that you can change to turn this into your own webapp.

The most important ones are in messenger.py. 
You will need to put in your own Plivo Auth ID, Auth Token, and phone number.

There are also some html changes you can make to change the name of the website, the about me section, etc.

### 5. Deploy the app
$ python messenger.py
Your webapp is now running! You can visit http://localhost:5000 to view your website

### 6. Expose your application to the internet using ngrok 
I used Ngrok to expose the web server to the internet. It is a free tunneling software. 

### 7. Send your first message!
