import os
import slack
import Score
import EmailReports

@slack.RTMClient.run_on(event='message')
def RTM(**payload):

    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    
    channel_id = data['channel']
    data['text'] = data['text'].lower()

    if not 'subtype' in data:  #  If subtype field is present, a bot is sending the message (prevents loops)
        
        if (('hello' in data['text']) or ('hi' in data['text']) or ('hey' in data['text'])) and not ('graphic' in data['text']) :
            user = data['user'] #  Gets username
            web_client.chat_postMessage(
                channel=channel_id, #  post to specific channel
                text=f"Hi <@{user}>!")

        if data['text'] == 'help':
            web_client.chat_postMessage(
                channel=channel_id,
                text=('I can:'
                    '\n1. Email a report.'
                    '\n2. Email a text report.'
                    '\n3. Get the Shop English score.'
                    '\n4. Get the Shop French score.'
                    '\n5. Get the Support English score.'
                    '\n6. Get the Support French score.'
                    '\n7. Get the total score.'
                    ))
                        
        if (('average' in data['text']) or ('total' in data['text'])) and ('score' in data['text']):
            web_client.chat_postMessage(
                channel=channel_id,
                text=("The average accessibility score today is: ")
                )
            filename='ENTER FILENAME'
            post_img(filename, channel_id)
        
        if (('bellen' in data['text']) or ('shop english' in data['text']) or ('shop en' in data['text'])) and ('score' in data['text']):
            web_client.chat_postMessage(
                channel=channel_id,
                text=("The accessibility score for Shop English today is: ")
                )
            filename='ENTER FILENAME'
            post_img(filename, channel_id)
        
        if (('bellfr' in data['text']) or ('shop french' in data['text']) or ('shop fr' in data['text'])) and ('score' in data['text']):
            web_client.chat_postMessage(
                channel=channel_id,
                text=("The accessibility score for Shop French today is: ")
                )
            filename='ENTER FILENAME'
            post_img(filename, channel_id)
        
        if (('supen' in data['text']) or ('support english' in data['text']) or ('support en' in data['text'])) and ('score' in data['text']):
            web_client.chat_postMessage(
                channel=channel_id,
                text=("The accessibility score for Support English today is: ")
                )
            filename='ENTER FILENAME'
            post_img(filename, channel_id)
        
        if (('supfr' in data['text']) or ('support french' in data['text']) or ('support fr' in data['text'])) and ('score' in data['text']):
            web_client.chat_postMessage(
                channel=channel_id,
                text=("The accessibility score for Support French today is: ")
                )
            filename='ENTER FILENAME'
            post_img(filename, channel_id)
        
        if ('update' in data['text']) and ('score' in data['text']):
            web_client.chat_postMessage(
                channel=channel_id,
                text=("The score is now updating..."),
                )
            Score.call_from_slackbot()
            web_client.chat_postMessage(
                channel=channel_id,
                text=("The score is now updated.")
                )

        if ('report' in data['text']) and not ('text' in data['text']):
            web_client.chat_postMessage(
                channel=channel_id,
                text=("Sending out a graphic report...")
                )
            EmailReports.Slackbot_Screenshot()
        if ('text' in data['text']) and ('report' in data['text']):
            web_client.chat_postMessage(
                channel=channel_id,
                text=("Sending out a text report...")
                )
            EmailReports.Slackbot_Text()

def post_img(filename, channel_id):
    response = client.files_upload(
        channels=channel_id,
        file=filename)
    assert response["ok"]

if __name__ == "__main__":
    slack_token = os.environ["SLACK_API_TOKEN"] #  Get API token from virtual environment (set in Autorun.py)
    client = slack.WebClient(token=slack_token, proxy='ENTER PROXY') 
    rtm_client = slack.RTMClient(token=slack_token, proxy='ENTER PROXY')
    rtm_client.start()
    
