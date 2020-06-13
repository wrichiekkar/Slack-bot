from selenium import webdriver
import time
from PIL import Image
from io import BytesIO

proxyDict = {  # Proxy for requests (Does not work on corporate network so using proxy)
              'http': 'ENTER PROXY',
              'https': 'ENTER PROXY'
            }

# Created this method to work easily with slack
def call_from_slackbot():
    Link1 = "ENTER LINK"
    Link2 = "ENTER LINK"
    Link3 = "ENTER LINK"
    Link4 = "ENTER LINK"
    Link5 = "ENTER LINK"
    
    get_score(Link1, Link2, Link3, Link4, Link5)

def get_score(Link1, Link2, Link3, Link4, Link5):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    s = webdriver.Chrome(executable_path="chromedriver.exe", options=options)  # Set up Selenium session

    s.get(Link1)  # Get page
    s.find_element_by_id('Email').send_keys('ENTER EMAIL')  # Type in email
    s.find_element_by_class_name('btn-primary').click()  # Click submit
    s.find_element_by_id('Password').send_keys('ENTER PASSWORD')  # Type in password
    s.find_element_by_class_name('btn-primary').click()  # Click submit

    time.sleep(2)  # Sleep to load in score
    TotScore = s.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div[2]/div[2]/div[1]')  # Get Score

    top, left, right, bottom = get_size(TotScore)
    png = s.get_screenshot_as_png()  # saves screenshot of entire page
    im = Image.open(BytesIO(png))  # uses PIL library to open image in memory
    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('FILENAME.png')  # saves new cropped image


    s.get(Link2)
    time.sleep(2)  # Sleep to load in score
    BellEN = s.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div[2]/div[2]/div[1]')  # Get Score

    top, left, right, bottom = get_size(BellEN)
    png = s.get_screenshot_as_png()  # saves screenshot of entire page
    im = Image.open(BytesIO(png))  # uses PIL library to open image in memory
    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('FILENAME.png')  # saves new cropped image


    s.get(Link3)
    time.sleep(2)  # Sleep to load in score
    BellFR = s.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div[2]/div[2]/div[1]')  # Get Score

    top, left, right, bottom = get_size(BellFR)
    png = s.get_screenshot_as_png()  # saves screenshot of entire page
    im = Image.open(BytesIO(png))  # uses PIL library to open image in memory
    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('FILENAME.png')  # saves new cropped image


    s.get(Link4)
    time.sleep(2)  # Sleep to load in score
    SupEN = s.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div[2]/div[2]/div[1]')  # Get Score
    top, left, right, bottom = get_size(SupEN)
    png = s.get_screenshot_as_png()  # saves screenshot of entire page
    im = Image.open(BytesIO(png))  # uses PIL library to open image in memory

    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('FILENAME.png')  # saves new cropped image


    s.get(Link5)
    time.sleep(2)  # Sleep to load in score
    SupFR = s.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div[2]/div[2]/div[1]')  # Get Score
    top, left, right, bottom = get_size(SupFR)
    png = s.get_screenshot_as_png()  # saves screenshot of entire page
    im = Image.open(BytesIO(png))  # uses PIL library to open image in memory

    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('FILENAME.png')  # saves new cropped image

    s.close()

def get_size(xpath):

    location = xpath.location
    size = xpath.size

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    return top, left, right, bottom


if __name__ == "__main__":
    Link1 = "ENTER LINK"
    Link2 = "ENTER LINK"
    Link3 = "ENTER LINK"
    Link4 = "ENTER LINK"
    Link5 = "ENTER LINK"

    get_score(Link1, Link2, Link3, Link4, Link5)


