# Slackbot
The objective of this project was to collect graphic scores (since pictures are always better :))  and post them to a slack channel when prompted. The slackbot is also to generate a report and send it out when prompted by the user.

EX: User: What is the score?
Accessibility Bot: The  score is: 57.5 (graphic 57.5).


<b>To start the slackbot, run Autorun.py (Change token in this file to autorun your bot)</b>

## Collect Graphic Scores
I used a headless selenium to collect the data required (requests or mechanize would not work). Selenium was used to login to a vendor's website (where the score was calculated) and take screenshots of various pages. The objective was to get graphic scores of specific sections in both English and French. Once the screenshot was taken, I then cropped the image to the required size and saved them.

## Email Reports
Selenium was used again to extract the data in the report. Once the data was collected, an email was sent out to the desired recipents. The file was designed to be able to be triggered by the slackbot, or sent out at a specific time daily. 

## Slackbot
The slackbot was created using a slack app and incorporating different API's such as RTM (Real Time Messaging) and files.upload. It was designed to be able to request data at any point in time and have an updated score. When prompted for a score, the bot would return a statement and the corresponding graphic image saved from the selenium script. Make sure to run this on a seperate virtual environment, steps to run and create this will be below.

Make sure to use a proxy if working on a corporate network.

### Steps to start slackbot:
Make sure to start on a server!

1. Open CMD
2. CD into folder and run activate.bat
3. Once you are in the virtual environment, set a virtual environment variable (for security purposes): 
    Type in the following on windows: "Set SLACK_API_TOKEN=(Bot User OAuth Access Token)"
4. CD into the folder and run slackbot.py

The slackbot is now running! Make sure to run through these steps every time your server shuts off

### Steps to create a virtual environment on windows
Make sure you have PIP installed! If not, "python get-pip.py"

1. Type in "pip install virtualenv"
2. CD into your project
3. Type in "Virtualenv 'environment name'"
4. Activate your virtual env: \path-to-env\Scripts\actiavte.bat (move activate.bat to main directory for easier accesss)
5. Refer to step 3 and 4 of "Steps to start slackbot"

<strong>NOTE: MAKE SURE ALL MODULES ARE UP TO DATE (slackclient 2.1.0 +)</strong><br>
If you have any questions feel free to contact me at: wrichiekkar.me -> Get in touch

