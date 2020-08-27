
#web app

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('AI3gfpd6tjj332T2HuV07U3McGaDgo0NI1N606cOjKuBBMitbCHmmc5y7coJLJcX6FYItmRUU1idoRwLiIgEx6rQ/mUd1T2KmFukMxkvgumrbyBJ7RRtyS8ucNEEZXjWarvxqKYg7mUFLfoALGNUWAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('29a8b7e4ac4ac99362321c4d8824b3c9')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()