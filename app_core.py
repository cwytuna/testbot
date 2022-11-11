from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('T0HwEDTign1i80yWEhT66wBk5jqqGhYLeShPY2+TEmgcBguKGk1YsgNHXgJKmz4huW1Q0WjENef7BbrmHHoKs6tddEsyM/uPMURRrIvpHd+z3t2mbjDA45xC6niuLyV53JEqGG4Kv+mA0Kt+70KMegdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('127293839562d33b530ba756e7baf03b')

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

if __name__ == "__main__":
    app.run()