import os
import time
from slackclient import SlackClient
import json

BOT_ID = os.environ.get("BOT_ID")
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

haiku_channel = os.environ.get('HAIKU_CHANNEL')

with open('syllables.json') as fh:
    SYLLABLES = json.load(fh)

def send_message(message):
    slack_client.api_call(
        "chat.postMessage",
        channel=haiku_channel,
        text=message,
        username="Pumbaku",
        icon_url="https://i.imgur.com/E99pb1h.jpg",
    )

def find_haiku(message):
    print('checking for haiku in: "{0}"'.format(message))

    words = [w.rstrip('.').rstrip('?').rstrip('!').rstrip(',') for w in message.strip().upper().split()]

    count_syl = 0
    temp_words = []
    line1 = ''
    line2 = ''
    line3 = ''
    haiku = False

    for word in words:
        try:
            count_syl += SYLLABLES[word]
            temp_words.append(word)
            if count_syl == 5 and line1 == '':
                line1 = ' '.join(temp_words)
                temp_words = []
            elif count_syl == 12:
                line2 = ' '.join(temp_words)
                temp_words = []
            elif count_syl == 17:
                line3 = ' '.join(temp_words)
                temp_words = []
                haiku = True
        except KeyError:
            return('PUMBAKU DO NOT KNOW {0}'.format(word))

    if haiku and count_syl == 17:
        return('{0}\n{1}\n{2}'.format(line1, line2, line3))
    else:
        return('HAS {0} SYLLABLES! IS NOT HAIKU!'.format(count_syl))

def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output:
                if not output.get('channel') == haiku_channel:
                    # ignore messages from other channels
                    continue
                if not output.get('type') == 'message':
                    # ignore non messages
                    continue
                elif output.get('user') == BOT_ID:
                    # ignore messages from self
                    continue

                message = output.get('text') or ''
                if not len(message):
                    continue
                return message
    return None


if __name__ == "__main__":
    if os.environ.get('DEBUG'):
        while True:
            message = input('message: ')
            if message == '':
                break
            print(find_haiku(message))
    elif slack_client.rtm_connect():
        print("Pumbaku connected and running!")
        while True:
            output = parse_slack_output(slack_client.rtm_read())
            if output:
                message = find_haiku(output)
                if message:
                    send_message(message)
            time.sleep(1)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")