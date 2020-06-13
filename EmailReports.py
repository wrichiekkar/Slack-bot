from selenium import webdriver
from PIL import Image
from io import BytesIO
import urllib.parse
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import requests


proxyDict = {  # Proxy for requests (Does not work on corporate network so using proxy)
              'http': 'ENTER PROXY',
              'https': 'ENTER PROXY'
            }
user = 'ENTER EMAIL' #  email
api_key = 'ENTER API KEY'  # api key for password

def Slackbot_Screenshot():
    Link2 = "ENTER LINK"
    Link3 = "ENTER LINK"
    Link4 = "ENTER LINK"
    Link5 = "ENTER LINK"

    get_ss(Link2, Link3, Link4, Link5)
    Email_Screenshot()

def Slackbot_Text():
    Score1, Score2, Score3, Score4, Score5 = get_score()
    Email_Text(Score1, Score2, Score3, Score4, Score5)

def get_ss(Link2, Link3, Link4, Link5):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # Remove UI
    options.add_argument("window-size=1920x1080")
    s = webdriver.Chrome(executable_path="chromedriver.exe", options=options)  # Set up Selenium session

    s.get(Link2)  # Get page
    s.find_element_by_id('Email').send_keys('ENTER EMAIL')  # Type in email
    s.find_element_by_class_name('btn-primary').click()  # Click submit
    s.find_element_by_id('Password').send_keys('ENTER PASSWORD')  # Type in password
    s.find_element_by_class_name('btn-primary').click()  # Click submit
    time.sleep(3)  # Sleep to load in score
    Score2 = s.find_element_by_class_name('dci-overview-vm')  # Get Score

    top, left, right, bottom = get_size(Score2)
    png = s.get_screenshot_as_png()  # saves screenshot of entire page
    im = Image.open(BytesIO(png))  # uses PIL library to open image in memory
    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('ER_Score2.png')  # saves new cropped image


    s.get(Link3)
    time.sleep(3)  # Sleep to load in score
    Score3 = s.find_element_by_class_name('dci-overview-vm')  # Get Score

    top, left, right, bottom = get_size(Score3)
    png = s.get_screenshot_as_png()  # saves screenshot of entire page
    im = Image.open(BytesIO(png))  # uses PIL library to open image in memory
    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('ER_Score3.png')  # saves new cropped image


    s.get(Link4)
    time.sleep(3)  # Sleep to load in score
    Score4 = s.find_element_by_class_name('dci-overview-vm')  # Get Score
    top, left, right, bottom = get_size(Score4)
    png = s.get_screenshot_as_png()  # saves screenshot of entire page
    im = Image.open(BytesIO(png))  # uses PIL library to open image in memory

    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('ER_Score4.png')  # saves new cropped image


    s.get(Link5)
    time.sleep(3)  # Sleep to load in score
    Score5 = s.find_element_by_class_name('dci-overview-vm')  # Get Score
    top, left, right, bottom = get_size(Score5)
    png = s.get_screenshot_as_png()  # saves screenshot of entire page
    im = Image.open(BytesIO(png))  # uses PIL library to open image in memory

    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('ER_Score5.png')  # saves new cropped image

    s.quit()

def get_size(xpath):

    location = xpath.location
    size = xpath.size

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    return top, left, right, bottom

def get_score():
    data = requests.get('ENTER LINK', verify=False, auth=(user, api_key), proxies=proxyDict).json()
    Score1 = data.get("accessibility").get("total")

    data = requests.get('ENTER LINK', verify=False, auth=(user, api_key), proxies=proxyDict).json()
    Score2 = data.get("accessibility").get("total")

    data = requests.get('ENTER LINK', verify=False, auth=(user, api_key), proxies=proxyDict).json()
    Score3 = data.get("accessibility").get("total")

    data = requests.get('ENTER LINK', verify=False, auth=(user, api_key), proxies=proxyDict).json()
    Score4 = data.get("accessibility").get("total")

    data = requests.get('ENTER LINK', verify=False, auth=(user, api_key), proxies=proxyDict).json()
    Score5 = data.get("accessibility").get("total")

    return Score1, Score2, Score3, Score4, Score5

def Email_Screenshot():
    recipients = ['ENTER EMAIL'] #When using multiple recipients, the recipients in server.sendmail() has to be a list

    # create message object instance
    msg = MIMEMultipart('related') #This 'related' keyword is needed to get in-text embedded images!

    # setup the parameters of the message
    msg['From'] = "ENTER EMAIL"
    msg['To'] = ", ".join(recipients) # When using multiple recipients, the msg['To'] needs to be a string. The .join method converts to a list to a string
    msg['Subject'] = "Shop and Support Accessibility Scores"

    #Add inline embedded HTML images to the body
    Body = '<html><h3>Shop English:</h3><img src="cid:image1"><h3>Shop French:</h3><img src="cid:image2"><h3>Support English:</h3><img src="cid:image3"><h3>Support French:</h3><img src="cid:image4"><br><p>This is an automated email. For any questions, feel free to reach out to ENTER EMAIL</p></html>'
    htmlOBJECT = MIMEText(Body, 'html')
    msg.attach(htmlOBJECT)

    # attach screenshot to message body
    fp = open("FILENAME", 'rb') # Opens the image in the directory of the python script
    img = MIMEImage(fp.read())
    fp.close()
    img.add_header('Content-ID', '<image1>') # The headers are used to refer to attachments for the html 'cid'
    msg.attach(img) # Attaches the img to the cid in the html above

    fp = open("FILENAME", 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    img.add_header('Content-ID', '<image2>') 
    msg.attach(img)

    fp = open("FILENAME", 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    img.add_header('Content-ID', '<image3>')
    msg.attach(img) 

    fp = open("FILENAME", 'rb') 
    img = MIMEImage(fp.read())
    fp.close()
    img.add_header('Content-ID', '<image4>')
    msg.attach(img)


    #Send through SMTP service
    server = smtplib.SMTP('ENTER SMTP SERVER',25)
    server.sendmail(msg['From'], recipients, msg.as_string())
    server.quit()

def Email_Text(Score1, Score2, Score3, Score4, Score5):
    recipients = ['ENTER EMAIL'] #When using multiple recipients, must to be a list

    # create message object instance
    msg = MIMEMultipart('related') #This 'related' keyword is needed to get in-text embedded images!

    # setup the parameters of the message
    msg['From'] = "ENTER EMAIL"
    msg['To'] = ", ".join(recipients) # When using multiple recipients, the msg['To'] needs to be a string. The .join method converts to a list to a string
    msg['Subject'] = "Shop and Support Accessibility Scores"

    #Add inline embedded HTML images to the body
    Body = '<html><h3>Shop English: ' + str(Score2) +'</h3><h3>Shop French: ' + str(Score3) + '</h3><h3>Support English: ' + str(Score4) + '</h3><h3>Support French: ' + str(Score5) + '</h3><br><p>This is an automated email. For any questions, feel free to reach out to ENTER EMAIL</p></html>'
    htmlOBJECT = MIMEText(Body, 'html')
    msg.attach(htmlOBJECT)

    
    #Send through SMTP service
    server = smtplib.SMTP('ENTER SMTP SERVER',25)
    server.sendmail(msg['From'], recipients, msg.as_string())
    server.quit()

if __name__ == "__main__":
    requests.packages.urllib3.disable_warnings() #ignore SSL warning
    Link2 = "ENTER LINK"
    Link3 = "ENTER LINK"
    Link4 = "ENTER LINK"
    Link5 = "ENTER LINK"

    get_ss(Link2, Link3, Link4, Link5)
    Email_Screenshot()


