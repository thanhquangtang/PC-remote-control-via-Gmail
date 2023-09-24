from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CLIENT_SECRET_FILE = 'client-secret-2.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

def sendMAC(target_email):
    emailMsg = 'MAC address'
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = target_email
    mimeMessage['subject'] = 'MAC address'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    print(message)

def sendShutdown(target_email):
    emailMsg = 'Shutdown'
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = target_email
    mimeMessage['subject'] = 'Shutdown'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    print(message)

def sendLogout(target_email):
    emailMsg = 'Logout'
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = target_email
    mimeMessage['subject'] = 'Logout'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    print(message)

def sendLivescreen(target_email):
    emailMsg = 'Livescreen'
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = target_email
    mimeMessage['subject'] = 'Livescreen'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    print(message)

def sendLoadRegistry(target_email, content):
    emailMsg = content
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = target_email
    mimeMessage['subject'] = 'Load registry'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    print(message)

def sendSaveRegistry(target_email):
    emailMsg = 'Save registry'
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = target_email
    mimeMessage['subject'] = 'Save registry'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    print(message)

def sendAppProcess(target_email):
    emailMsg = 'App process'
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = target_email
    mimeMessage['subject'] = 'App process'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    print(message)

def sendDirectoryTree(target_email, content):
    emailMsg = content
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = target_email
    mimeMessage['subject'] = 'Directory tree'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    print(message)