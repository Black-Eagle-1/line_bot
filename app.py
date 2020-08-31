
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
    msg = event.message.text
    r = '我不懂你的意思，輸入[hi]試試吧!'

    if msg in ['hi', 'Hi', 'HI']:
        r = '哈囉'
    elif msg == '你吃飯了嗎':
        r = '還沒'
    elif msg in ['你幾歲', '你幾歲?', '你多老', '你多老?']:
        r = '我的年紀不是人類能計算出來的'
    elif '你是誰' in msg:
        r = '我是機器人~'
    elif '天氣' in msg:
        r = '全台天氣:https://www.cwb.gov.tw/V8/C/ ，獲得縣市天氣資訊請打[城市名稱]+[天氣]'
    elif msg == '台北天氣':
        r = '台北天氣:https://www.cwb.gov.tw/V8/C/W/County/County.html?CID=63'
    elif msg == '新北天氣':
        r = '新北天氣:https://www.cwb.gov.tw/V8/C/W/County/County.html?CID=65'
    elif msg == '所有指令':
        r = '所有指令:hi, 你吃飯了嗎, 你幾歲, 你是誰, 天氣, 台北天氣, 新北天氣'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()