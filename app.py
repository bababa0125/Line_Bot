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

line_bot_api = LineBotApi('r13Lsepj0Y+Q8y2QhdCB1bJ6AEW6VT65TiOeqZxwAA46oKyTMb3E9PatowoMYUcu1AQAMR83jg4wbstMw1V0ywLzROxk61R4mvSxUZw7XWN7owzpuCu6uG3WVlpDuiokZCYwPoXSvyQ1/pGj6IzNeAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('54a52f58187ab9b2755d9ff32b7f4485')


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
    s = "不好意思，你講得太複雜"

    if msg in [HI,Hi,hi] :
        r = 'Hi !!'
    elif msg == '你吃飯了嗎' :
        r = '還沒'
    elif msg == "你是誰" :
        r = '我是機器人'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()